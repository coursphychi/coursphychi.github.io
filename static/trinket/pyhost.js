/* =====================================================================
   pyhost.js — UNE instance Pyodide partagée par toutes les fenêtres
   runpython lang="pyodide" d'une même page.

   Injecté dans la PAGE (et non dans les iframes) par player.html : l'instance
   doit vivre dans un document qui ne se recharge pas. Une iframe rechargée
   (bouton ■) rendrait inutilisables les objets créés dans son propre document.

   • get()     : démarre Pyodide une seule fois ; les fenêtres suivantes
                 réutilisent l'instance et les bibliothèques déjà installées.
   • acquire() : une seule exécution à la fois (les sorties print, figures,
                 input() vont à la fenêtre qui détient le tour) ; un tour
                 détenu par une fenêtre disparue ou rechargée est libéré.
   • release() : rend le tour.
   Les fonctions passées à Pyodide sont créées ICI (dans la page) et
   relaient vers la fenêtre courante : elles survivent aux iframes.
===================================================================== */
(function () {
  if (window.__tkPyHost) return;

  var S = {
    loading: null,   // promesse de l'instance
    ready: false,    // instance démarrée ?
    mpl: false,      // matplotlib configuré ?
    owner: null,     // jeton de la fenêtre qui détient le tour
    cur: null        // ses relais { out(bytes, isErr), stdin(), image(b64) }
  };

  // Une fenêtre est vivante si une iframe de la page porte encore son jeton
  // (un rechargement de l'iframe crée un nouveau jeton).
  function alive(token) {
    if (!token) return false;
    if (window.__tkToken === token) return true;           // mode local (sans page hôte)
    var fr = document.getElementsByTagName("iframe");
    for (var i = 0; i < fr.length; i++) {
      try { if (fr[i].contentWindow && fr[i].contentWindow.__tkToken === token) return true; }
      catch (e) {}
    }
    return false;
  }
  function relay(name) {
    return function () {
      var c = S.cur;
      if (!c || !c[name]) return name === "stdin" ? null : undefined;
      try { return c[name].apply(null, arguments); }
      catch (e) { return name === "stdin" ? null : undefined; }   // fenêtre disparue
    };
  }

  window.__tkPyHost = {
    state: S,

    get: function (indexURL, bootCode) {
      if (S.loading) return S.loading;
      S.loading = new Promise(function (res, rej) {
        if (window.loadPyodide) return res();
        var s = document.createElement("script");
        s.src = indexURL + "pyodide.js";
        s.onload = function () { res(); };
        s.onerror = function () { rej(new Error("pyodide.js")); };
        document.head.appendChild(s);
      }).then(function () {
        return window.loadPyodide({ indexURL: indexURL });
      }).then(function (py) {
        var out = relay("out"), stdin = relay("stdin"), image = relay("image");
        py.setStdout({ write: function (b) { out(b, false); return b.length; } });
        py.setStderr({ write: function (b) { out(b, true);  return b.length; } });
        py.setStdin({ stdin: function () { return stdin(); } });
        py.registerJsModule("tkbridge", { image: function (b64) { image(b64); } });
        return py.runPythonAsync(bootCode).then(function () { S.ready = true; return py; });
      });
      S.loading.catch(function () { S.loading = null; });   // nouvel essai possible
      return S.loading;
    },

    acquire: function (token, handlers, onWait) {
      return new Promise(function (res) {
        var waited = false;
        (function attempt() {
          if (!S.owner || S.owner === token || !alive(S.owner)) {
            S.owner = token; S.cur = handlers; res();
          } else {
            if (!waited && onWait) { waited = true; try { onWait(); } catch (e) {} }
            setTimeout(attempt, 60);
          }
        })();
      });
    },

    release: function (token) {
      if (S.owner === token) { S.owner = null; S.cur = null; }
    }
  };
})();
