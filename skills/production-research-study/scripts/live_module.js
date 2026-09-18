(function () {
  'use strict';
  if (window.__eco3Pivot2yLive) return;
  window.__eco3Pivot2yLive = true;

  var PAL = ['#B85C3C', '#1A1A1A', '#4A6B8A'];
  var INK = '#1A1A1A', MUTED = '#757575', GRID = '#E0E0E0', SHADE = 'rgba(117,117,117,.14)';
  var UP = '#C73E2E', DOWN = '#4A6B8A';
  var SANS = 'Inter, "DM Sans", system-ui, sans-serif', MONO = '"IBM Plex Mono", "JetBrains Mono", ui-monospace, monospace';
  var NS = 'http://www.w3.org/2000/svg';
  var L = {
    en: { spread: 'Spread', regime: 'Regime', bp: 'bp', hike: 'Fed reversal to hiking', ease: 'Fed reversal to easing',
          pin: 'pinned, click the marker again to release', window: 'Time window',
          reg: { deeply_inverted: 'deep inversion', mildly_inverted: 'negative', neutral: 'neutral',
                 mildly_positive: 'positive', deeply_positive: 'very positive' },
          aria: 'Interactive chart; full values in the downloadable CSV.', loc: 'en-GB' },
    fr: { spread: 'Spread', regime: 'Régime', bp: 'pb', hike: 'retournement Fed vers la hausse', ease: 'retournement Fed vers la baisse',
          pin: 'épinglé, cliquer de nouveau le marqueur pour libérer', window: 'Fenêtre',
          reg: { deeply_inverted: 'inversion profonde', mildly_inverted: 'négatif', neutral: 'neutre',
                 mildly_positive: 'positif', deeply_positive: 'très positif' },
          aria: 'Graphique interactif ; valeurs complètes dans le CSV téléchargeable.', loc: 'fr-FR' }
  };

  function el(n, a) { var e = document.createElementNS(NS, n); for (var k in a) e.setAttribute(k, a[k]); return e; }
  function json(s, d) { if (!s) return d; try { return JSON.parse(s); } catch (err) { return d; } }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  function parseCSV(txt) {
    var rows = [], row = [], f = '', q = false, i, c;
    txt = txt.replace(/^﻿/, '').replace(/\r\n?/g, '\n');
    for (i = 0; i < txt.length; i++) {
      c = txt[i];
      if (q) {
        if (c === '"') { if (txt[i + 1] === '"') { f += '"'; i++; } else q = false; }
        else f += c;
      } else if (c === '"') q = true;
      else if (c === ',') { row.push(f); f = ''; }
      else if (c === '\n') { row.push(f); rows.push(row); row = []; f = ''; }
      else f += c;
    }
    if (f.length || row.length) { row.push(f); rows.push(row); }
    if (!rows.length) return [];
    var head = rows.shift().map(function (h) { return h.trim(); });
    return rows.filter(function (r) { return r.length === head.length; })
               .map(function (r) { var o = {}; head.forEach(function (h, j) { o[h] = r[j]; }); return o; });
  }

  function toDate(v) {
    v = (v || '').trim();
    if (/^\d{4}-\d{2}$/.test(v)) return new Date(v + '-15T00:00:00Z');
    var d = new Date(v + (v.length === 10 ? 'T00:00:00Z' : ''));
    return isNaN(d) ? null : d;
  }
  function ym(d) { return d.getUTCFullYear() + '-' + ('0' + (d.getUTCMonth() + 1)).slice(-2); }
  function niceTicks(lo, hi, n) {
    var span = hi - lo; if (!(span > 0)) return [lo];
    var raw = span / n, mag = Math.pow(10, Math.floor(Math.log(raw) / Math.LN10)), norm = raw / mag,
        step = (norm >= 5 ? 10 : norm >= 2 ? 5 : norm >= 1 ? 2 : 1) * mag,
        t = [], v = Math.ceil(lo / step) * step;
    for (; v <= hi + step * 1e-9; v += step) t.push(+v.toFixed(10));
    return t;
  }

  function build(fig) {
    var cfg = {
      csv: fig.getAttribute('data-csv'),
      x: fig.getAttribute('data-x') || 'date',
      series: json(fig.getAttribute('data-series'), []),
      unit: fig.getAttribute('data-unit') || '',
      dec: parseInt(fig.getAttribute('data-decimals') || '2', 10),
      ranges: json(fig.getAttribute('data-ranges'), [{ label: 'All', years: 0 }]),
      shade: json(fig.getAttribute('data-shade'), []),
      extra: json(fig.getAttribute('data-extra'), []),
      markers: json(fig.getAttribute('data-markers'), null),
      ylab: fig.getAttribute('data-y-label') || '',
      src: fig.getAttribute('data-source') || '',
      lang: (fig.getAttribute('data-lang') || 'en').slice(0, 2)
    };
    if (!cfg.csv || !cfg.series.length) return;
    fetch(cfg.csv, { credentials: 'omit' })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })
      .then(function (txt) { render(fig, cfg, parseCSV(txt)); })
      .catch(function () { /* the static picture stays: intended */ });
  }

  function render(fig, cfg, rows) {
    var T = L[cfg.lang] || L.en;
    var data = rows.map(function (r) {
      var o = { d: toDate(r[cfg.x]), raw: r };
      cfg.series.forEach(function (s) { var v = parseFloat(r[s.col]); o[s.col] = isNaN(v) ? null : v; });
      return o;
    }).filter(function (o) { return o.d; }).sort(function (a, b) { return a.d - b.d; });
    if (data.length < 2) return;
    var fmtDate = function (d) { return d.toLocaleDateString(T.loc, { year: 'numeric', month: 'short', timeZone: 'UTC' }); };
    var fmtNum = function (v, dec) { return v.toLocaleString(T.loc, { minimumFractionDigits: dec, maximumFractionDigits: dec }); };

    var on = cfg.series.map(function () { return true; }), range = 0, pinned = -1;

    var wrap = document.createElement('div');
    wrap.className = 'eco3-pivot2y-live-wrap';
    wrap.innerHTML =
      '<div class="eco3-pivot2y-live-bar">' +
        '<div class="eco3-pivot2y-live-ranges" role="group" aria-label="' + esc(T.window) + '"></div>' +
        '<div class="eco3-pivot2y-live-legend"></div>' +
      '</div>' +
      '<div class="eco3-pivot2y-live-plot"></div>' +
      '<output class="eco3-pivot2y-live-readout" aria-live="polite"></output>' +
      (cfg.src ? '<div class="eco3-pivot2y-live-src">' + cfg.src + '</div>' : '');

    var pic = fig.querySelector('picture'), cap = fig.querySelector('figcaption');
    if (cap) fig.insertBefore(wrap, cap); else fig.appendChild(wrap);
    if (pic) pic.hidden = true;

    var elRanges = wrap.querySelector('.eco3-pivot2y-live-ranges'),
        elLegend = wrap.querySelector('.eco3-pivot2y-live-legend'),
        elPlot   = wrap.querySelector('.eco3-pivot2y-live-plot'),
        elOut    = wrap.querySelector('.eco3-pivot2y-live-readout');

    cfg.ranges.forEach(function (r, i) {
      var b = document.createElement('button');
      b.type = 'button'; b.textContent = r.label;
      b.setAttribute('aria-pressed', i === 0 ? 'true' : 'false');
      b.addEventListener('click', function () {
        range = i; pinned = -1;
        [].forEach.call(elRanges.children, function (x, j) { x.setAttribute('aria-pressed', j === i ? 'true' : 'false'); });
        draw();
      });
      elRanges.appendChild(b);
    });
    cfg.series.forEach(function (s, i) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'eco3-pivot2y-live-key';
      b.setAttribute('aria-pressed', 'true');
      b.innerHTML = '<span style="background:' + PAL[i % PAL.length] + '"></span>' + esc(s.label);
      b.addEventListener('click', function () {
        if (on.filter(Boolean).length === 1 && on[i]) return;
        on[i] = !on[i]; b.setAttribute('aria-pressed', on[i] ? 'true' : 'false'); draw();
      });
      elLegend.appendChild(b);
    });
    if (cfg.markers) {
      var k1 = document.createElement('span'); k1.className = 'eco3-pivot2y-live-mk';
      k1.innerHTML = '<span style="border-bottom-color:' + UP + '"></span>' + esc(T.hike);
      var k2 = document.createElement('span'); k2.className = 'eco3-pivot2y-live-mk';
      k2.innerHTML = '<span class="eco3-pivot2y-live-mk-down" style="border-top-color:' + DOWN + '"></span>' + esc(T.ease);
      elLegend.appendChild(k1); elLegend.appendChild(k2);
    }

    var view = [];

    function draw() {
      var yrs = cfg.ranges[range].years, cut = null;
      if (yrs) { cut = new Date(data[data.length - 1].d); cut.setUTCFullYear(cut.getUTCFullYear() - yrs); }
      view = cut ? data.filter(function (o) { return o.d >= cut; }) : data.slice();
      if (view.length < 2) view = data.slice();

      var W = Math.max(elPlot.clientWidth || 720, 300), H = Math.round(Math.min(Math.max(W * 0.52, 240), 430)),
          M = { t: 16, r: 16, b: 30, l: 46 };
      var lo = Infinity, hi = -Infinity;
      view.forEach(function (o) {
        cfg.series.forEach(function (s, i) {
          if (!on[i] || o[s.col] === null) return;
          if (o[s.col] < lo) lo = o[s.col]; if (o[s.col] > hi) hi = o[s.col];
        });
      });
      if (!isFinite(lo)) return;
      if (lo === hi) { lo -= 1; hi += 1; }
      var pad = (hi - lo) * 0.08; lo -= pad; hi += pad;
      if (lo < 0 && yrs === 0) lo = 0;

      var t0 = view[0].d.getTime(), t1 = view[view.length - 1].d.getTime();
      var X = function (d) { return M.l + (d.getTime() - t0) / (t1 - t0) * (W - M.l - M.r); };
      var Y = function (v) { return M.t + (hi - v) / (hi - lo) * (H - M.t - M.b); };

      var svg = el('svg', {
        viewBox: '0 0 ' + W + ' ' + H, width: '100%', height: H, role: 'img', tabindex: '0',
        'aria-label': cfg.series.filter(function (s, i) { return on[i]; }).map(function (s) { return s.label; }).join(', ') +
          ', ' + fmtDate(view[0].d) + ' - ' + fmtDate(view[view.length - 1].d) + '. ' + T.aria
      });

      cfg.shade.forEach(function (b) {
        var a = toDate(b.from), z = toDate(b.to); if (!a || !z) return;
        var xa = Math.max(X(a), M.l), xz = Math.min(X(z), W - M.r); if (xz <= xa) return;
        svg.appendChild(el('rect', { x: xa, y: M.t, width: xz - xa, height: H - M.t - M.b, fill: SHADE }));
        if (b.label && xz - xa > 30) {
          var lb = el('text', { x: (xa + xz) / 2, y: M.t + 11, 'text-anchor': 'middle', fill: MUTED, 'font-family': MONO, 'font-size': 10 });
          lb.textContent = b.label; svg.appendChild(lb);
        }
      });
      niceTicks(lo, hi, 5).forEach(function (v) {
        var y = Y(v);
        svg.appendChild(el('line', { x1: M.l, x2: W - M.r, y1: y, y2: y, stroke: GRID, 'stroke-width': 1 }));
        var tx = el('text', { x: M.l - 8, y: y + 4, 'text-anchor': 'end', fill: MUTED, 'font-family': MONO, 'font-size': 11 });
        tx.textContent = v + (cfg.unit === '%' ? '%' : ''); svg.appendChild(tx);
      });
      if (cfg.ylab) {
        var yl = el('text', { fill: MUTED, 'font-family': SANS, 'font-size': 11, 'text-anchor': 'middle',
                              transform: 'translate(11,' + (M.t + (H - M.t - M.b) / 2) + ') rotate(-90)' });
        yl.textContent = cfg.ylab; svg.appendChild(yl);
      }
      var y0 = new Date(t0).getUTCFullYear(), y1 = new Date(t1).getUTCFullYear();
      var years = y1 - y0 >= 4 ? niceTicks(y0, y1, Math.max(3, Math.floor(W / 110))) : null;
      if (years) {
        years.forEach(function (yr) {
          var d = new Date(Date.UTC(yr, 0, 1)); if (d < view[0].d || d > view[view.length - 1].d) return;
          var tx = el('text', { x: X(d), y: H - 10, 'text-anchor': 'middle', fill: MUTED, 'font-family': MONO, 'font-size': 11 });
          tx.textContent = yr; svg.appendChild(tx);
        });
      } else {
        view.forEach(function (o, k) {
          if (o.d.getUTCMonth() % 3 !== 0) return;
          var tx = el('text', { x: X(o.d), y: H - 10, 'text-anchor': 'middle', fill: MUTED, 'font-family': MONO, 'font-size': 10 });
          tx.textContent = fmtDate(o.d); svg.appendChild(tx);
        });
      }

      cfg.series.forEach(function (s, i) {
        if (!on[i]) return;
        var d = '', pen = false;
        view.forEach(function (o) {
          if (o[s.col] === null) { pen = false; return; }
          d += (pen ? 'L' : 'M') + X(o.d).toFixed(1) + ' ' + Y(o[s.col]).toFixed(1) + ' '; pen = true;
        });
        svg.appendChild(el('path', { d: d, fill: 'none', stroke: PAL[i % PAL.length], 'stroke-width': 1.7, 'stroke-linejoin': 'round' }));
      });

      var cross = el('line', { y1: M.t, y2: H - M.b, stroke: INK, 'stroke-width': 1, 'stroke-dasharray': '3 3', opacity: 0 });
      svg.appendChild(cross);
      var dots = cfg.series.map(function (s, i) {
        var c = el('circle', { r: 3.5, fill: PAL[i % PAL.length], stroke: '#FFF', 'stroke-width': 1.5, opacity: 0 });
        svg.appendChild(c); return c;
      });

      var idx = -1;
      function markerOf(o) {
        if (!cfg.markers || o.raw[cfg.markers.col] !== '1') return null;
        var dir = (cfg.markers.dirs || {})[ym(o.d)] || 'up';
        return dir;
      }
      function at(px) {
        var best = 0, bd = Infinity;
        view.forEach(function (o, k) { var dd = Math.abs(X(o.d) - px); if (dd < bd) { bd = dd; best = k; } });
        show(best);
      }
      function show(k) {
        idx = k; var o = view[k];
        cross.setAttribute('x1', X(o.d)); cross.setAttribute('x2', X(o.d)); cross.setAttribute('opacity', 1);
        var parts = ['<b>' + esc(fmtDate(o.d)) + '</b>'];
        cfg.series.forEach(function (s, i) {
          if (!on[i] || o[s.col] === null) { dots[i].setAttribute('opacity', 0); return; }
          dots[i].setAttribute('cx', X(o.d)); dots[i].setAttribute('cy', Y(o[s.col])); dots[i].setAttribute('opacity', 1);
          parts.push('<span><i style="background:' + PAL[i % PAL.length] + '"></i>' + esc(s.label) +
                     ' <b>' + fmtNum(o[s.col], cfg.dec) + (cfg.unit ? cfg.unit : '') + '</b></span>');
        });
        cfg.extra.forEach(function (x) {
          var v = o.raw[x.col]; if (v === undefined || v === '') return;
          if (x.map === 'regime') { parts.push('<span>' + esc(T.regime) + ' <b>' + esc(T.reg[v] || v) + '</b></span>'); return; }
          var n = parseFloat(v); if (isNaN(n)) return;
          parts.push('<span>' + esc(x.label) + ' <b>' + (n > 0 ? '+' : '') + fmtNum(n, x.dec || 0) + ' ' + esc(T.bp) + '</b></span>');
        });
        var mk = markerOf(o);
        if (mk) parts.push('<span class="eco3-pivot2y-live-flag" style="color:' + (mk === 'up' ? UP : DOWN) + '">' + esc(mk === 'up' ? T.hike : T.ease) +
                           (pinned === k ? ' (' + esc(T.pin) + ')' : '') + '</span>');
        elOut.innerHTML = parts.join('');
      }
      function hide() {
        if (pinned >= 0 && pinned < view.length) { show(pinned); return; }
        cross.setAttribute('opacity', 0); dots.forEach(function (c) { c.setAttribute('opacity', 0); }); elOut.innerHTML = '';
      }

      if (cfg.markers) {
        var si = cfg.series.map(function (s) { return s.col; }).indexOf(cfg.markers.on);
        var col = si >= 0 ? cfg.markers.on : cfg.series[0].col;
        view.forEach(function (o, k) {
          var mk = markerOf(o); if (!mk || o[col] === null || !on[Math.max(si, 0)]) return;
          var x = X(o.d), y = Y(o[col]), s = 5.5;
          var pts = mk === 'up' ? (x + ',' + (y - s) + ' ' + (x - s) + ',' + (y + s) + ' ' + (x + s) + ',' + (y + s))
                                : (x + ',' + (y + s) + ' ' + (x - s) + ',' + (y - s) + ' ' + (x + s) + ',' + (y - s));
          var tri = el('polygon', { points: pts, fill: mk === 'up' ? UP : DOWN, stroke: '#FFF', 'stroke-width': 1, cursor: 'pointer' });
          tri.addEventListener('click', function (e) { e.stopPropagation(); pinned = (pinned === k) ? -1 : k; show(k); });
          svg.appendChild(tri);
        });
      }

      svg.addEventListener('pointermove', function (e) {
        var r = svg.getBoundingClientRect();
        at((e.clientX - r.left) * (W / r.width));
      });
      svg.addEventListener('pointerleave', hide);
      svg.addEventListener('focus', function () { show(idx < 0 ? view.length - 1 : idx); });
      svg.addEventListener('blur', hide);
      svg.addEventListener('keydown', function (e) {
        if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
        e.preventDefault();
        var k = idx < 0 ? view.length - 1 : idx + (e.key === 'ArrowRight' ? 1 : -1);
        show(Math.max(0, Math.min(view.length - 1, k)));
      });

      elPlot.innerHTML = ''; elPlot.appendChild(svg);
      show(pinned >= 0 && pinned < view.length ? pinned : view.length - 1);
    }

    draw();
    var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(draw, 160); });
  }

  function init() { [].forEach.call(document.querySelectorAll('[data-eco3-live="pivot2y"]'), build); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
