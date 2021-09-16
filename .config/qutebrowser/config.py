config.load_autoconfig()

c.tabs.background = True
c.new_instance_open_target = 'window'
c.downloads.position = 'bottom'
# c.spellcheck.languages = ['en-US', 'es-ES', 'pt-BR']

# Bindings for normal mode
config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('Z', 'hint links spawn st -e youtube-dl {hint-url}')
config.bind('t', 'set-cmd-text -s :open -t')
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')
config.bind(',ce', 'config-edit')
config.bind(',p', 'config-cycle -p content.plugins ;; reload')

config.bind(',rta', 'open {url}top/?sort=top&t=all')
config.bind(',rtv', 'spawn termite -e "rtv {url}"')
config.bind(',c', 'spawn -d chromium {url}')

css = '~/proj/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css'
config.bind(',n', f'config-cycle content.user_stylesheets {css} ""')

c.url.searchengines['rfc'] = 'https://tools.ietf.org/html/rfc{}'
c.url.searchengines['pypi'] = 'https://pypi.org/project/{}/'
c.url.searchengines['qtbug'] = 'https://bugreports.qt.io/browse/QTBUG-{}'
c.url.searchengines['qb'] = 'https://github.com/The-Compiler/qutebrowser/issues/{}'
c.url.searchengines['btc'] = 'https://www.blockchain.com/btc/address/{}'
c.url.searchengines['http'] = 'https://httpstatuses.com/{}'
c.url.searchengines['duden'] = 'https://www.duden.de/suchen/dudenonline/{}'
c.url.searchengines['dictcc'] = 'https://www.dict.cc/?s={}'
#c.url.searchengines['maps'] = 'https://www.google.com/maps?q=%s'

# c.fonts.tabs = '12pt IBM Plex Mono'
# c.fonts.statusbar = '12pt IBM Plex Mono'
c.fonts.web.family.fantasy = 'IBM Plex Mono'

c.search.incremental = False

#c.qt.args = ['ppapi-widevine-path=/usr/lib/qt/plugins/ppapi/libwidevinecdmadapter.so']

c.content.javascript.enabled = True
config.source('gruvbox.py')
