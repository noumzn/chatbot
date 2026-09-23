import streamlit as st
import ollama

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Chatbat AI",
    page_icon="🦇",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Premium dark UI
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background:
            radial-gradient(circle at 75% 8%, rgba(111, 76, 255, 0.12), transparent 28%),
            radial-gradient(circle at 20% 85%, rgba(45, 125, 255, 0.07), transparent 25%),
            #0b0d12;
        color: #f5f7fb;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {background: transparent;}

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #11141b 0%, #0d0f14 100%);
        border-right: 1px solid rgba(255,255,255,0.07);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 11px;
        margin-bottom: 26px;
    }

    .brand-icon {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: linear-gradient(135deg, #6d4aff, #8f6cff);
        box-shadow: 0 8px 28px rgba(109, 74, 255, 0.25);
        font-size: 22px;
    }

    .brand-name {
        font-size: 20px;
        font-weight: 750;
        letter-spacing: -0.4px;
    }

    .brand-sub {
        color: #858b9b;
        font-size: 11px;
        margin-top: 1px;
    }

    .section-label {
        color: #70778a;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1.2px;
        margin: 20px 0 8px;
        text-transform: uppercase;
    }

    /* Main content */
    .main-wrap  {
    max-width: 920px;
    margin: 0 auto;
    padding: 10px 24px 80px;
    }

    .hero {
        text-align: center;
        padding: 10px 0 15px;
    }

    .hero-icon {
        display: inline-flex;
        width: 68px;
        height: 68px;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(109,74,255,.22), rgba(109,74,255,.07));
        border: 1px solid rgba(145,120,255,.20);
        box-shadow: 0 15px 45px rgba(80,50,180,.18);
        font-size: 34px;
        margin-bottom: 17px;
    }

    .hero h1 {
        margin: 0 0 5px;
        font-size: clamp(34px, 5vw, 50px);
        line-height: 1.05;
        letter-spacing: -1.8px;
        font-weight: 800;
        color: #f7f8fb;
    }

    .hero p {
        margin: 12px 0 0;
        color: #9298a8;
        font-size: 15px;
    }

    .status {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        margin-top: 17px;
        padding: 6px 11px;
        border-radius: 999px;
        background: rgba(255,255,255,.045);
        border: 1px solid rgba(255,255,255,.07);
        color: #aeb4c2;
        font-size: 11px;
    }

    .status-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #55d68a;
        box-shadow: 0 0 10px rgba(85,214,138,.55);
    }

    /* Prompt cards */
    .cards-title {
        text-align: center;
        color: #737a8c;
        font-size: 11px;
        margin: 16px 0 10px;
        letter-spacing: .4px;
    }

    div[data-testid="stHorizontalBlock"] {
        gap: 12px;
    }

    .prompt-card button {
        min-height: 92px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 13px;
        border: 1px solid rgba(255,255,255,.08);
        background: rgba(255,255,255,.035);
        color: #e9ebf1;
        transition: all .18s ease;
    }

    .stButton > button:hover {
        border-color: rgba(130,104,255,.55);
        background: rgba(109,74,255,.10);
        color: #fff;
        transform: translateY(-1px);
    }

    /* Select box */
    div[data-baseweb="select"] > div {
        background: #171a22;
        border-color: rgba(255,255,255,.08);
        border-radius: 11px;
    }

    /* Chat bubbles */
    div[data-testid="stChatMessage"] {
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,.055);
        background: rgba(255,255,255,.025);
        padding: 13px 16px;
        margin-bottom: 12px;
    }

    /* Chat input */
    div[data-testid="stChatInput"] {
        max-width: 920px;
        margin: 0 auto;
    }

    div[data-testid="stChatInput"] > div {
        background: #171a22;
        border: 1px solid rgba(255,255,255,.10);
        border-radius: 17px;
        box-shadow: 0 10px 35px rgba(0,0,0,.22);
    }

    div[data-testid="stChatInput"] textarea {
        color: #f4f5f8;
    }

    /* Divider */
    hr {
        border-color: rgba(255,255,255,.06);
    }

    /* Sidebar buttons */
    section[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        min-height: 42px;
    }

    .footer-note {
        text-align: center;
        color: #565d6d;
        font-size: 10px;
        margin-top: 20px;
    }

    /* Animated red bats in the night background */
    .bat-bg {
        position: fixed;
        inset: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        pointer-events: none;
        z-index: 0;
    }

    .bat {
        position: absolute;
        width: 34px;
        height: auto;
        opacity: 0.24;
        filter: drop-shadow(0 0 7px rgba(255, 35, 65, 0.24));
        animation: batFly linear infinite;
        will-change: transform;
    }

    .bat svg {
        display: block;
        width: 100%;
        height: auto;
    }

    .bat-1  { top: 13%; left: -8%;  width: 28px; animation-duration: 22s; animation-delay: -4s; }
    .bat-2  { top: 27%; left: -12%; width: 22px; animation-duration: 27s; animation-delay: -15s; opacity: .20; }
    .bat-3  { top: 42%; left: -9%;  width: 38px; animation-duration: 25s; animation-delay: -8s; }
    .bat-4  { top: 61%; left: -14%; width: 25px; animation-duration: 31s; animation-delay: -22s; opacity: .19; }
    .bat-5  { top: 77%; left: -7%;  width: 31px; animation-duration: 24s; animation-delay: -11s; }
    .bat-6  { top: 90%; left: -15%; width: 20px; animation-duration: 29s; animation-delay: -19s; opacity: .17; }
    .bat-7  { top: 19%; left: -16%; width: 18px; animation-duration: 34s; animation-delay: -27s; opacity: .16; }
    .bat-8  { top: 35%; left: -11%; width: 30px; animation-duration: 28s; animation-delay: -6s; }
    .bat-9  { top: 52%; left: -18%; width: 23px; animation-duration: 32s; animation-delay: -24s; opacity: .18; }
    .bat-10 { top: 69%; left: -10%; width: 35px; animation-duration: 26s; animation-delay: -17s; }
    .bat-11 { top: 83%; left: -20%; width: 19px; animation-duration: 37s; animation-delay: -31s; opacity: .15; }
    .bat-12 { top: 8%;  left: -13%; width: 24px; animation-duration: 30s; animation-delay: -12s; opacity: .18; }

    @keyframes batFly {
        0% {
            transform: translate3d(-12vw, 0, 0) rotate(-5deg);
        }
        18% {
            transform: translate3d(18vw, -18px, 0) rotate(4deg);
        }
        40% {
            transform: translate3d(42vw, 22px, 0) rotate(-3deg);
        }
        62% {
            transform: translate3d(67vw, -14px, 0) rotate(5deg);
        }
        82% {
            transform: translate3d(91vw, 16px, 0) rotate(-4deg);
        }
        100% {
            transform: translate3d(118vw, -8px, 0) rotate(3deg);
        }
    }

    /* Keep the actual interface above the animated layer */
    .main-wrap {
        position: relative;
        z-index: 2;
    }

    section[data-testid="stSidebar"] {
        position: relative;
        z-index: 3;
    }

    /* Slightly richer night atmosphere */
    .stApp {
        background:
            radial-gradient(circle at 72% 8%, rgba(255, 35, 65, 0.055), transparent 22%),
            radial-gradient(circle at 20% 82%, rgba(76, 70, 150, 0.09), transparent 28%),
            linear-gradient(180deg, #080a10 0%, #0b0d14 52%, #080a0f 100%);
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Animated red bats background
# ---------------------------------------------------------
BAT_SVG = """
<svg viewBox="0 0 120 70" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <path d="M60 29
           C52 21 44 15 34 14
           C38 20 37 25 34 29
           C26 22 16 20 5 21
           C12 27 16 34 20 42
           C27 36 35 35 42 38
           C48 41 53 42 60 38
           C67 42 72 41 78 38
           C85 35 93 36 100 42
           C104 34 108 27 115 21
           C104 20 94 22 86 29
           C83 25 82 20 86 14
           C76 15 68 21 60 29 Z"
        fill="#ff334f"/>
</svg>
"""

st.markdown(
    f"""
    <div class="bat-bg" aria-hidden="true">
        <div class="bat bat-1">{BAT_SVG}</div>
        <div class="bat bat-2">{BAT_SVG}</div>
        <div class="bat bat-3">{BAT_SVG}</div>
        <div class="bat bat-4">{BAT_SVG}</div>
        <div class="bat bat-5">{BAT_SVG}</div>
        <div class="bat bat-6">{BAT_SVG}</div>
        <div class="bat bat-7">{BAT_SVG}</div>
        <div class="bat bat-8">{BAT_SVG}</div>
        <div class="bat bat-9">{BAT_SVG}</div>
        <div class="bat bat-10">{BAT_SVG}</div>
        <div class="bat bat-11">{BAT_SVG}</div>
        <div class="bat bat-12">{BAT_SVG}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = None

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">🦇</div>
            <div>
                <div class="brand-name">CHATBAT</div>
                <div class="brand-sub">AI assistant</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("＋  New chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.selected_prompt = None
        st.rerun()

    st.markdown('<div class="section-label">Model</div>', unsafe_allow_html=True)

    try:
        models_info = ollama.list()
        model_names = [m.model for m in models_info.models]
    except Exception as e:
        st.error(f"Could not connect to Ollama: {e}")
        model_names = []

    if model_names:
        selected_model = st.selectbox(
            "Choose a model",
            model_names,
            label_visibility="collapsed",
        )
    else:
        st.warning("No models found. Please run an Ollama model first.")
        selected_model = None

    st.markdown("---")
    st.markdown('<div class="section-label">Conversation</div>', unsafe_allow_html=True)

    if st.button("🗑  Clear chat history", use_container_width=True):
        st.session_state.messages = []
        st.session_state.selected_prompt = None
        st.rerun()

    st.markdown(
        """
        <div style="position:fixed; bottom:18px; color:#555c6b; font-size:10px;">
            Local AI • Powered by Nouman
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# Main area
# ---------------------------------------------------------
st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

# Welcome screen only when there is no chat yet
if not st.session_state.messages:
    st.markdown(
        """
        <div class="hero">
            <div class="hero-icon">🦇</div>
            <h1>How can I help?</h1>
            <p>Ask anything, create something, or explore an idea.</p>
            <div class="status">
                <span class="status-dot"></span>
                Local AI assistant
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="cards-title">TRY SOMETHING</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            "💡  Ask anything\n\nGet a clear answer to your question",
            use_container_width=True,
        ):
            st.session_state.selected_prompt = "Explain artificial intelligence in simple words."
    with col2:
        if st.button(
            "💻  Write code\n\nCreate, explain or debug code",
            use_container_width=True,
        ):
            st.session_state.selected_prompt = "Help me write a Python program."

    col3, col4 = st.columns(2)
    with col3:
        if st.button(
            "✍️  Write something\n\nEmails, ideas, summaries and more",
            use_container_width=True,
        ):
            st.session_state.selected_prompt = "Help me write a professional email."
    with col4:
        if st.button(
            "🍳  Cook something\n\nFind a recipe from what you have",
            use_container_width=True,
        ):
            st.session_state.selected_prompt = "Give me an easy recipe using common ingredients."

    if st.session_state.selected_prompt:
        prompt = st.session_state.selected_prompt
        st.session_state.selected_prompt = None
    else:
        prompt = None
else:
    prompt = None

# ---------------------------------------------------------
# Display existing messages
# ---------------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------------------------
# Chat input
# ---------------------------------------------------------
typed_prompt = st.chat_input("Message Chatbat...")
if typed_prompt:
    prompt = typed_prompt

if prompt:
    if not selected_model:
        st.error("Please select an Ollama model from the sidebar first.")
    else:
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            try:
                stream = ollama.chat(
                    model=selected_model,
                    messages=st.session_state.messages,
                    stream=True,
                )

                for chunk in stream:
                    content = chunk.message.content
                    full_response += content
                    response_placeholder.markdown(full_response + "▌")

                response_placeholder.markdown(full_response)

                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response}
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown(
    '<div class="footer-note">Chatbat runs locally with Ollama</div>',
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
