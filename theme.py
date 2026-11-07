"""Look and feel for the clone: CSS, fonts and the animated ladybug mascot (a QA engineer's mascot).
Edit the three CONFIG values to make it yours; everything else is styling."""

# ---------- CONFIG (edit me) ----------
MASCOT_NAME = "Bugsy"
TAGLINE = "I hunt bugs for a living, so I'll tell you straight when something isn't in my notes."
PILLS = ["🤖 AI clone", "🔎 Hybrid RAG", "🐞 Bug-hunter at heart"]
# The assignment requires a visible "This is an AI clone, not the real person." banner.
# Set to False only if your instructor does not require it.
SHOW_BANNER = True
# --------------------------------------

HEAD = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&'
        'family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">')

BUG_SVG = """
<svg viewBox="0 0 200 210" class="bug" role="img" aria-label="Animated ladybug mascot">
  <ellipse class="shadow" cx="100" cy="196" rx="52" ry="8" fill="#000" opacity=".12"/>
  <g class="legs" stroke="#3a2a3a" stroke-width="5" stroke-linecap="round" fill="none">
    <path d="M52 140 L30 152"/><path d="M52 160 L34 178"/><path d="M148 160 L166 178"/>
  </g>
  <path class="armR" d="M148 138 L172 118" stroke="#3a2a3a" stroke-width="5" stroke-linecap="round" fill="none"/>
  <g class="ant" stroke="#3a2a3a" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M84 40 Q74 18 60 16"/><path d="M116 40 Q126 18 140 16"/>
    <circle cx="60" cy="16" r="5" fill="#3a2a3a"/><circle cx="140" cy="16" r="5" fill="#3a2a3a"/>
  </g>
  <ellipse cx="100" cy="132" rx="64" ry="58" fill="#e5484d"/>
  <path d="M100 76 V190" stroke="#3a2a3a" stroke-width="4"/>
  <g fill="#3a2a3a"><circle cx="70" cy="118" r="9"/><circle cx="132" cy="112" r="8"/>
    <circle cx="74" cy="154" r="7"/><circle cx="128" cy="152" r="9"/></g>
  <path d="M60 78 A42 40 0 0 1 140 78 Q100 92 60 78Z" fill="#3a2a3a"/>
  <g class="face">
    <g class="eye"><circle cx="86" cy="64" r="8" fill="#fff"/><circle cx="88" cy="65" r="4" fill="#3a2a3a"/></g>
    <g class="eye"><circle cx="114" cy="64" r="8" fill="#fff"/><circle cx="116" cy="65" r="4" fill="#3a2a3a"/></g>
    <path d="M92 76 Q100 83 108 76" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>
    <circle cx="74" cy="74" r="5" fill="#ff9db6" opacity=".8"/><circle cx="126" cy="74" r="5" fill="#ff9db6" opacity=".8"/>
  </g>
</svg>"""

def hero_html():
    banner = '<div class="neon-badge">🤖 This is an AI clone, not the real person.</div>' if SHOW_BANNER else ""
    pills = "".join(f'<span class="pill">{p}</span>' for p in PILLS)
    return f"""
{banner}
<div class="hero">
  <div class="hero-text">
    <span class="tag">Digital Clone</span>
    <h1>Hi, I'm <span class="hl">Hafsa's</span> AI&nbsp;clone!</h1>
    <p class="lead">{TAGLINE}</p>
    <div class="pills">{pills}</div>
  </div>
  <div class="mascot-box">{BUG_SVG}<span class="spark s1">✨</span><span class="spark s2">✦</span><span class="spark s3">💖</span></div>
</div>"""

FOOTER = f"""<div class="foot"><span>{MASCOT_NAME} says: answers come only from my notes. If it isn't there, I won't make it up.</span></div>"""

CSS = """
:root{--limb:#3a2a3a;--bg:#fff7f0;--bg2:#ffeef0;--card:#fff;--ink:#3a2a3a;--muted:#6f5d6c;--line:#f0dfd0;--bug:#e5484d;
--rose:#ffdfe6;--mint:#def5e2;--butter:#fff1bf;--butter-d:#a77a00;--sky:#dcf0fb;--shadow:0 8px 24px rgba(229,72,77,.12)}
.dark{--limb:#f0dce8;--bg:#1d1620;--bg2:#271b26;--card:#2a2030;--ink:#f6ecf3;--muted:#cdb9c8;--line:#4a3a48;
--rose:#4a2c37;--mint:#244234;--butter:#4a4222;--butter-d:#ffd866;--sky:#1f3a48;--shadow:0 8px 24px rgba(0,0,0,.4)}
body,.gradio-container{background:radial-gradient(circle at 85% 0,var(--bg2) 0,transparent 40%),var(--bg)!important;
font-family:"Nunito",system-ui,sans-serif!important;color:var(--ink)}
.gradio-container{max-width:1040px!important}
h1,h2,h3{font-family:"Fredoka","Nunito",sans-serif!important;color:var(--ink)}
footer{display:none!important}

.ribbon{background:var(--butter);border:2px dashed var(--butter-d);color:var(--ink);font-weight:800;text-align:center;
padding:8px 14px;border-radius:99px;margin:6px auto 18px;max-width:520px;animation:pop 2.4s ease-in-out infinite}
@keyframes pop{0%,100%{transform:rotate(-.6deg) scale(1)}50%{transform:rotate(.6deg) scale(1.03)}}
.hero{display:grid;grid-template-columns:1.3fr .7fr;gap:12px;align-items:center;padding:6px 0 18px}
.hero h1{font-size:clamp(2.1rem,6vw,3.4rem);font-weight:700;line-height:1.1;margin:.1em 0 .25em}
.hero h1 .hl{color:var(--bug)}
.tag{display:inline-block;background:var(--rose);color:var(--bug);font-weight:800;font-size:.8rem;padding:4px 12px;
border-radius:99px;letter-spacing:.6px;text-transform:uppercase}
.lead{font-size:1.1rem;color:var(--muted);max-width:560px;margin:0 0 .7em}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.pill{background:var(--card);border:2px solid var(--line);border-radius:99px;padding:4px 14px;font-weight:700;font-size:.92rem;color:var(--ink)}
.mascot-box{position:relative;display:flex;justify-content:center}
.bug{width:100%;max-width:230px;overflow:visible;animation:bounce 3s ease-in-out infinite;transform-origin:50% 100%;cursor:pointer}
.bug [stroke="#3a2a3a"]{stroke:var(--limb)}
.bug .ant circle{fill:var(--limb)}
.bug .eye{transform-box:fill-box;transform-origin:center;animation:blink 5s infinite}
.bug .ant{transform-box:view-box;transform-origin:100px 40px;animation:wiggle 3s ease-in-out infinite}
.bug .armR{transform-box:fill-box;transform-origin:0% 100%}
.bug:hover .armR{animation:wave .5s ease-in-out 4}
@keyframes bounce{0%,100%{transform:translateY(0) scale(1)}45%{transform:translateY(-9px) scale(.98,1.02)}60%{transform:translateY(0) scale(1.03,.97)}}
@keyframes blink{0%,92%,100%{transform:scaleY(1)}95%{transform:scaleY(.08)}}
@keyframes wiggle{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(4deg)}}
@keyframes wave{0%,100%{transform:rotate(0)}50%{transform:rotate(-35deg)}}
.spark{position:absolute;color:var(--butter-d);animation:twinkle 2.6s ease-in-out infinite;font-size:1.3rem;pointer-events:none}
.s1{top:2%;left:8%}.s2{top:14%;right:6%;animation-delay:.8s}.s3{bottom:18%;right:2%;animation-delay:1.4s}
@keyframes twinkle{0%,100%{opacity:.25;transform:scale(.7) rotate(0)}50%{opacity:1;transform:scale(1.15) rotate(20deg)}}

.hc-card{background:var(--card)!important;border:2px solid var(--line)!important;border-radius:26px!important;
padding:18px!important;box-shadow:var(--shadow)!important;animation:fadeup .7s cubic-bezier(.2,.8,.2,1) both}
.hc-card h3{margin:0 0 6px;font-size:1.25rem}
@keyframes fadeup{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
.gradio-container textarea,.gradio-container input[type=text]{border-radius:16px!important;font-family:"Nunito",system-ui,sans-serif!important}
.gradio-container button.primary{background:var(--bug)!important;border:0!important;border-radius:99px!important;
font-family:"Fredoka","Nunito",system-ui,sans-serif!important;font-size:1.05rem!important;box-shadow:0 4px 0 #b3363a;transition:transform .15s}
.gradio-container button.primary:hover{transform:translateY(-2px)}
.gradio-container button.primary:active{transform:translateY(3px);box-shadow:none}
.chip-btn{background:var(--sky)!important;color:var(--ink)!important;border:0!important;border-radius:14px!important;
font-weight:700!important;transition:transform .15s}
.chip-btn:hover{transform:translateY(-2px) rotate(-1deg)}
.bubble{background:var(--mint)!important;border-radius:22px 22px 22px 4px!important;padding:14px 18px!important;
min-height:90px;font-size:1.05rem;border:0!important;box-shadow:none!important}
.bubble *{background:transparent!important;border:0!important;box-shadow:none!important}
.chunk{background:var(--card);border:2px solid var(--line);border-radius:20px;padding:12px 14px;margin:0 0 10px;
animation:fadeup .6s both}
.chead{display:flex;justify-content:space-between;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:6px}
.src{font-family:"Fredoka","Nunito",sans-serif;font-weight:600;color:var(--ink)}
.score{background:var(--butter);color:var(--ink);font-weight:800;font-size:.8rem;padding:2px 10px;border-radius:99px}
.rk{display:inline-block;font-size:.78rem;font-weight:800;padding:2px 9px;border-radius:99px;margin-right:6px}
.rk.b{background:var(--rose)}.rk.d{background:var(--sky)}.rk.n{background:var(--mint)}
.chunk summary{cursor:pointer;font-weight:600;color:var(--muted);margin-top:6px}
.chunk p{margin:6px 0 0;color:var(--ink);line-height:1.55}
.empty{color:var(--muted);text-align:center;padding:14px}
.foot{text-align:center;color:var(--muted);font-weight:700;padding:18px 0 6px}
@media(max-width:700px){.hero{grid-template-columns:1fr}.mascot-box{order:-1}.bug{max-width:150px}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

# ---------------- Streamlit-specific styling (used by the Streamlit app.py) ----------------
STREAMLIT_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap');
.stApp{color-scheme:light;background:radial-gradient(circle at 85% 0,var(--bg2) 0,transparent 40%),var(--bg)!important;font-family:"Nunito",system-ui,sans-serif}
[data-testid="stHeader"]{background:transparent!important}
.block-container{max-width:1040px!important;padding-top:2.2rem!important}
.stApp [data-testid="stMarkdownContainer"],.stApp [data-testid="stWidgetLabel"] *,.stApp [data-testid="stCaptionContainer"],
.stApp h1,.stApp h2,.stApp h3{color:var(--ink)!important}
.stApp h2,.stApp h3{font-family:"Fredoka","Nunito",sans-serif!important}
[data-testid="stSidebar"]{background:var(--card)!important;border-right:2px dashed var(--line)}
[data-testid="stForm"]{background:var(--card);border:2px solid var(--line)!important;border-radius:26px;padding:18px;
box-shadow:var(--shadow);animation:fadeup .7s cubic-bezier(.2,.8,.2,1) both}
.stTextArea textarea{border-radius:16px!important;background:var(--bg)!important;color:var(--ink)!important;font-family:"Nunito",system-ui,sans-serif!important}
[data-testid="stFormSubmitButton"] button{background:var(--bug)!important;border:0!important;border-radius:99px!important;
box-shadow:0 4px 0 #b3363a;font-family:"Fredoka","Nunito",sans-serif!important;font-size:1.05rem!important;transition:transform .15s}
[data-testid="stFormSubmitButton"] button *{color:#fff!important}
[data-testid="stFormSubmitButton"] button:hover{transform:translateY(-2px)}
[data-testid="stFormSubmitButton"] button:active{transform:translateY(3px);box-shadow:none}
[data-baseweb="select"]>div{border-radius:14px!important;background:var(--card)!important;color:var(--ink)!important}
[data-testid="stSlider"] [role="slider"]{background:var(--bug)!important}
[data-testid="stExpander"]{background:var(--card);border:2px solid var(--line)!important;border-radius:20px!important;
overflow:hidden;animation:fadeup .6s both}
[data-testid="stExpander"] summary{font-weight:700}
[data-testid="stAlert"]{border-radius:18px}
hr{border-color:var(--line)!important;border-top-style:dashed!important}
.bubble{padding:14px 18px;margin:4px 0 10px}
.bubble p:last-child{margin-bottom:0}
"""


# ---------------- Neon effect ----------------
NEON_BASE = """
:root{--n-pink:#ff2e93;--n-cyan:#00cfe8;--n-violet:#8b5cf6}
.neon-badge{display:block;width:max-content;max-width:100%;margin:0 auto 16px;padding:5px 16px;border-radius:99px;
font-weight:800;font-size:.86rem;color:#00788a;background:#fff;border:2px solid var(--n-cyan);
text-shadow:0 0 6px rgba(0,207,232,.55);animation:neonpulse 2.8s ease-in-out infinite}
@keyframes neonpulse{0%,100%{box-shadow:0 0 5px var(--n-cyan),0 0 14px rgba(0,207,232,.45),inset 0 0 6px rgba(0,207,232,.2)}
50%{box-shadow:0 0 9px var(--n-cyan),0 0 26px rgba(0,207,232,.75),inset 0 0 10px rgba(0,207,232,.35)}}
.hero h1 .hl{color:var(--n-pink)!important;
text-shadow:0 0 5px rgba(255,46,147,.8),0 0 16px rgba(255,46,147,.55),0 0 36px rgba(255,46,147,.35);animation:flicker 6s infinite}
@keyframes flicker{0%,17%,22%,25%,53%,57%,100%{opacity:1;text-shadow:0 0 5px rgba(255,46,147,.8),0 0 16px rgba(255,46,147,.55),0 0 36px rgba(255,46,147,.35)}
20%,24%,55%{opacity:.8;text-shadow:0 0 2px rgba(255,46,147,.5)}}
.tag{border:2px solid var(--n-pink);background:#fff;color:var(--n-pink);box-shadow:0 0 8px rgba(255,46,147,.5)}
.pill{transition:all .25s}.pill:hover{border-color:var(--n-cyan);box-shadow:0 0 12px rgba(0,207,232,.6);transform:translateY(-2px)}
.bug{filter:drop-shadow(0 0 8px rgba(255,46,147,.6)) drop-shadow(0 0 22px rgba(139,92,246,.4))}
.spark{filter:drop-shadow(0 0 6px var(--n-pink))}
.foot{text-shadow:0 0 8px rgba(255,46,147,.35)}
"""
CSS = CSS + NEON_BASE

NEON_ST = """
.stApp h3{text-shadow:0 0 12px rgba(255,46,147,.25)}
[data-testid="stForm"]{border-color:var(--n-pink)!important;
box-shadow:0 0 12px rgba(255,46,147,.4),0 0 36px rgba(139,92,246,.2)!important}
[data-baseweb="textarea"]:focus-within{border-color:var(--n-cyan)!important;box-shadow:0 0 14px rgba(0,207,232,.65)!important}
[data-testid="stFormSubmitButton"] button{background:linear-gradient(90deg,#ff2e93,#8b5cf6)!important;
box-shadow:0 0 14px rgba(255,46,147,.65),0 0 34px rgba(139,92,246,.4)!important;animation:btnglow 2.4s ease-in-out infinite}
@keyframes btnglow{0%,100%{filter:brightness(1)}50%{filter:brightness(1.12) saturate(1.15)}}
[data-testid="stFormSubmitButton"] button:active{box-shadow:0 0 8px rgba(255,46,147,.6)!important}
.bubble{border:2px solid var(--n-violet)!important;border-radius:22px 22px 22px 4px!important;
box-shadow:0 0 12px rgba(139,92,246,.5),0 0 30px rgba(139,92,246,.2)!important}
[data-testid="stExpander"]{border-color:var(--n-cyan)!important;box-shadow:0 0 8px rgba(0,207,232,.35);transition:box-shadow .25s}
[data-testid="stExpander"]:hover{box-shadow:0 0 16px rgba(0,207,232,.65),0 0 34px rgba(0,207,232,.25)}
[data-testid="stSlider"] [role="slider"]{box-shadow:0 0 10px var(--n-pink)}
"""
STREAMLIT_CSS = STREAMLIT_CSS + NEON_ST