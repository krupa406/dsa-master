/**
 * DSA Visualizer Engine
 * Interactive step-through animations for data structure & algorithm concepts.
 * Each viz is driven by a declarative config placed in a <div class="dsa-viz" data-viz="...">
 */

(function () {
  'use strict';

  const SPEED_DEFAULT = 700;

  /* =====================================================================
   *  UTILITY HELPERS
   * ===================================================================== */
  function el(tag, cls, html) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html !== undefined) e.innerHTML = html;
    return e;
  }

  function clearKids(node) { while (node.firstChild) node.removeChild(node.firstChild); }

  /* =====================================================================
   *  RENDERERS — one per viz type
   * ===================================================================== */

  // ---------- ARRAY (sorting, searching, general) ----------
  function renderArray(canvas, state) {
    clearKids(canvas);
    const row = el('div', 'viz-array');
    const ptrRow = el('div', 'viz-pointers');
    state.arr.forEach((v, i) => {
      const c = el('div', 'viz-cell', v);
      if (state.classes && state.classes[i]) c.classList.add(state.classes[i]);
      const idx = el('span', 'viz-cell-index', i);
      c.appendChild(idx);
      row.appendChild(c);

      // pointer label
      const p = el('div', 'viz-pointer-slot');
      if (state.pointers) {
        Object.entries(state.pointers).forEach(([name, pi]) => {
          if (pi === i) { p.textContent = name; p.classList.add('ptr-' + name); }
        });
      }
      ptrRow.appendChild(p);
    });
    canvas.appendChild(row);
    canvas.appendChild(ptrRow);
  }

  // ---------- LINKED LIST ----------
  function renderLinkedList(canvas, state) {
    clearKids(canvas);
    const row = el('div', 'viz-ll');
    state.nodes.forEach((v, i) => {
      const node = el('div', 'viz-ll-node');
      const box = el('div', 'viz-ll-box', v);
      if (state.classes && state.classes[i]) box.classList.add(state.classes[i]);
      node.appendChild(box);
      if (i < state.nodes.length - 1) {
        const arrow = el('span', 'viz-ll-arrow', '→');
        if (state.classes && state.classes[i] === 'active') arrow.classList.add('active');
        node.appendChild(arrow);
      }
      row.appendChild(node);
    });
    const nil = el('span', 'viz-ll-null', '→ null');
    row.appendChild(nil);
    canvas.appendChild(row);
  }

  // ---------- STACK ----------
  function renderStack(canvas, state) {
    clearKids(canvas);
    const labelTop = el('div', '', '<small style="color:var(--text-light);font-weight:600;font-size:.75rem">← TOP</small>');
    const stack = el('div', 'viz-stack');
    state.items.forEach((v, i) => {
      const it = el('div', 'viz-sq-item', v);
      if (state.classes && state.classes[i]) it.classList.add(state.classes[i]);
      stack.appendChild(it);
    });
    canvas.appendChild(labelTop);
    canvas.appendChild(stack);
  }

  // ---------- QUEUE ----------
  function renderQueue(canvas, state) {
    clearKids(canvas);
    const labels = el('div', '', '<small style="color:var(--text-light);font-weight:600;font-size:.72rem">FRONT →&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→ REAR</small>');
    const q = el('div', 'viz-queue');
    state.items.forEach((v, i) => {
      const it = el('div', 'viz-sq-item', v);
      if (state.classes && state.classes[i]) it.classList.add(state.classes[i]);
      q.appendChild(it);
    });
    canvas.appendChild(labels);
    canvas.appendChild(q);
  }

  // ---------- BINARY TREE (SVG) ----------
  function renderTree(canvas, state) {
    clearKids(canvas);
    const vals = state.nodes; // array in level-order, null for empty
    if (!vals || vals.length === 0) return;
    const depth = Math.floor(Math.log2(vals.length)) + 1;
    const W = Math.min(500, canvas.clientWidth - 20);
    const H = depth * 64 + 20;
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'viz-tree-svg');
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
    svg.setAttribute('width', W);
    svg.setAttribute('height', H);

    // positions
    const pos = [];
    for (let i = 0; i < vals.length; i++) {
      const d = Math.floor(Math.log2(i + 1));
      const count = Math.pow(2, d);
      const idx = i - count + 1;
      const x = (W / (count + 1)) * (idx + 1);
      const y = d * 60 + 30;
      pos.push({ x, y });
    }

    // edges
    for (let i = 0; i < vals.length; i++) {
      if (vals[i] === null) continue;
      const left = 2 * i + 1, right = 2 * i + 2;
      [left, right].forEach(ch => {
        if (ch < vals.length && vals[ch] !== null) {
          const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          line.setAttribute('class', 'edge-line' + ((state.edgeClasses && state.edgeClasses[ch]) ? ' ' + state.edgeClasses[ch] : ''));
          line.setAttribute('x1', pos[i].x); line.setAttribute('y1', pos[i].y);
          line.setAttribute('x2', pos[ch].x); line.setAttribute('y2', pos[ch].y);
          svg.appendChild(line);
        }
      });
    }

    // nodes
    for (let i = 0; i < vals.length; i++) {
      if (vals[i] === null) continue;
      const circ = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circ.setAttribute('class', 'node-circle' + ((state.classes && state.classes[i]) ? ' ' + state.classes[i] : ''));
      circ.setAttribute('cx', pos[i].x); circ.setAttribute('cy', pos[i].y);
      circ.setAttribute('r', 18);
      circ.setAttribute('fill', '#fff'); circ.setAttribute('stroke', '#cbd5e1'); circ.setAttribute('stroke-width', 2);
      svg.appendChild(circ);
      const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      txt.setAttribute('class', 'node-text');
      txt.setAttribute('x', pos[i].x); txt.setAttribute('y', pos[i].y);
      txt.textContent = vals[i];
      svg.appendChild(txt);
    }
    canvas.appendChild(svg);
  }

  // ---------- HASH TABLE ----------
  function renderHashTable(canvas, state) {
    clearKids(canvas);
    const ht = el('div', 'viz-ht');
    state.buckets.forEach((items, i) => {
      const row = el('div', 'viz-ht-row');
      const idx = el('div', 'viz-ht-idx', i);
      const bucket = el('div', 'viz-ht-bucket');
      if (state.activeIdx === i) bucket.classList.add('active');
      if (items.length > 1) bucket.classList.add('collision');
      bucket.textContent = items.length ? items.join(' → ') : '∅';
      row.appendChild(idx);
      row.appendChild(bucket);
      ht.appendChild(row);
    });
    canvas.appendChild(ht);
  }

  // ---------- GENERIC / TEXT ----------
  function renderText(canvas, state) {
    clearKids(canvas);
    const d = el('div', '', '');
    d.style.cssText = 'text-align:center;font-size:0.95rem;color:var(--text);line-height:1.7;max-width:520px';
    d.innerHTML = state.html;
    canvas.appendChild(d);
  }

  const RENDERERS = {
    array: renderArray,
    linkedlist: renderLinkedList,
    stack: renderStack,
    queue: renderQueue,
    tree: renderTree,
    hashtable: renderHashTable,
    text: renderText,
  };

  /* =====================================================================
   *  VIZ CONTROLLER — manages step-through for each widget
   * ===================================================================== */
  function initViz(container) {
    let config;
    try {
      // Read JSON from a child <script type="application/json"> tag
      const scriptTag = container.querySelector('script[type="application/json"]');
      if (scriptTag) {
        config = JSON.parse(scriptTag.textContent);
      } else {
        // Fallback: try data-viz attribute
        config = JSON.parse(container.getAttribute('data-viz'));
      }
    } catch (e) {
      container.innerHTML = '<p style="color:red">Viz config error: ' + e.message + '</p>';
      return;
    }

    const type = config.type || 'array';
    const steps = config.steps || [];
    const title = config.title || 'Visualization';
    let step = 0;
    let playing = false;
    let timer = null;
    let speed = SPEED_DEFAULT;

    // Build DOM
    const header = el('div', 'dsa-viz-header');
    const titleEl = el('div', 'dsa-viz-title', '👁️ ' + title);

    const controls = el('div', 'dsa-viz-controls');
    const stepInd = el('span', 'viz-step-indicator', '1/' + steps.length);

    const btnPrev = el('button', 'viz-btn', '◀');
    const btnNext = el('button', 'viz-btn', '▶');
    const btnPlay = el('button', 'viz-btn viz-btn-primary', '⏵ Play');
    const btnReset = el('button', 'viz-btn', '↺');

    controls.appendChild(btnPrev);
    controls.appendChild(btnNext);
    controls.appendChild(btnPlay);
    controls.appendChild(btnReset);
    controls.appendChild(stepInd);

    header.appendChild(titleEl);
    header.appendChild(controls);

    const canvas = el('div', 'dsa-viz-canvas');
    const footer = el('div', 'dsa-viz-footer');

    clearKids(container);
    container.appendChild(header);
    container.appendChild(canvas);
    container.appendChild(footer);

    // Render
    function render() {
      const s = steps[step];
      stepInd.textContent = (step + 1) + '/' + steps.length;
      footer.textContent = s.desc || '';
      btnPrev.disabled = step === 0;
      btnNext.disabled = step === steps.length - 1;
      const renderer = RENDERERS[type] || RENDERERS.text;
      renderer(canvas, s.state);
    }

    function next() { if (step < steps.length - 1) { step++; render(); } else { stopPlay(); } }
    function prev() { if (step > 0) { step--; render(); } }
    function reset() { stopPlay(); step = 0; render(); }

    function startPlay() {
      playing = true;
      btnPlay.textContent = '⏸ Pause';
      timer = setInterval(() => {
        if (step < steps.length - 1) { step++; render(); } else { stopPlay(); }
      }, speed);
    }
    function stopPlay() {
      playing = false;
      btnPlay.textContent = '⏵ Play';
      if (timer) { clearInterval(timer); timer = null; }
    }

    btnNext.addEventListener('click', () => { stopPlay(); next(); });
    btnPrev.addEventListener('click', () => { stopPlay(); prev(); });
    btnReset.addEventListener('click', reset);
    btnPlay.addEventListener('click', () => { playing ? stopPlay() : startPlay(); });

    render();
  }

  /* =====================================================================
   *  AUTO-INIT — find all .dsa-viz elements and initialize them
   * ===================================================================== */
  function initAll() {
    var els = document.querySelectorAll('.dsa-viz');
    console.log('[DSA-Viz] Found', els.length, 'visualization widgets');
    els.forEach(function(el, i) {
      console.log('[DSA-Viz] Initializing widget', i);
      initViz(el);
    });
  }

  // Run after DOM is ready — use multiple strategies for reliability
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(initAll, 0);
  } else {
    document.addEventListener('DOMContentLoaded', initAll);
  }
  // Fallback: also try on window load
  window.addEventListener('load', function() {
    var remaining = document.querySelectorAll('.dsa-viz:not([data-initialized])');
    if (remaining.length > 0) {
      console.log('[DSA-Viz] Window load fallback: found', remaining.length, 'uninitialized');
      remaining.forEach(function(el) {
        el.setAttribute('data-initialized', 'true');
        initViz(el);
      });
    }
  });
})();
