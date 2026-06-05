/* =============================================================
   Luca Healthcare — custom animated lung centerpiece (Canvas)
   Hand-coded: procedural bronchial tree, airflow particles,
   drifting particle field, pulsing node network, breathing.
   ============================================================= */
(function () {
  'use strict';
  var canvas = document.getElementById('lungCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Design space is 400x400; we scale to the real pixel size.
  var BASE = 400, S = 1, DPR = 1, W = 400, H = 400;

  function resize() {
    var rect = canvas.getBoundingClientRect();
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    W = Math.max(1, rect.width); H = Math.max(1, rect.height);
    canvas.width = W * DPR; canvas.height = H * DPR;
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    S = Math.min(W, H) / BASE;            // uniform scale from design space
  }

  // ---- map a design-space point (cx 200 center) to canvas px ----
  function px(x) { return W / 2 + (x - 200) * S; }
  function py(y) { return H / 2 + (y - 200) * S; }

  // ============================================================
  // Procedural bronchial tree — returns array of segments
  // each: {x1,y1,x2,y2,depth,len}
  // ============================================================
  function buildTree(rootX, rootY, ang, len, depth, dir, segs) {
    if (depth <= 0 || len < 5) return;
    var x2 = rootX + Math.cos(ang) * len;
    var y2 = rootY + Math.sin(ang) * len;
    segs.push({ x1: rootX, y1: rootY, x2: x2, y2: y2, depth: depth });
    var spread = 0.42 + Math.random() * 0.16;
    var f = 0.72;
    // main continues, plus a branch toward the lung body (dir = -1 left, +1 right)
    buildTree(x2, y2, ang + spread * dir, len * f, depth - 1, dir, segs);
    buildTree(x2, y2, ang - spread * 0.5 * dir, len * f * 0.92, depth - 1, dir, segs);
    if (depth > 2 && Math.random() > 0.4) {
      buildTree(x2, y2, ang + spread * 1.5 * dir, len * f * 0.7, depth - 2, dir, segs);
    }
  }

  // Lung lobe outline (design space) as bezier path commands
  function leftLobePath(p) {
    p.moveTo(px(186), py(112));
    p.bezierCurveTo(px(150), py(116), px(96), py(140), px(80), py(186));
    p.bezierCurveTo(px(66), py(226), px(74), py(280), px(104), py(300));
    p.bezierCurveTo(px(128), py(316), px(166), py(308), px(178), py(280));
    p.bezierCurveTo(px(190), py(250), px(188), py(150), px(186), py(112));
    p.closePath();
  }
  function rightLobePath(p) {
    p.moveTo(px(214), py(112));
    p.bezierCurveTo(px(250), py(116), px(304), py(140), px(320), py(186));
    p.bezierCurveTo(px(334), py(226), px(326), py(280), px(296), py(300));
    p.bezierCurveTo(px(272), py(316), px(234), py(308), px(222), py(280));
    p.bezierCurveTo(px(210), py(250), px(212), py(150), px(214), py(112));
    p.closePath();
  }

  // ============================================================
  // Build static structure (rebuilt on resize for crisp trees)
  // ============================================================
  var leftSegs, rightSegs, allSegs, flow, field, nodes, links, pulses;

  function seed() {
    leftSegs = []; rightSegs = [];
    // trachea splits at ~ (200,150) into two bronchi
    buildTree(190, 152, Math.PI * 0.62, 30, 6, -1, leftSegs);   // into left lobe
    buildTree(210, 152, Math.PI * 0.38, 30, 6, 1, rightSegs);   // into right lobe
    allSegs = leftSegs.concat(rightSegs);

    // airflow particles ride random segments
    flow = [];
    var n = reduce ? 0 : 90;
    for (var i = 0; i < n; i++) flow.push(makeFlow());

    // ambient particle field (denser to the right => "dissolving" side)
    field = [];
    var m = reduce ? 40 : 150;
    for (var j = 0; j < m; j++) {
      var rightBias = Math.random() < 0.62;
      var cx = rightBias ? 230 + Math.random() * 130 : 40 + Math.random() * 320;
      var cy = 90 + Math.random() * 230;
      field.push({
        x: cx, y: cy, r: 0.6 + Math.random() * 1.8,
        vx: (Math.random() - 0.5) * 0.18 + (rightBias ? 0.12 : 0),
        vy: (Math.random() - 0.5) * 0.18 - 0.05,
        a: 0.15 + Math.random() * 0.5,
        tw: Math.random() * Math.PI * 2,
        c: Math.random() < 0.5 ? '0,158,223' : (Math.random() < 0.5 ? '43,224,200' : '140,91,246')
      });
    }

    // orbiting node network (design-space, around center)
    nodes = [];
    var nodeDefs = [
      [150, 130], [250, 130], [286, 210], [262, 286],
      [138, 286], [108, 200], [200, 104]
    ];
    for (var k = 0; k < nodeDefs.length; k++) {
      nodes.push({
        bx: nodeDefs[k][0], by: nodeDefs[k][1],
        phase: Math.random() * Math.PI * 2,
        rad: 1 + Math.random() * 4,
        c: k % 3 === 0 ? '140,91,246' : (k % 3 === 1 ? '0,158,223' : '255,157,182')
      });
    }
    links = [[6,0],[6,1],[6,3],[6,4],[0,1],[4,3],[1,2],[5,4]];
    pulses = links.map(function (lk, idx) {
      return { lk: lk, t: Math.random(), spd: 0.004 + Math.random() * 0.006, on: idx % 2 === 0 };
    });
  }

  function makeFlow() {
    var seg = allSegs[(Math.random() * allSegs.length) | 0];
    return { seg: seg, t: Math.random(), spd: 0.006 + Math.random() * 0.014, r: 0.7 + Math.random() * 1.3 };
  }

  // ============================================================
  // Render loop
  // ============================================================
  var t0 = performance.now();
  function frame(now) {
    var time = (now - t0) / 1000;
    var breath = 0.5 + 0.5 * Math.sin(time * (Math.PI * 2) / 6); // 6s cycle 0..1
    var scaleB = 0.985 + breath * 0.03;
    var inhale = Math.cos(time * (Math.PI * 2) / 6);            // +1 inhale, -1 exhale

    ctx.clearRect(0, 0, W, H);

    // breathing transform around center
    ctx.save();
    ctx.translate(W / 2, H / 2);
    ctx.scale(scaleB, scaleB);
    ctx.translate(-W / 2, -H / 2);

    // ---- ambient particle field (behind) ----
    for (var i = 0; i < field.length; i++) {
      var p = field[i];
      p.x += p.vx; p.y += p.vy; p.tw += 0.05;
      if (p.x > 380) p.x = 220; if (p.x < 30) p.x = 60;
      if (p.y < 80) p.y = 320; if (p.y > 330) p.y = 90;
      var tw = 0.5 + 0.5 * Math.sin(p.tw);
      ctx.beginPath();
      ctx.arc(px(p.x), py(p.y), p.r * S, 0, 6.283);
      ctx.fillStyle = 'rgba(' + p.c + ',' + (p.a * tw).toFixed(3) + ')';
      ctx.fill();
    }

    // ---- lung lobe fills (soft translucent) ----
    var grL = ctx.createLinearGradient(px(80), py(112), px(190), py(310));
    grL.addColorStop(0, 'rgba(255,170,190,0.30)');
    grL.addColorStop(1, 'rgba(140,91,246,0.16)');
    var grR = ctx.createLinearGradient(px(320), py(112), px(210), py(310));
    grR.addColorStop(0, 'rgba(255,180,160,0.30)');
    grR.addColorStop(1, 'rgba(0,158,223,0.16)');

    var pL = new Path2D(); leftLobePath(pL);
    var pR = new Path2D(); rightLobePath(pR);
    ctx.fillStyle = grL; ctx.fill(pL);
    ctx.fillStyle = grR; ctx.fill(pR);
    ctx.lineWidth = 1.8 * S;
    ctx.strokeStyle = 'rgba(0,158,223,0.6)'; ctx.stroke(pL);
    ctx.strokeStyle = 'rgba(140,91,246,0.55)'; ctx.stroke(pR);

    // ---- bronchial tree + airflow, CLIPPED inside the lobes ----
    ctx.lineCap = 'round';
    drawTreeInside(pL, leftSegs);
    drawTreeInside(pR, rightSegs);

    // trachea (drawn over, not clipped)
    ctx.beginPath();
    ctx.moveTo(px(200), py(96)); ctx.lineTo(px(200), py(150));
    ctx.lineWidth = 5 * S; ctx.strokeStyle = 'rgba(0,158,223,0.7)'; ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(px(200), py(150)); ctx.lineTo(px(190), py(152));
    ctx.moveTo(px(200), py(150)); ctx.lineTo(px(210), py(152));
    ctx.lineWidth = 4 * S; ctx.stroke();

    function drawTreeInside(clipPath, segs) {
      ctx.save();
      ctx.clip(clipPath);
      var i, g;
      for (i = 0; i < segs.length; i++) {
        g = segs[i];
        ctx.beginPath();
        ctx.moveTo(px(g.x1), py(g.y1));
        ctx.lineTo(px(g.x2), py(g.y2));
        ctx.lineWidth = Math.max(0.6, g.depth * 0.7) * S;
        ctx.strokeStyle = 'rgba(0,158,223,' + (0.18 + g.depth * 0.06).toFixed(2) + ')';
        ctx.stroke();
      }
      // airflow particles for this lobe's segments
      for (i = 0; i < flow.length; i++) {
        var fp = flow[i];
        if (segs.indexOf(fp.seg) === -1) continue;
        var sg = fp.seg;
        var x = sg.x1 + (sg.x2 - sg.x1) * fp.t;
        var y = sg.y1 + (sg.y2 - sg.y1) * fp.t;
        ctx.beginPath();
        ctx.arc(px(x), py(y), fp.r * S, 0, 6.283);
        ctx.fillStyle = 'rgba(120,220,255,0.95)';
        ctx.shadowColor = 'rgba(0,200,255,0.9)'; ctx.shadowBlur = 6 * S;
        ctx.fill();
        ctx.shadowBlur = 0;
      }
      ctx.restore();
    }

    // advance airflow particles
    for (var f = 0; f < flow.length; f++) {
      var afp = flow[f];
      afp.t += afp.spd * (0.4 + 0.6 * Math.abs(inhale)) * (inhale >= 0 ? 1 : -1);
      if (afp.t > 1 || afp.t < 0) flow[f] = makeFlow();
    }

    // ---- node network (gentle orbit) ----
    function nodePos(nd) {
      return {
        x: nd.bx + Math.sin(time * 0.5 + nd.phase) * 6,
        y: nd.by + Math.cos(time * 0.4 + nd.phase) * 6
      };
    }
    // links
    for (var l = 0; l < links.length; l++) {
      var a = nodePos(nodes[links[l][0]]), b = nodePos(nodes[links[l][1]]);
      var pulse = 0.12 + 0.18 * (0.5 + 0.5 * Math.sin(time * 1.5 + l));
      ctx.beginPath();
      ctx.moveTo(px(a.x), py(a.y)); ctx.lineTo(px(b.x), py(b.y));
      ctx.lineWidth = 0.8 * S;
      ctx.strokeStyle = 'rgba(0,150,220,' + pulse.toFixed(2) + ')';
      ctx.stroke();
    }
    // travelling pulses along links
    for (var pz = 0; pz < pulses.length; pz++) {
      var pu = pulses[pz]; pu.t += pu.spd; if (pu.t > 1) pu.t = 0;
      var na = nodePos(nodes[pu.lk[0]]), nb = nodePos(nodes[pu.lk[1]]);
      var x = na.x + (nb.x - na.x) * pu.t, y = na.y + (nb.y - na.y) * pu.t;
      ctx.beginPath();
      ctx.arc(px(x), py(y), 1.8 * S, 0, 6.283);
      ctx.fillStyle = 'rgba(255,255,255,0.95)';
      ctx.shadowColor = 'rgba(120,220,255,1)'; ctx.shadowBlur = 6 * S;
      ctx.fill(); ctx.shadowBlur = 0;
    }
    // nodes
    for (var nn = 0; nn < nodes.length; nn++) {
      var nd = nodes[nn], pos = nodePos(nd);
      var pr = (nd.rad + Math.sin(time * 2 + nd.phase) * 1.2) * S;
      ctx.beginPath();
      ctx.arc(px(pos.x), py(pos.y), Math.max(1, pr), 0, 6.283);
      ctx.fillStyle = 'rgba(' + nd.c + ',0.95)';
      ctx.shadowColor = 'rgba(' + nd.c + ',0.9)'; ctx.shadowBlur = 8 * S;
      ctx.fill(); ctx.shadowBlur = 0;
    }

    ctx.restore();

    if (!reduce) requestAnimationFrame(frame);
  }

  // ---- init ----
  function init() { resize(); seed(); requestAnimationFrame(frame); }
  init();
  var rt;
  window.addEventListener('resize', function () {
    clearTimeout(rt);
    rt = setTimeout(function () { resize(); seed(); if (reduce) requestAnimationFrame(frame); }, 200);
  });
})();
