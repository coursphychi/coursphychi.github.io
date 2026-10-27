/* ==================================================================
   cours.js — scripts communs des pages de cours
   À placer dans : static/js/cours.js
   Chargé dans chaque page par : <script src="/js/cours.js" defer></script>
   ================================================================== */
(function () {
  'use strict';
  /* ---------------- Mode révision ---------------- */
  (function () {
    var btn = document.querySelector('.nt-quiz-toggle');
    if (!btn) { return; }
    var holes = Array.prototype.slice.call(document.querySelectorAll('.nt-hole'));
    function reveal(h) { if (document.body.classList.contains('nt-quiz')) { h.classList.toggle('nt-shown'); } }
    holes.forEach(function (h) {
      h.addEventListener('click', function () { reveal(h); });
      h.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); reveal(h); }
      });
    });
    btn.addEventListener('click', function () {
      var on = document.body.classList.toggle('nt-quiz');
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      holes.forEach(function (h) {
        h.classList.remove('nt-shown');
        if (on) { h.setAttribute('tabindex', '0'); h.setAttribute('role', 'button'); }
        else { h.removeAttribute('tabindex'); h.removeAttribute('role'); }
      });
    });
  })();

  /* ---------------- Bilan des quiz ----------------
     Quand un quiz affiche son bilan (score dans .nt-big-score), on ne montre plus que lui :
     les réponses de la dernière question sont masquées, le bilan est centré et précédé d'un emoji
     adapté au score. Fonctionne pour tous les moteurs de quiz des pages, sans les modifier. */
  (function () {
    function emoji(r) { return r >= 1 ? '\uD83C\uDFC6' : (r >= 0.75 ? '\uD83C\uDF89' : (r >= 0.5 ? '\uD83D\uDC4D' : '\uD83D\uDCDA')); }   /* 🏆 🎉 👍 📚 */
    function maj() {
      Array.prototype.forEach.call(document.querySelectorAll('.nt-quizlab, .nt-lab'), function (lab) {
        var sc = lab.querySelector('.nt-big-score');
        if (!sc) { lab.classList.remove('nt-bilan'); return; }
        lab.classList.add('nt-bilan');
        if (sc.getAttribute('data-emoji')) { return; }
        var m = (sc.textContent || '').match(/(\d+)\s*\/\s*(\d+)/);
        if (!m) { return; }
        var e = document.createElement('span'); e.className = 'nt-bilan-emoji'; e.setAttribute('aria-hidden', 'true'); e.textContent = emoji(+m[1] / Math.max(1, +m[2]));
        sc.parentNode.insertBefore(e, sc); sc.setAttribute('data-emoji', '1');
      });
    }
    var attente = null;
    new MutationObserver(function () { if (!attente) { attente = setTimeout(function () { attente = null; maj(); }, 30); } }).observe(document.body, { childList: true, subtree: true });
    maj();
  })();

})();
