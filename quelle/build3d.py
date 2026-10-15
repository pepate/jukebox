"""Baut jukebox3d.src.html zu einer einzigen offline-fähigen Datei (three.js + Addons als data:-Module per Importmap)."""
import base64, json, pathlib, posixpath, re

ROOT = pathlib.Path(__file__).parent
THREE = ROOT / 'assets/three'
b64 = lambda data: base64.b64encode(data).decode()

# Addon-Module einsammeln, relative Imports auf Importmap-Namen umschreiben
modules, todo = {}, ['environments/RoomEnvironment.js', 'geometries/RoundedBoxGeometry.js',
                     'postprocessing/EffectComposer.js', 'postprocessing/RenderPass.js',
                     'postprocessing/UnrealBloomPass.js', 'postprocessing/OutputPass.js']
while todo:
    rel = todo.pop()
    if rel in modules:
        continue
    src = (THREE / rel).read_text(encoding='utf-8')
    def repl(m):
        dep = posixpath.normpath(posixpath.join(posixpath.dirname(rel), m.group(2)))
        todo.append(dep)
        return f"{m.group(1)}'three/addons/{dep}'"
    modules[rel] = re.sub(r"""(from\s*)['"](\.{1,2}/[^'"]+)['"]""", repl, src)

imports = {'three': 'data:text/javascript;base64,' + b64((THREE / 'three.module.min.js').read_bytes())}
for rel, src in modules.items():
    imports[f'three/addons/{rel}'] = 'data:text/javascript;base64,' + b64(src.encode())
importmap = '<script type="importmap">' + json.dumps({'imports': imports}) + '</script>'

FONTS = [('Oswald', 'Oswald-500.woff2', '200 700'), ('Raleway', 'Raleway-500.woff2', '100 900'), ('Yellowtail', 'Yellowtail-400.woff2', '400')]
css = '\n'.join(f"@font-face{{font-family:'{fam}';font-weight:{w};font-display:block;"
                f"src:url(data:font/woff2;base64,{b64((ROOT / 'assets/fonts' / f).read_bytes())}) format('woff2')}}" for fam, f, w in FONTS)

html = (ROOT / 'jukebox3d.src.html').read_text(encoding='utf-8')
html = (html.replace('<!--IMPORTMAP-->', importmap).replace('/*FONTS*/', css)
            .replace('__LOGO__', 'data:image/png;base64,' + b64((ROOT / 'assets/logo.png').read_bytes())))
out = ROOT.parent / 'Jukebox3D.html'
out.write_text(html, encoding='utf-8')
print(out, len(html) // 1024, 'KB,', len(modules), 'Addon-Module')
