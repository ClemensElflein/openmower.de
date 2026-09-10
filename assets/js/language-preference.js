(function () {
    'use strict';

    var settings = document.currentScript.dataset;
    var targets = JSON.parse(settings.languageTargets);
    var current = new URL(window.location.href);
    var storageKey = 'openmower.language';
    var explicit = current.searchParams.get('lang');
    var preferred;

    function supported(language) {
        return language === 'de' || language === 'en';
    }

    // The query parameter also handles opening a language-menu link in a new tab.
    if (supported(explicit)) {
        preferred = explicit;
        current.searchParams.delete('lang');
        window.history.replaceState(window.history.state, '', current.href);
    }

    try {
        var saved = window.localStorage.getItem(storageKey);
        if (!preferred && supported(saved)) preferred = saved;
        if (!preferred) {
            var languages = navigator.languages && navigator.languages.length
                ? navigator.languages : [navigator.language || 'en'];
            for (var i = 0; i < languages.length; i++) {
                var language = languages[i].toLowerCase().split('-')[0];
                if (supported(language)) {
                    preferred = language;
                    break;
                }
            }
            preferred = preferred || 'en';
        }
        window.localStorage.setItem(storageKey, preferred);
    } catch (error) {
        // Without storage, keep normal links usable instead of undoing a manual choice.
        return;
    }

    // Missing translations must leave visitors on the requested page.
    if (preferred === settings.pageLanguage || !targets[preferred]) return;

    var target = new URL(targets[preferred], current);
    if (target.origin !== current.origin || target.pathname === current.pathname) return;
    target.search = current.search;
    target.hash = current.hash;
    window.location.replace(target.href);
})();
