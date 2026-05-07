import streamlit as st

st.set_page_config(
    page_title="Tamarin Rule Generator",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------- Styling ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    :root {
        --bg: #0b1020;
        --panel: #111733;
        --panel-2: #161d3d;
        --border: #232b55;
        --text: #e7ecff;
        --muted: #9aa3c7;
        --accent: #7c5cff;
        --accent-2: #22d3ee;
        --success: #34d399;
        --warn: #f59e0b;
        --danger: #f43f5e;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* App background gradient */
    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(1200px 600px at 10% -10%, rgba(124,92,255,0.18), transparent 60%),
            radial-gradient(900px 500px at 110% 10%, rgba(34,211,238,0.15), transparent 60%),
            linear-gradient(180deg, #0a0f1f 0%, #0b1020 100%);
        color: var(--text);
    }

    [data-testid="stHeader"] { background: transparent; }

    .main .block-container,
    [data-testid="stMainBlockContainer"] {
        max-width: 1280px;
        margin: 0 auto;
        padding-top: 1.25rem;
        padding-bottom: 3rem;
    }

    /* ---------- Hero ---------- */
    .hero {
        position: relative;
        padding: 28px 32px;
        border-radius: 18px;
        border: 1px solid var(--border);
        background:
            linear-gradient(135deg, rgba(124,92,255,0.18), rgba(34,211,238,0.10) 60%, rgba(11,16,32,0.0)),
            var(--panel);
        overflow: hidden;
        margin-bottom: 22px;
    }
    .hero::after {
        content: "";
        position: absolute; inset: 0;
        background-image:
            linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
        background-size: 28px 28px;
        mask-image: radial-gradient(circle at 30% 30%, black, transparent 70%);
        pointer-events: none;
    }
    .hero-row { display: flex; align-items: center; gap: 18px; position: relative; z-index: 1; }
    .hero-badge {
        font-size: 11px; letter-spacing: .14em; text-transform: uppercase;
        color: var(--accent-2);
        background: rgba(34,211,238,0.08);
        border: 1px solid rgba(34,211,238,0.25);
        padding: 4px 10px; border-radius: 999px;
    }
    .hero h1 {
        margin: 8px 0 6px 0;
        font-size: 34px;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: var(--text);
    }
    .hero p {
        color: var(--muted);
        margin: 0;
        font-size: 15px;
        max-width: 720px;
    }
    .hero-emoji {
        font-size: 42px;
        filter: drop-shadow(0 4px 16px rgba(124,92,255,0.5));
    }

    /* ---------- Section labels ---------- */
    .section-label {
        display: flex; align-items: center; gap: 10px;
        margin: 4px 0 10px 0;
        font-size: 13px; letter-spacing: .12em; text-transform: uppercase;
        color: var(--muted);
        font-weight: 600;
    }
    .section-label .dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: var(--accent);
        box-shadow: 0 0 12px var(--accent);
    }

    /* ---------- Panel cards ---------- */
    .card {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 18px;
    }

    /* ---------- Inputs ---------- */
    textarea {
        resize: none !important;
        font-family: 'JetBrains Mono', ui-monospace, Menlo, Consolas, monospace !important;
        font-size: 14px !important;
        line-height: 1.55 !important;
        background: #0e1430 !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
    }
    textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px rgba(124,92,255,0.18) !important;
    }

    /* ---------- Buttons ---------- */
    .stButton > button {
        border-radius: 12px !important;
        border: 1px solid var(--border) !important;
        background: var(--panel-2) !important;
        color: var(--text) !important;
        font-weight: 600 !important;
        height: 42px;
        transition: transform .04s ease, box-shadow .15s ease, border-color .15s ease;
    }
    .stButton > button:hover {
        border-color: var(--accent) !important;
        box-shadow: 0 6px 22px rgba(124,92,255,0.18);
    }
    .stButton > button:active { transform: translateY(1px); }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #7c5cff, #22d3ee) !important;
        border: 0 !important;
        color: #0b1020 !important;
    }
    .stDownloadButton > button {
        border-radius: 12px !important;
        border: 1px solid var(--border) !important;
        background: var(--panel-2) !important;
        color: var(--text) !important;
        font-weight: 600 !important;
        height: 42px;
    }
    .stDownloadButton > button:hover {
        border-color: var(--accent-2) !important;
        box-shadow: 0 6px 22px rgba(34,211,238,0.18);
    }
    .stDownloadButton > button:disabled {
        opacity: .5;
    }

    /* ---------- Code block ---------- */
    pre, code, [data-testid="stCodeBlock"] {
        font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace !important;
        font-size: 13px !important;
    }
    [data-testid="stCodeBlock"] {
        border-radius: 12px !important;
        border: 1px solid var(--border) !important;
    }

    /* ---------- Metric cards ---------- */
    .metric {
        background: var(--panel-2);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 12px 14px;
        display: flex; flex-direction: column; gap: 4px;
    }
    .metric .label {
        font-size: 11px; text-transform: uppercase; letter-spacing: .1em;
        color: var(--muted);
    }
    .metric .value {
        font-size: 22px; font-weight: 700; color: var(--text);
    }
    .metric .value.accent { color: var(--accent-2); }

    /* ---------- Step list ---------- */
    .steps { display: flex; flex-direction: column; gap: 6px; }
    .step {
        display: grid;
        grid-template-columns: 28px 1fr;
        gap: 10px;
        padding: 10px 12px;
        background: var(--panel-2);
        border: 1px solid var(--border);
        border-radius: 10px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
    }
    .step.bad { border-color: rgba(244,63,94,0.45); background: rgba(244,63,94,0.08); }
    .step .num {
        display: inline-flex; align-items: center; justify-content: center;
        width: 24px; height: 24px; border-radius: 6px;
        background: rgba(124,92,255,0.15);
        color: var(--accent-2);
        font-size: 11px; font-weight: 700;
    }
    .step.bad .num { background: rgba(244,63,94,0.18); color: var(--danger); }
    .actor { color: var(--accent-2); font-weight: 600; }
    .arrow { color: var(--muted); padding: 0 6px; }
    .msg { color: #fef3c7; }
    .step .err {
        color: var(--danger); font-size: 12px; margin-top: 4px;
    }

    /* ---------- Empty state ---------- */
    .empty {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 100%;
        gap: 10px; padding: 30px;
        color: var(--muted); text-align: center;
    }
    .empty .glyph {
        font-size: 38px; opacity: .8;
        filter: drop-shadow(0 4px 14px rgba(124,92,255,0.35));
    }

    /* ---------- Sidebar ---------- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0f1f 0%, #0b1020 100%) !important;
        border-right: 1px solid var(--border);
    }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: var(--text);
    }
    .side-title {
        font-size: 12px; letter-spacing: .14em; text-transform: uppercase;
        color: var(--muted); margin: 14px 0 8px 0; font-weight: 600;
    }
    .side-card {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }
    .side-card .name { font-weight: 600; color: var(--text); margin-bottom: 4px; font-size: 14px; }
    .side-card .desc { color: var(--muted); font-size: 12px; line-height: 1.4; }

    .syntax-line {
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 8px 10px;
        color: var(--text);
        margin-bottom: 6px;
    }

    /* ---------- Tabs ---------- */
    [data-testid="stTabs"] [data-baseweb="tab-list"] {
        gap: 4px;
        background: var(--panel);
        padding: 4px;
        border-radius: 10px;
        border: 1px solid var(--border);
    }
    [data-testid="stTabs"] [data-baseweb="tab"] {
        height: 34px;
        padding: 0 14px;
        background: transparent;
        color: var(--muted);
        border-radius: 8px;
    }
    [data-testid="stTabs"] [aria-selected="true"] {
        background: var(--panel-2) !important;
        color: var(--text) !important;
    }

    /* ---------- Responsive ---------- */
    @media (max-width: 900px) {
        [data-testid="stHorizontalBlock"] { flex-wrap: wrap; }
        [data-testid="stHorizontalBlock"] > [data-testid="column"] {
            flex: 1 1 100% !important;
            width: 100% !important;
            min-width: 100% !important;
        }
        .hero h1 { font-size: 26px; }
    }

    /* hide default streamlit footer & menu for cleaner look */
    footer, #MainMenu { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Session state ----------
if "output" not in st.session_state:
    st.session_state.output = ""
if "error" not in st.session_state:
    st.session_state.error = ""
if "protocol_text" not in st.session_state:
    st.session_state.protocol_text = ""


# ---------- Example protocols ----------
EXAMPLES = {
    "Simple Login": (
        "User -> Server: Login\n"
        "Server -> User: Token"
    ),
    "Needham–Schroeder (sketch)": (
        "A -> B: NA\n"
        "B -> A: NB\n"
        "A -> B: NB"
    ),
    "Diffie–Hellman (sketch)": (
        "A -> B: gx\n"
        "B -> A: gy\n"
        "A -> B: K"
    ),
    "Three-Party Auth": (
        "Client -> Auth: Request\n"
        "Auth -> Client: Challenge\n"
        "Client -> Auth: Response\n"
        "Auth -> Server: Ticket\n"
        "Server -> Client: Session"
    ),
}


def load_example(name):
    st.session_state.protocol_text = EXAMPLES[name]
    st.session_state.output = ""
    st.session_state.error = ""


# ---------- Parsing ----------
def parse_protocol(text):
    steps = []
    invalid = []
    lines = text.strip().split("\n")

    for i, raw in enumerate(lines, start=1):
        line = raw.strip()
        if not line:
            continue
        if "->" in line and ":" in line:
            parts = line.split(":", 1)
            actors = parts[0].split("->")
            if len(actors) != 2:
                invalid.append((i, raw, "Expected exactly one '->'."))
                continue
            sender = actors[0].strip()
            receiver = actors[1].strip()
            message = parts[1].strip()
            if not sender or not receiver or not message:
                invalid.append((i, raw, "Sender, receiver, and message are required."))
                continue
            steps.append({
                "step": len(steps) + 1,
                "line": i,
                "from": sender,
                "to": receiver,
                "message": message,
            })
        else:
            invalid.append((i, raw, "Use the form `A -> B: message`."))

    return steps, invalid


def generate_tamarin_rules(protocol):
    rules = []
    for step in protocol:
        sender = step["from"]
        receiver = step["to"]
        message = step["message"]
        step_no = step["step"]

        send_rule = f"""rule Step_{step_no}_{sender}_to_{receiver}:
  [ Fr(~{message}) ]
  -->
  [ Out({message}), State({sender},{receiver},{message}) ]
"""
        receive_rule = f"""rule Step_{step_no}_{receiver}_receives:
  [ In({message}), State({sender},{receiver},{message}) ]
  -->
  [ ]
"""
        rules.append(send_rule)
        rules.append(receive_rule)

    return "\n".join(rules)


# ---------- Actions ----------
def on_generate():
    text = st.session_state.protocol_text
    if text.strip() == "":
        st.session_state.error = "Please enter at least one protocol step."
        st.session_state.output = ""
        return
    parsed, _ = parse_protocol(text)
    if not parsed:
        st.session_state.error = "No valid steps detected. Use the form `A -> B: message`."
        st.session_state.output = ""
        return
    st.session_state.output = generate_tamarin_rules(parsed)
    st.session_state.error = ""


def on_clear():
    st.session_state.output = ""
    st.session_state.error = ""
    st.session_state.protocol_text = ""


# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("### 🔐 Tamarin Studio")
    st.caption("Protocol → formal verification rules")

    st.markdown('<div class="side-title">Quick Examples</div>', unsafe_allow_html=True)
    for name in EXAMPLES:
        st.button(
            name,
            key=f"ex_{name}",
            on_click=load_example,
            args=(name,),
            use_container_width=True,
        )

    st.markdown('<div class="side-title">Syntax</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="syntax-line">Sender -> Receiver: message</div>'
        '<div class="syntax-line">Alice -> Bob: NA</div>'
        '<div class="syntax-line">Bob -> Alice: NB</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="side-title">About</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="side-card">'
        '<div class="name">Tamarin Prover</div>'
        '<div class="desc">A formal verification tool for cryptographic protocols. '
        'This generator scaffolds <code>.spthy</code> rules from a high-level '
        'message-passing description.</div>'
        '</div>',
        unsafe_allow_html=True,
    )


# ---------- Hero ----------
st.markdown(
    """
    <div class="hero">
      <div class="hero-row">
        <div class="hero-emoji">🔐</div>
        <div>
          <div class="hero-badge">Formal Verification · Tamarin</div>
          <h1>Protocol → Tamarin Rule Generator</h1>
          <p>Sketch a cryptographic protocol as message-passing steps, and instantly generate Tamarin
          <code>.spthy</code> rules ready for analysis.</p>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------- Live parse for stats / preview ----------
parsed_steps, invalid_lines = parse_protocol(st.session_state.protocol_text)
actors = sorted({s["from"] for s in parsed_steps} | {s["to"] for s in parsed_steps})

# ---------- Metrics row ----------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(
        f'<div class="metric"><div class="label">Steps Detected</div>'
        f'<div class="value accent">{len(parsed_steps)}</div></div>',
        unsafe_allow_html=True,
    )
with m2:
    st.markdown(
        f'<div class="metric"><div class="label">Actors</div>'
        f'<div class="value">{len(actors)}</div></div>',
        unsafe_allow_html=True,
    )
with m3:
    st.markdown(
        f'<div class="metric"><div class="label">Invalid Lines</div>'
        f'<div class="value" style="color:{"#f43f5e" if invalid_lines else "#34d399"}">'
        f'{len(invalid_lines)}</div></div>',
        unsafe_allow_html=True,
    )
with m4:
    rule_count = len(parsed_steps) * 2
    st.markdown(
        f'<div class="metric"><div class="label">Rules to Generate</div>'
        f'<div class="value">{rule_count}</div></div>',
        unsafe_allow_html=True,
    )

st.write("")

# ---------- Main two-column layout ----------
left, right = st.columns(2, gap="large")

with left:
    st.markdown(
        '<div class="section-label"><span class="dot"></span>Protocol Input</div>',
        unsafe_allow_html=True,
    )
    st.text_area(
        "Protocol steps",
        key="protocol_text",
        height=380,
        label_visibility="collapsed",
        placeholder="User -> Server: Login\nServer -> User: Token",
    )

    c1, c2 = st.columns([1, 1])
    with c1:
        st.button(
            "⚡ Generate Tamarin Rules",
            on_click=on_generate,
            type="primary",
            use_container_width=True,
        )
    with c2:
        st.button("🗑 Clear", on_click=on_clear, use_container_width=True)

    # Live preview of detected steps
    if parsed_steps or invalid_lines:
        st.markdown(
            '<div class="section-label" style="margin-top:18px;">'
            '<span class="dot"></span>Detected Steps</div>',
            unsafe_allow_html=True,
        )
        items_html = '<div class="steps">'
        for s in parsed_steps:
            items_html += (
                f'<div class="step">'
                f'<span class="num">{s["step"]}</span>'
                f'<span><span class="actor">{s["from"]}</span>'
                f'<span class="arrow">→</span>'
                f'<span class="actor">{s["to"]}</span>'
                f'<span class="arrow">:</span>'
                f'<span class="msg">{s["message"]}</span></span>'
                f'</div>'
            )
        for line_no, raw, reason in invalid_lines:
            safe = (raw or "").replace("<", "&lt;").replace(">", "&gt;")
            items_html += (
                f'<div class="step bad">'
                f'<span class="num">!</span>'
                f'<span><span class="msg">{safe or "(empty)"}</span>'
                f'<div class="err">Line {line_no}: {reason}</div></span>'
                f'</div>'
            )
        items_html += "</div>"
        st.markdown(items_html, unsafe_allow_html=True)


with right:
    st.markdown(
        '<div class="section-label"><span class="dot"></span>Tamarin Rules Output</div>',
        unsafe_allow_html=True,
    )

    tab_rules, tab_summary = st.tabs(["📜 Rules", "📊 Summary"])

    with tab_rules:
        if st.session_state.error:
            st.warning(st.session_state.error)
        elif st.session_state.output:
            st.code(st.session_state.output, language="text")
        else:
            st.markdown(
                '<div class="card" style="height:420px;">'
                '<div class="empty">'
                '<div class="glyph">📜</div>'
                '<div><strong>No rules yet</strong></div>'
                '<div>Enter a protocol on the left and click '
                '<em>Generate Tamarin Rules</em> to see the output here.</div>'
                '</div></div>',
                unsafe_allow_html=True,
            )

    with tab_summary:
        if st.session_state.output and parsed_steps:
            actor_lines = "".join(
                f'<div class="step"><span class="num">·</span>'
                f'<span class="actor">{a}</span></div>'
                for a in actors
            )
            st.markdown(
                f'<div class="card">'
                f'<div style="display:flex; gap:14px; flex-wrap:wrap; margin-bottom:14px;">'
                f'  <div class="metric" style="flex:1; min-width:140px;">'
                f'    <div class="label">Total Steps</div>'
                f'    <div class="value accent">{len(parsed_steps)}</div></div>'
                f'  <div class="metric" style="flex:1; min-width:140px;">'
                f'    <div class="label">Total Rules</div>'
                f'    <div class="value">{len(parsed_steps) * 2}</div></div>'
                f'</div>'
                f'<div class="section-label" style="margin-top:0;">'
                f'<span class="dot"></span>Actors</div>'
                f'<div class="steps">{actor_lines}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="card"><div class="empty">'
                '<div class="glyph">📊</div>'
                '<div>Generate rules to see a summary.</div>'
                '</div></div>',
                unsafe_allow_html=True,
            )

    st.write("")
    d1, d2 = st.columns([1, 1])
    with d1:
        st.download_button(
            label="⬇️ Download .spthy",
            data=st.session_state.output or "",
            file_name="protocol.spthy",
            mime="text/plain",
            disabled=not st.session_state.output,
            use_container_width=True,
        )
    with d2:
        st.download_button(
            label="📋 Copy as .txt",
            data=st.session_state.output or "",
            file_name="protocol.txt",
            mime="text/plain",
            disabled=not st.session_state.output,
            use_container_width=True,
        )
