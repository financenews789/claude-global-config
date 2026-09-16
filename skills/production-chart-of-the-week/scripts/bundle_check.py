# -*- coding: utf-8 -*-
"""Blocking assertions for the Chart of the Week import bundle (ÉTAPE 10).

The bundle is never hand-assembled: a cycle's build_bundle.py builds the dict,
calls check_bundle(bundle, spec) and writes the file only if the returned list
is empty. Every rule of production-chart-of-the-week, hub-card-etude and
eco3min-import-contenu-bilingue that can be checked mechanically is here, so it
is written once instead of being re-typed (and drifting) every cycle.

    import os, sys
    sys.path.insert(0, os.path.expanduser(
        '~/.claude/skills/production-chart-of-the-week/scripts'))
    from bundle_check import check_bundle, write_or_refuse

    spec = dict(
        png={'en': 'cycle21_chart_desktop_16x9.png', 'fr': 'cycle21_chart_desktop_16x9_fr.png'},
        csv='cycle21_bigmac_worktime_data.csv',
        uploads='https://eco3min.fr/wp-content/uploads/2026/09/',
        shortcode={'en': '[eco3min_chart_x]', 'fr': '[eco3min_chart_x lang="fr"]'},
        shortcode_name='eco3min_chart_x',
        slugs={'en': 'slug-en', 'fr': 'slug-fr'},
        publish='2026-09-22',
        badge={'en': 'September 22, 2026', 'fr': '22 septembre 2026'},
        figures={'en': ['7.3', '62.6'], 'fr': ['7,3', '62,6']},   # in content AND on the card
        stale=['77.1', '77,1', 'tenfold', '2024'],                  # nowhere in the bundle
        snippet_must_contain=["add_shortcode('eco3min_chart_x'"],
    )
    write_or_refuse(bundle, spec, out_path)

`png` may be one string (same file for both pages) or a dict per language.
"""
import json
import os
import re

HUB_EN_ID, HUB_FR_ID = 12664, 12662
GRID = '<div class="eco3-grid">'
EM_DASH = '—'
BANNED_PRESCRIPTIVE = ('should ', 'must buy', ' buy ', ' sell ', 'allocate', 'price target',
                       'cheapest country', 'best country', 'worst country')
REGULATORY = ('AMF', 'registered with', 'enregistré auprès', 'agréé')


def check_bundle(bundle, spec):
    fail = []

    def check(cond, msg):
        if not cond:
            fail.append(msg)

    png = spec['png']
    png_by_lang = png if isinstance(png, dict) else {'en': png, 'fr': png}
    uploads = spec['uploads']
    csv_url = uploads + spec['csv']
    min_gap = spec.get('min_gap', 3000)
    card_words = spec.get('card_words', (95, 150))
    banned = spec.get('banned_words', BANNED_PRESCRIPTIVE)

    pages = bundle.get('pages', {})
    check(set(pages) == {'en', 'fr'}, 'bundle must carry exactly en and fr pages')
    for lang, page in pages.items():
        body = page.get('content', '')
        png_url = uploads + png_by_lang[lang]
        check(page.get('post_type') == 'page', '%s: post_type must be page' % lang)
        check(page.get('lang') == lang, '%s: lang field drift' % lang)
        check(page.get('slug') == spec['slugs'][lang], '%s: slug drift' % lang)
        check(not re.findall(r'<!--.*?-->', body, re.S), '%s: HTML comment in content' % lang)
        check('<script' not in body, '%s: <script> in content' % lang)
        check('ld+json' not in body, '%s: inline JSON-LD in content' % lang)
        check(body.count(png_url) == 1, '%s: figure src must use the uploads URL exactly once' % lang)
        check(csv_url in body, '%s: CSV download link missing' % lang)
        check('{N}' not in body, '%s: {N} placeholder left in content' % lang)
        check(page.get('featured_image') == png_url, '%s: featured_image drift' % lang)
        seo = page.get('seo', {})
        check(seo.get('og_image') == png_url, '%s: og_image drift' % lang)
        ld = page.get('json_ld') or []
        check(len(ld) >= 2, '%s: json_ld must carry Article and Dataset' % lang)
        if len(ld) >= 2:
            check(ld[0].get('image') == png_url, '%s: json_ld Article image drift' % lang)
            dist = (ld[1].get('distribution') or [{}])[0]
            check(dist.get('contentUrl') == csv_url, '%s: Dataset contentUrl drift' % lang)
            check(ld[0].get('datePublished') == spec['publish'], '%s: datePublished != publish date' % lang)
        check(len(seo.get('title', '')) <= 60, '%s: seo title %d chars' % (lang, len(seo.get('title', ''))))
        check(150 <= len(seo.get('description', '')) <= 160,
              '%s: seo description %d chars' % (lang, len(seo.get('description', ''))))
        check(seo.get('robots') == ['index', 'follow'], '%s: robots must be index,follow' % lang)
        check(EM_DASH not in body, '%s: em dash in content' % lang)
        check(body.count('<div') == body.count('</div>'), '%s: unbalanced <div>' % lang)
        for word in REGULATORY:
            check(word not in body, '%s: regulatory status wording %r in content' % (lang, word))
        short = spec['shortcode'][lang]
        check(body.startswith(short), '%s: content must open with the shortcode %s' % (lang, short))
        i_fig = body.find('<figure')
        check(i_fig > min_gap, '%s: static PNG too close to the interactive chart (%d chars)' % (lang, i_fig))
        check(body.count('<h2') >= 4, '%s: article looks truncated' % lang)
        for figure in spec.get('figures', {}).get(lang, ()):
            check(figure in body, '%s: article missing figure %s' % (lang, figure))

    check(pages.get('en', {}).get('slug') != pages.get('fr', {}).get('slug'), 'slugs must differ')

    snip = bundle.get('snippet', {})
    code = snip.get('code', '')
    check(not code.lstrip().startswith('<?php'), 'snippet code starts with <?php')
    check('cdnjs.cloudflare.com' not in code, 'snippet loads a CDN blocked by the CSP')
    check(EM_DASH not in code, 'em dash in snippet')
    check(snip.get('scope') == 'global', 'snippet scope must be global')
    for needle in spec.get('snippet_must_contain', ()):
        check(needle in code, 'snippet missing %r' % needle)

    hubs = bundle.get('hubs', {})
    check(hubs.get('en', {}).get('post_id') == HUB_EN_ID, 'EN hub id must be %d' % HUB_EN_ID)
    check(hubs.get('fr', {}).get('post_id') == HUB_FR_ID, 'FR hub id must be %d' % HUB_FR_ID)
    slug_en, slug_fr = spec['slugs']['en'], spec['slugs']['fr']
    for lang, hub in hubs.items():
        card = hub.get('card_html', '')
        check(not re.findall(r'<!--.*?-->', card, re.S), '%s hub: HTML comment in card' % lang)
        check(card.count('\n  <a class="eco3-card__media"') == 1, '%s hub: media anchor must be on one line' % lang)
        check(EM_DASH not in card, '%s hub: em dash in card' % lang)
        check(hub.get('insert_after') == GRID, '%s hub: wrong insertion anchor' % lang)
        check(hub.get('dedupe_marker') == ('/en/%s/' % slug_en if lang == 'en' else '/%s/' % slug_fr),
              '%s hub: dedupe_marker must be the canonical href' % lang)
        m = re.search(r'eco3-card__desc">(.*?)</p>', card, re.S)
        words = len(re.sub(r'<[^>]+>', ' ', m.group(1)).split()) if m else 0
        check(card_words[0] <= words <= card_words[1], '%s hub: card description is %d words' % (lang, words))
        check(spec['badge'][lang] in card, '%s hub: badge date must be %s' % (lang, spec['badge'][lang]))
        low = card.lower()
        for word in banned:
            check(word not in low, '%s hub: prescriptive wording %r' % (lang, word))
        for figure in spec.get('figures', {}).get(lang, ()):
            check(figure in card, '%s hub: card missing figure %s' % (lang, figure))
    en_card = hubs.get('en', {}).get('card_html', '')
    fr_card = hubs.get('fr', {}).get('card_html', '')
    check('lang-note' in en_card, 'EN card must carry the lang note')
    check('lang-note' not in fr_card, 'FR card must not carry a lang note')
    check('path="en/%s"' % slug_en in en_card, 'EN card featured image needs the en/ prefix')
    check('path="%s"' % slug_fr in fr_card, 'FR card featured image must use the bare slug')
    check('/%s/' % slug_fr in en_card, 'EN lang note must point at the FR slug')
    check('Read the study' in en_card and 'Lire l' in fr_card, 'card CTA wording drift')

    check(bundle.get('cycle', {}).get('date') == spec['publish'], 'cycle.date != publish date')
    check(bundle.get('polylang', {}).get('link_translations') is True, 'polylang.link_translations must be true')

    dump = json.dumps(bundle, ensure_ascii=False)
    check(EM_DASH not in dump, 'em dash somewhere in the bundle')
    for stale in spec.get('stale', ()):
        check(stale not in dump, 'stale figure in bundle: %r' % stale)
    return fail


def write_or_refuse(bundle, spec, out_path):
    fail = check_bundle(bundle, spec)
    if fail:
        print('REFUSING TO WRITE, %d blocking issue(s):' % len(fail))
        for f in fail:
            print(' -', f)
        raise SystemExit(1)
    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(bundle, fh, ensure_ascii=False, indent=2)
    size = os.path.getsize(out_path)
    print('written      : %s (%.1f Ko)' % (out_path, size / 1024))
    return size
