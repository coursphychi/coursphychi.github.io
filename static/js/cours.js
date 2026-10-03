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

})();
