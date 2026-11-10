{{ $needmermaid := .Site.Params.mermaid.enable -}}
{{ if ge hugo.Version "0.93.0" -}}
    {{ $needmermaid = or $needmermaid (.Page.Store.Get "hasmermaid") -}}
{{ end }}

{{ if $needmermaid }}
(function($) {
    var needMermaid = false;

{{ if ge hugo.Version "0.93.0" -}}
    if ($('.mermaid').length > 0) {
        needMermaid = true;
    };
{{ else -}}
    $('.language-mermaid').parent().replaceWith(function() {
        needMermaid = true;
        return $('<pre class="mermaid">').text($(this).text());
    });
{{ end -}}

    if (!needMermaid)  {
        mermaid.initialize({startOnLoad: false});
        return;
    }

    // Docsy 0.5.1 serialises the page here (a jsonify of the page object) to pick up
    // site-wide Mermaid defaults. On Hugo >= 0.111 that overflows the stack, because
    // Page now carries circular references - the build dies with "fatal error: stack
    // overflow". We do not use site-wide defaults anyway (a diagram configures itself
    // with an init directive), so an empty object keeps this working on both versions.
    // NOTE: this file is a Hugo template, so do not write template delimiters here.
    var params = {};

    // site params are stored with lowercase keys; lookup correct casing
    // from Mermaid default config.
    var norm = function(defaultConfig, params) {
        var result = {};
        for (const key in defaultConfig) {
            const keyLower = key.toLowerCase();
            if (defaultConfig.hasOwnProperty(key) && params.hasOwnProperty(keyLower)) {
                if (typeof defaultConfig[key] === "object") {
                    result[key] = norm(defaultConfig[key], params[keyLower]);
                } else {
                    result[key] = params[keyLower];
                }
            }
        }
        return result;
    };
    var settings = norm((mermaid.mermaidAPI || mermaid).defaultConfig, params);
    settings.startOnLoad = true;
    mermaid.initialize(settings);
})(jQuery);
{{ end }}
