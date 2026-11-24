"""Genera los SVG animados del perfil de GitHub de BlueSmile Technology.

Uso: python3 scripts/generar_assets.py   (escribe en assets/)
"""
import os
import sys

import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, "assets")
# Logo oficial en blanco (de bluesmile-it.com/marca/logo-blanco.svg), incrustado en la cabecera
LOGO = re.search(r'href="(data:image/png;base64,[^"]+)"', open(os.path.join(ROOT, "assets", "logo-blanco.svg")).read()).group(1)

SANS = "'Segoe UI',-apple-system,BlinkMacSystemFont,Helvetica,Arial,'DejaVu Sans',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono','DejaVu Sans Mono',monospace"

NAVY_DEEP = "#06122b"
NAVY = "#0b1d40"
NAVY_2 = "#13295a"
LINE = "#1e3566"
BLUE = "#1f4bff"
BLUE_SOFT = "#9db8ff"
MINT = "#2fd49a"
CYAN = "#0a9cc8"
TEXT = "#e8edf5"
MUTED = "#b9c2d3"

REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


def write(name, svg):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{name}: {len(svg.encode()) / 1024:.1f} KB")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------------------
# 1. Cabecera
# ---------------------------------------------------------------------------
def header():
    W, H = 1280, 400
    nodes = [
        (60, 70), (150, 40), (230, 110), (110, 170), (40, 260), (190, 250), (280, 330), (90, 350),
        (1220, 60), (1130, 120), (1240, 190), (1060, 60), (1160, 260), (1050, 220), (1230, 340), (1100, 350),
    ]
    edges = [
        (0, 1), (1, 2), (0, 3), (2, 3), (3, 4), (3, 5), (5, 6), (4, 7), (6, 7), (2, 5),
        (8, 9), (9, 11), (8, 10), (9, 10), (10, 12), (9, 13), (12, 13), (12, 14), (14, 15), (13, 15),
    ]
    lines = []
    for i, (a, b) in enumerate(edges):
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        lines.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="edge"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="pkt" style="animation-delay:-{(i * 0.7) % 4:.1f}s"/>'
        )
    dots = []
    for i, (x, y) in enumerate(nodes):
        dots.append(
            f'<circle cx="{x}" cy="{y}" r="9" class="ring" style="animation-delay:-{(i * 0.45) % 3:.2f}s"/>'
            f'<circle cx="{x}" cy="{y}" r="3.2" class="node"/>'
        )

    # Logo: 2116 x 411 (viewBox del logo oficial en blanco)
    lw = 600
    lh = round(lw * 411 / 2116)
    lx = (W - lw) / 2
    ly = 62

    chips = [("Consultora TI · Chile y LATAM", 300), ("11 años de trayectoria", 240), ("ISO 9001 · 14001 · 45001", 270)]
    gap = 18
    total = sum(w for _, w in chips) + gap * (len(chips) - 1)
    x = (W - total) / 2
    chip_svg = []
    for i, (label, w) in enumerate(chips):
        chip_svg.append(
            f'<g class="fade" style="animation-delay:{0.9 + i * 0.15:.2f}s">'
            f'<rect x="{x}" y="318" width="{w}" height="38" rx="19" class="chip"/>'
            f'<circle cx="{x + 22}" cy="337" r="4" fill="{MINT}"/>'
            f'<text x="{x + w / 2 + 8}" y="342.5" text-anchor="middle" class="chipt">{esc(label)}</text></g>'
        )
        x += w + gap

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">BlueSmile Technology</title>
<desc id="d">Consultora TI en Chile: modernizamos la tecnología que mueve tu empresa.</desc>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{NAVY_DEEP}"/><stop offset=".55" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY_2}"/></linearGradient>
  <radialGradient id="o1"><stop offset="0" stop-color="{BLUE}" stop-opacity=".55"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
  <radialGradient id="o2"><stop offset="0" stop-color="{MINT}" stop-opacity=".30"/><stop offset="1" stop-color="{MINT}" stop-opacity="0"/></radialGradient>
  <radialGradient id="o3"><stop offset="0" stop-color="{CYAN}" stop-opacity=".40"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
  <linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset=".5" stop-color="{MINT}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>
  <linearGradient id="shine" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <linearGradient id="tag" x1="0" x2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#dfe8ff"/><stop offset="1" stop-color="#ffffff"/></linearGradient>
  <pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="{BLUE_SOFT}" fill-opacity=".13"/></pattern>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<style>
  text{{font-family:{SANS}}}
  .tagline{{font-size:38px;font-weight:700;letter-spacing:-.3px}}
  .sub{{font-size:20px;fill:{BLUE_SOFT};letter-spacing:.2px}}
  .sub .sep{{fill:{MINT}}}
  .chip{{fill:#ffffff;fill-opacity:.06;stroke:#ffffff;stroke-opacity:.16}}
  .chipt{{font-size:15px;fill:{TEXT};font-weight:600}}
  .edge{{stroke:{BLUE_SOFT};stroke-opacity:.16;stroke-width:1}}
  .pkt{{stroke:{MINT};stroke-width:2;stroke-linecap:round;stroke-dasharray:6 400;animation:pkt 4s linear infinite;opacity:.8}}
  .node{{fill:{MINT}}}
  .ring{{fill:none;stroke:{MINT};stroke-width:1.5;transform-box:fill-box;transform-origin:center;animation:ring 3s ease-out infinite;opacity:0}}
  .orb1{{animation:d1 16s ease-in-out infinite alternate}}
  .orb2{{animation:d2 19s ease-in-out infinite alternate}}
  .orb3{{animation:d3 13s ease-in-out infinite alternate}}
  .shine{{animation:shine 5s ease-in-out infinite}}
  .fade{{animation:up .9s cubic-bezier(.2,.8,.2,1) backwards}}
  .logo{{animation:logo 1.1s cubic-bezier(.2,.8,.2,1) backwards}}
  @keyframes pkt{{from{{stroke-dashoffset:406}}to{{stroke-dashoffset:0}}}}
  @keyframes ring{{0%{{transform:scale(.3);opacity:.9}}100%{{transform:scale(2.2);opacity:0}}}}
  @keyframes d1{{to{{transform:translate(160px,60px)}}}}
  @keyframes d2{{to{{transform:translate(-180px,-40px)}}}}
  @keyframes d3{{to{{transform:translate(90px,-70px)}}}}
  @keyframes shine{{0%{{transform:translateX(-300px)}}60%,100%{{transform:translateX(1300px)}}}}
  @keyframes up{{from{{opacity:0;transform:translateY(14px)}}}}
  @keyframes logo{{from{{opacity:0;transform:translateY(-10px) scale(.98)}}}}
  {REDUCED}
</style>
<g clip-path="url(#frame)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <circle class="orb1" cx="250" cy="120" r="360" fill="url(#o1)"/>
  <circle class="orb2" cx="1060" cy="320" r="340" fill="url(#o2)"/>
  <circle class="orb3" cx="760" cy="-40" r="300" fill="url(#o3)"/>
  <rect width="{W}" height="{H}" fill="url(#dots)"/>
  <g>{''.join(lines)}</g>
  <g>{''.join(dots)}</g>
  <svg class="logo" x="{lx}" y="{ly}" width="{lw}" height="{lh}" viewBox="67 185 2116 411"><image width="2250" height="780" href="{LOGO}"/></svg>
  <text class="tagline fade" x="{W / 2}" y="242" text-anchor="middle" fill="url(#tag)" style="animation-delay:.35s">Modernizamos la tecnología que mueve tu empresa</text>
  <text class="sub fade" x="{W / 2}" y="285" text-anchor="middle" style="animation-delay:.6s">Automatización <tspan class="sep">·</tspan> Nube <tspan class="sep">·</tspan> Datos <tspan class="sep">·</tspan> Desarrollo de software <tspan class="sep">·</tspan> Inteligencia artificial</text>
  {''.join(chip_svg)}
  <rect y="{H - 5}" width="{W}" height="5" fill="url(#bar)"/>
  <rect class="shine" y="{H - 5}" width="260" height="5" fill="url(#shine)"/>
</g>
</svg>
"""


# ---------------------------------------------------------------------------
# 2. Terminal animada (como el hero de bluesmile-it.com)
# ---------------------------------------------------------------------------
def terminal():
    W = 900
    FS = 19
    CW = FS * 0.6  # ancho de carácter monoespaciado
    LH = 28
    X0 = 34
    TOP = 92
    DUR = 16.0

    services = [
        "Business Intelligence", "Servicios de Datos", "Infraestructura On-Premise",
        "Servicios Cloud", "Desarrollo de Software", "Soporte TI",
        "Integración IT/OT", "Inteligencia Artificial", "Automatización",
    ]
    cmd = "bluesmile servicios --listar"
    n_lines = 1 + len(services) + 1 + 1  # comando, servicios, resumen, prompt
    H = TOP + LH * (n_lines - 1) + 30

    def kt(t):
        return f"{t / DUR:.4f}"

    def show(t_in, t_out=15.3, fade=0.25):
        """Animación SMIL de opacidad: aparece en t_in y desaparece al final del ciclo."""
        return (
            f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" '
            f'values="0;0;1;1;0;0" keyTimes="0;{kt(t_in)};{kt(t_in + fade)};{kt(t_out)};{kt(t_out + 0.4)};1"/>'
        )

    def prompt(y):
        parts = [("bluesmile@latam", MINT, 15), (":", TEXT, 1), ("~", BLUE_SOFT, 1), ("$", TEXT, 1)]
        out, x = [], X0
        for txt, col, n in parts:
            out.append(f'<text x="{x:.1f}" y="{y}" fill="{col}" textLength="{n * CW:.1f}" lengthAdjust="spacingAndGlyphs">{esc(txt)}</text>')
            x += n * CW
        return "".join(out), X0 + 19 * CW  # 15 + 1 + 1 + 1 + espacio

    # Línea 1: comando tecleado
    y = TOP
    p1, cx = prompt(y)
    t0, t1 = 0.6, 2.6
    n = len(cmd)
    widths = ";".join(f"{k * CW:.1f}" for k in range(n + 1))
    times = ";".join(f"{(t0 + (t1 - t0) * k / n) / DUR:.4f}" for k in range(n + 1))
    typing = (
        f'<clipPath id="type"><rect x="{cx:.1f}" y="{y - FS}" height="{FS + 8}" width="{n * CW:.1f}">'
        f'<animate attributeName="width" dur="{DUR}s" repeatCount="indefinite" calcMode="discrete" '
        f'values="0;{widths};{n * CW:.1f}" keyTimes="0;{times};1"/></rect></clipPath>'
    )
    xs = ";".join(f"{cx + k * CW:.1f}" for k in range(n + 1))
    cursor1 = (
        f'<rect y="{y - FS + 3}" width="{CW:.1f}" height="{FS + 2}" fill="{MINT}" x="{cx + n * CW:.1f}">'
        f'<animate attributeName="x" dur="{DUR}s" repeatCount="indefinite" calcMode="discrete" '
        f'values="{cx:.1f};{xs};{cx + n * CW:.1f}" keyTimes="0;{times};1"/>'
        f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" calcMode="discrete" '
        f'values="1;0;1;1;0;0" keyTimes="0;{0.3 / DUR:.4f};{t0 / DUR:.4f};{(t1 + 0.3) / DUR:.4f};{(t1 + 0.35) / DUR:.4f};1"/></rect>'
    )
    body = [
        p1,
        f'<g clip-path="url(#type)"><text x="{cx:.1f}" y="{y}" fill="{TEXT}" textLength="{n * CW:.1f}" lengthAdjust="spacingAndGlyphs">{esc(cmd)}</text></g>',
        cursor1,
    ]

    # Servicios
    t = 3.0
    for i, s in enumerate(services):
        y = TOP + LH * (i + 1)
        body.append(
            f'<g opacity="1">{show(t)}'
            f'<text x="{X0}" y="{y}" fill="{MINT}" font-weight="700">✓</text>'
            f'<text x="{X0 + 2 * CW:.1f}" y="{y}" fill="{TEXT}">{esc(s)}</text></g>'
        )
        t += 0.32

    # Resumen
    y = TOP + LH * (len(services) + 1)
    t += 0.25
    body.append(
        f'<g opacity="1">{show(t)}'
        f'<text x="{X0}" y="{y}" fill="{MUTED}"><tspan fill="{MINT}" font-weight="700">9</tspan> servicios '
        f'<tspan fill="{BLUE_SOFT}">·</tspan> <tspan fill="{MINT}" font-weight="700">11</tspan> años '
        f'<tspan fill="{BLUE_SOFT}">·</tspan> <tspan fill="{MINT}" font-weight="700">28</tspan> clientes '
        f'<tspan fill="{BLUE_SOFT}">·</tspan> <tspan fill="{MINT}" font-weight="700">5</tspan> países</text></g>'
    )

    # Nuevo prompt con cursor parpadeante
    t += 0.6
    y = TOP + LH * (len(services) + 2)
    p2, cx2 = prompt(y)
    body.append(
        f'<g opacity="1">{show(t)}{p2}'
        f'<rect x="{cx2:.1f}" y="{y - FS + 3}" width="{CW:.1f}" height="{FS + 2}" fill="{MINT}">'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/></rect></g>'
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">bluesmile servicios --listar</title>
<desc id="d">Terminal animada que lista los 9 servicios de BlueSmile Technology: Business Intelligence, Servicios de Datos, Infraestructura On-Premise, Servicios Cloud, Desarrollo de Software, Soporte TI, Integración IT/OT, Inteligencia Artificial y Automatización.</desc>
<defs>
  <linearGradient id="win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY_DEEP}"/></linearGradient>
  <linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset=".5" stop-color="{MINT}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>
  {typing}
</defs>
<style>
  text{{font-family:{MONO};font-size:{FS}px;white-space:pre}}
  .title{{font-family:{SANS};font-size:14px;fill:{MUTED}}}
  .glow{{animation:glow 4s ease-in-out infinite alternate}}
  @keyframes glow{{from{{stroke-opacity:.35}}to{{stroke-opacity:.9}}}}
  {REDUCED}
</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#win)"/>
<rect class="glow" x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="none" stroke="url(#edge)" stroke-width="1.5"/>
<path d="M1 47H{W - 1}" stroke="{LINE}"/>
<circle cx="26" cy="24" r="6.5" fill="#ff5f57"/><circle cx="48" cy="24" r="6.5" fill="#febc2e"/><circle cx="70" cy="24" r="6.5" fill="#28c840"/>
<text class="title" x="{W / 2}" y="29" text-anchor="middle">bluesmile@latam: ~</text>
{''.join(body)}
</svg>
"""


# ---------------------------------------------------------------------------
# 3. Cifras con odómetro
# ---------------------------------------------------------------------------
def stats():
    items = [("11", "años de trayectoria"), ("28", "clientes atendidos"), ("5", "países con proyectos"), ("3", "certificaciones ISO")]
    W, H = 1280, 190
    CW_CARD, GAP = 296, 18
    x0 = (W - (CW_CARD * 4 + GAP * 3)) / 2
    FS = 60
    DW = 38  # ancho de dígito
    LHD = 72  # alto de la ventana del odómetro
    cards, css = [], []
    k = 0
    for i, (num, label) in enumerate(items):
        x = x0 + i * (CW_CARD + GAP)
        cx = x + CW_CARD / 2
        nx = cx - len(num) * DW / 2
        base_y = 36
        digits = []
        for j, d in enumerate(num):
            col = "".join(
                f'<text x="{nx + j * DW + DW / 2:.1f}" y="{base_y + 58 + r * LHD}" text-anchor="middle" class="num">{r % 10}</text>'
                for r in range(21)
            )
            target = (10 + int(d)) * LHD
            css.append(
                f".r{k}{{transform:translateY(-{target}px);animation:r{k} {2.0 + j * 0.25:.2f}s cubic-bezier(.15,.85,.25,1) {0.25 + i * 0.18:.2f}s backwards}}"
                f"@keyframes r{k}{{from{{transform:translateY(0)}}}}"
            )
            digits.append(f'<g class="r{k}">{col}</g>')
            k += 1
        cards.append(
            f'<g><rect x="{x}" y="8" width="{CW_CARD}" height="{H - 16}" rx="16" fill="url(#card)" stroke="{LINE}"/>'
            f'<rect x="{x + 24}" y="8" width="{CW_CARD - 48}" height="3" rx="1.5" fill="url(#acc)" class="accent" style="animation-delay:-{i * 0.8}s"/>'
            f'<clipPath id="w{i}"><rect x="{x}" y="{base_y - 4}" width="{CW_CARD}" height="{LHD + 8}"/></clipPath>'
            f'<mask id="m{i}" maskUnits="userSpaceOnUse" x="{x}" y="{base_y - 4}" width="{CW_CARD}" height="{LHD + 8}">'
            f'<rect x="{x}" y="{base_y - 4}" width="{CW_CARD}" height="{LHD + 8}" fill="url(#fadev)"/></mask>'
            f'<g clip-path="url(#w{i})" mask="url(#m{i})">{"".join(digits)}</g>'
            f'<text x="{cx}" y="{H - 34}" text-anchor="middle" class="label">{esc(label)}</text></g>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
<title id="t">11 años de trayectoria, 28 clientes atendidos, 5 países con proyectos, 3 certificaciones ISO</title>
<defs>
  <linearGradient id="card" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY_2}"/></linearGradient>
  <linearGradient id="acc" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{MINT}"/></linearGradient>
  <linearGradient id="fadev" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".22" stop-color="#fff"/><stop offset=".85" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <linearGradient id="numg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="{BLUE_SOFT}"/></linearGradient>
</defs>
<style>
  text{{font-family:{SANS}}}
  .num{{font-size:{FS}px;font-weight:800;fill:#ffffff;font-variant-numeric:tabular-nums}}
  .label{{font-size:17px;fill:{MUTED};font-weight:600}}
  .accent{{animation:pulse 3.2s ease-in-out infinite}}
  @keyframes pulse{{0%,100%{{opacity:.45}}50%{{opacity:1}}}}
  {''.join(css)}
  {REDUCED}
</style>
{''.join(cards)}
</svg>
"""


# ---------------------------------------------------------------------------
# 4. Tarjetas de proyectos
# ---------------------------------------------------------------------------
def card_frame(W, H, bg1, bg2, c1, c2, uid):
    return f"""<defs>
  <linearGradient id="bg{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient>
  <linearGradient id="br{uid}" x1="0" x2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
  <radialGradient id="gl{uid}"><stop offset="0" stop-color="{c1}" stop-opacity=".35"/><stop offset="1" stop-color="{c1}" stop-opacity="0"/></radialGradient>
  <clipPath id="cl{uid}"><rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16"/></clipPath>
</defs>
<g clip-path="url(#cl{uid})">
  <rect width="{W}" height="{H}" fill="url(#bg{uid})"/>
  <circle class="glowb" cx="{W - 60}" cy="40" r="230" fill="url(#gl{uid})"/>
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="#ffffff" stroke-opacity=".10"/>
<rect class="comet" x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="url(#br{uid})" stroke-width="2.5" stroke-linecap="round" pathLength="1000"/>"""


def card_css(extra=""):
    return f"""<style>
  text{{font-family:{SANS}}}
  .mono{{font-family:{MONO}}}
  .title{{font-size:30px;font-weight:800;fill:#ffffff;letter-spacing:-.3px}}
  .tagl{{font-size:16px;font-weight:600}}
  .desc{{font-size:15.5px;fill:#cbd5e1}}
  .chipt{{font-size:12.5px;font-weight:700;fill:#ffffff}}
  .kpi{{font-size:24px;font-weight:800;fill:#ffffff}}
  .kpil{{font-size:12.5px;fill:#94a3b8;font-weight:600}}
  .comet{{stroke-dasharray:110 890;animation:comet 7s linear infinite}}
  .glowb{{animation:breath 6s ease-in-out infinite alternate}}
  @keyframes comet{{from{{stroke-dashoffset:1000}}to{{stroke-dashoffset:0}}}}
  @keyframes breath{{from{{opacity:.55}}to{{opacity:1}}}}
  {extra}
  {REDUCED}
</style>"""


def chips(items, x_right, y):
    """Chips alineados a la derecha. items: (texto, ancho, color)."""
    out = []
    x = x_right
    for label, w, col in reversed(items):
        x -= w
        out.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="12" fill="{col}" fill-opacity=".22" stroke="{col}" stroke-opacity=".6"/>'
            f'<text x="{x + w / 2}" y="{y + 16.5}" text-anchor="middle" class="chipt">{esc(label)}</text>'
        )
        x -= 8
    return "".join(out)


def kpis(items, x0, y, w):
    out = []
    for i, (v, l) in enumerate(items):
        x = x0 + i * w
        out.append(
            f'<text x="{x}" y="{y}" class="kpi">{esc(v)}</text>'
            f'<text x="{x}" y="{y + 20}" class="kpil">{esc(l)}</text>'
        )
        if i:
            out.append(f'<path d="M{x - 18} {y - 22}V{y + 22}" stroke="#ffffff" stroke-opacity=".1"/>')
    return "".join(out)


def card_aisdk():
    W, H = 640, 340
    c1, c2, c3 = "#a78bfa", "#60a5fa", "#22d3ee"
    providers = ["OpenAI", "Claude", "Gemini", "Mistral", "Bedrock", "Cohere", "Ollama", "Groq", "DeepSeek"]
    slot = 112
    period = slot * len(providers)
    names = "".join(
        f'<text x="{k * slot + slot / 2}" y="0" text-anchor="middle" class="prov">{p}</text>'
        f'<circle cx="{(k + 1) * slot}" cy="-5" r="2.5" fill="{c3}" fill-opacity=".6"/>'
        for k, p in enumerate(providers)
    )
    extra = (
        f".prov{{font-size:14px;font-weight:700;fill:#e2e8f0}}"
        f".marq{{animation:marq 26s linear infinite}}"
        f"@keyframes marq{{to{{transform:translateX(-{period}px)}}}}"
        f".spark{{transform-box:fill-box;transform-origin:center;animation:spin 9s linear infinite}}"
        f"@keyframes spin{{to{{transform:rotate(360deg)}}}}"
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">AiSdk.Net</title>
<desc id="d">SDK open source para construir apps y agentes de IA en .NET 10: 7 proveedores, 15 paquetes, más de 200 tests.</desc>
{card_frame(W, H, "#0b1020", "#1c1147", c1, c3, "a")}
<defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7c3aed"/><stop offset="1" stop-color="#06b6d4"/></linearGradient>
<linearGradient id="tg" x1="0" x2="1"><stop offset="0" stop-color="{c1}"/><stop offset=".5" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/></linearGradient>
<linearGradient id="fadeL" x1="0" x2="1"><stop offset="0" stop-color="#140f33"/><stop offset=".12" stop-color="#140f33" stop-opacity="0"/><stop offset=".88" stop-color="#140f33" stop-opacity="0"/><stop offset="1" stop-color="#140f33"/></linearGradient>
<clipPath id="band"><rect x="1" y="282" width="{W - 2}" height="57"/></clipPath></defs>
{card_css(extra)}
<rect x="32" y="30" width="58" height="58" rx="14" fill="url(#lg)"/>
<path class="spark" d="M61 41 L65.5 54.5 L79 59 L65.5 63.5 L61 77 L56.5 63.5 L43 59 L56.5 54.5Z" fill="#ffffff"/>
<text x="106" y="58" class="title">AiSdk.Net</text>
<text x="106" y="83" class="tagl" fill="url(#tg)">SDK de IA y agentes para .NET 10</text>
{chips([("C#", 44, c1), (".NET 10", 72, c2), ("MIT", 48, c3)], W - 30, 34)}
<text x="32" y="128" class="desc">Una sola API, independiente del proveedor, para texto, streaming,</text>
<text x="32" y="150" class="desc">objetos tipados, herramientas, agentes, multi-agente, RAG, MCP y workflows.</text>
{kpis([("7", "proveedores"), ("15", "paquetes NuGet"), ("200+", "tests"), ("0", "warnings")], 32, 212, 150)}
<g clip-path="url(#band)">
  <rect x="0" y="282" width="{W}" height="58" fill="#000000" fill-opacity=".22"/>
  <path d="M0 282.5H{W}" stroke="#ffffff" stroke-opacity=".08"/>
  <g transform="translate(0 316)"><g class="marq">{names}<g transform="translate({period} 0)">{names}</g></g></g>
  <rect x="0" y="282" width="{W}" height="58" fill="url(#fadeL)"/>
</g>
</svg>
"""


def card_gob():
    W, H = 640, 340
    blue, red, light = "#006fb3", "#fe6565", "#a8b7c7"
    bars = [("Clases oficiales", 1.0, "100 %"), ("Paridad visual", 0.9952, "99,52 %"), ("Alto contraste", 0.9947, "99,47 %")]
    bx, bw = 200, 300
    bar_svg = []
    css = []
    for i, (label, v, txt) in enumerate(bars):
        y = 128 + i * 34
        bar_svg.append(
            f'<text x="32" y="{y + 5}" class="bl">{esc(label)}</text>'
            f'<rect x="{bx}" y="{y - 5}" width="{bw}" height="10" rx="5" fill="#ffffff" fill-opacity=".08"/>'
            f'<rect class="fill f{i}" x="{bx}" y="{y - 5}" width="{bw * v:.1f}" height="10" rx="5" fill="url(#gb)"/>'
            f'<text x="{W - 32}" y="{y + 5}" text-anchor="end" class="bv">{esc(txt)}</text>'
        )
        css.append(f".f{i}{{animation:grow 1.6s cubic-bezier(.2,.8,.2,1) {0.3 + i * 0.25:.2f}s backwards}}")
    extra = (
        f".bl{{font-size:14px;fill:#cbd5e1;font-weight:600}}"
        f".bv{{font-size:15px;fill:#ffffff;font-weight:800}}"
        f".fill{{transform-box:fill-box;transform-origin:left center}}"
        f"@keyframes grow{{from{{transform:scaleX(0)}}}}"
        f".star{{transform-box:fill-box;transform-origin:center;animation:twinkle 3.5s ease-in-out infinite}}"
        f"@keyframes twinkle{{0%,100%{{transform:scale(1)}}50%{{transform:scale(.86)}}}}"
        f".sheen{{animation:sheen 4.5s ease-in-out infinite}}"
        f"@keyframes sheen{{0%{{transform:translateX(-120px)}}70%,100%{{transform:translateX({bw + 40}px)}}}}"
        + "".join(css)
    )
    # Estrella de cinco puntas centrada en (61, 59)
    import math
    pts = []
    for k in range(10):
        r = 17 if k % 2 == 0 else 7
        a = -math.pi / 2 + k * math.pi / 5
        pts.append(f"{61 + r * math.cos(a):.1f},{60 + r * math.sin(a):.1f}")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">framework-gob</title>
<desc id="d">Framework CSS del Gobierno de Chile sobre Tailwind CSS 4: 100 % de las clases oficiales, 99,52 % de paridad visual, 427 íconos y librería React.</desc>
{card_frame(W, H, "#0a132d", "#0d2350", blue, red, "g")}
<defs><linearGradient id="gb" x1="0" x2="1"><stop offset="0" stop-color="{blue}"/><stop offset="1" stop-color="#3fa3e8"/></linearGradient>
<linearGradient id="sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".45"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="bars"><rect x="{bx}" y="118" width="{bw}" height="90"/></clipPath></defs>
{card_css(extra)}
<g clip-path="url(#clg)"><rect x="0" y="0" width="{W / 2}" height="6" fill="{blue}"/><rect x="{W / 2}" y="0" width="{W / 2}" height="6" fill="{red}"/></g>
<rect x="32" y="30" width="58" height="58" rx="14" fill="{blue}"/>
<polygon class="star" points="{' '.join(pts)}" fill="#ffffff"/>
<text x="106" y="58" class="title">framework-gob</text>
<text x="106" y="83" class="tagl" fill="{light}">Gobierno de Chile × Tailwind CSS 4</text>
{chips([("CSS", 50, blue), ("Tailwind 4", 88, "#38bdf8"), ("React 19", 76, red)], W - 30, 34)}
{''.join(bar_svg)}
<g clip-path="url(#bars)"><rect class="sheen" x="{bx}" y="118" width="80" height="90" fill="url(#sh)"/></g>
<path d="M32 236H{W - 32}" stroke="#ffffff" stroke-opacity=".08"/>
<text x="32" y="262" class="desc">Migración íntegra de gob.cl (Bootstrap 4 + jQuery): mismo diseño y</text>
<text x="32" y="284" class="desc">mismas clases, con tokens de Tailwind y JavaScript sin dependencias.</text>
<text x="32" y="318" class="kpil"><tspan fill="#ffffff" font-weight="800">427</tspan> íconos  ·  <tspan fill="#ffffff" font-weight="800">React</tspan> librería de componentes  ·  <tspan fill="#ffffff" font-weight="800">IA</tspan> skill para agentes</text>
</svg>
"""


# ---------------------------------------------------------------------------
# 5. Pie con olas
# ---------------------------------------------------------------------------
def footer():
    W, H = 1280, 150

    def wave(amp, base, period):
        # Onda que se repite cada `period` px; se dibuja el doble de ancho para desplazarla sin cortes.
        d = f"M0 {base}"
        x = 0
        while x < W * 2 + period:
            d += f" q{period / 4} {-amp} {period / 2} 0 t{period / 2} 0"
            x += period
        d += f" V{H} H0Z"
        return d

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="BlueSmile Technology">
<defs>
  <linearGradient id="w1" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}" stop-opacity=".55"/><stop offset="1" stop-color="{CYAN}" stop-opacity=".55"/></linearGradient>
  <linearGradient id="w2" x1="0" x2="1"><stop offset="0" stop-color="{MINT}" stop-opacity=".45"/><stop offset="1" stop-color="{BLUE}" stop-opacity=".45"/></linearGradient>
  <linearGradient id="w3" x1="0" x2="1"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY_2}"/></linearGradient>
  <clipPath id="c"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<style>
  text{{font-family:{SANS}}}
  .a{{animation:mv 14s linear infinite}}
  .b{{animation:mv 9s linear infinite reverse}}
  .c{{animation:mv 20s linear infinite}}
  @keyframes mv{{to{{transform:translateX(-320px)}}}}
  {REDUCED}
</style>
<g clip-path="url(#c)">
  <path class="a" d="{wave(18, 58, 320)}" fill="url(#w1)"/>
  <path class="b" d="{wave(14, 72, 320)}" fill="url(#w2)"/>
  <path class="c" d="{wave(10, 86, 320)}" fill="url(#w3)"/>
  <text x="{W / 2}" y="126" text-anchor="middle" font-size="17" font-weight="700" fill="#ffffff" letter-spacing="1.5">BLUESMILE TECHNOLOGY</text>
</g>
</svg>
"""


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    write("header.svg", header())
    write("terminal.svg", terminal())
    write("stats.svg", stats())
    write("project-aisdk.svg", card_aisdk())
    write("project-framework-gob.svg", card_gob())
    write("footer.svg", footer())
