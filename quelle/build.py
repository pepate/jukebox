"""Baut aus jukebox.src.html + assets eine einzige, offline lauffähige HTML-Datei."""
import base64, pathlib

ROOT = pathlib.Path(__file__).parent
b64 = lambda p: base64.b64encode((ROOT / p).read_bytes()).decode()

FONTS = [  # (Familie, Datei, Gewichtsbereich) – Oswald/Raleway sind variable Fonts
    ('Oswald', 'Oswald-500.woff2', '200 700'),
    ('Raleway', 'Raleway-500.woff2', '100 900'),
    ('Yellowtail', 'Yellowtail-400.woff2', '400'),
]
css = '\n'.join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};font-display:block;"
    f"src:url(data:font/woff2;base64,{b64('assets/fonts/' + f)}) format('woff2')}}"
    for fam, f, w in FONTS)

html = (ROOT / 'jukebox.src.html').read_text(encoding='utf-8')
html = html.replace('/*FONTS*/', css).replace('__LOGO__', 'data:image/png;base64,' + b64('assets/logo.png'))
out = ROOT.parent / 'Jukebox.html'
out.write_text(html, encoding='utf-8')
print(out, len(html) // 1024, 'KB')
