import streamlit as st

# --- NOKIA OS INITIALIZATION ---
if 'page' not in st.session_state:
    st.session_state.page = "HOME"
if 'scroll_idx' not in st.session_state:
    st.session_state.scroll_idx = 0

# --- THE HARDENED UI SKIN ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #1a1c22 !important; }
    [data-testid="stHeader"] { visibility: hidden; }
    .main .block-container { padding-top: 1rem; }

    .nokia-bezel {
        background-color: #8e9aaf;
        padding: 25px 15px;
        border-radius: 40px;
        border: 6px solid #4a4e69;
        width: 300px;
        margin: auto;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.5);
    }
    
    .nokia-screen {
        background-color: #c7d19e;
        border: 4px solid #2b3d20;
        height: 320px;
        width: 100%;
        box-sizing: border-box;
        padding: 10px;
        font-family: 'Courier New', monospace;
        color: #2b3d20 !important;
    }

    .lcd-header { border-bottom: 2px solid #2b3d20; margin-bottom: 8px; font-weight: bold; font-size: 12px; }
    .lcd-line { font-weight: 900; font-size: 14px; margin: 0; text-transform: uppercase; line-height: 1.2; }
    .selected { background-color: #2b3d20; color: #c7d19e !important; }

    /* Keypad Styling */
    .stButton>button {
        background: #4a4e69; color: white; border: 1px solid #222;
        border-radius: 8px; font-weight: bold; width: 100%; height: 45px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ENGINE ---
def nav(target):
    st.session_state.page = target

# --- SCREEN CONTENT GENERATOR ---
screen_html = ""

if st.session_state.page == "HOME":
    screen_html = f"""
    <div class="lcd-header">MUZ-3310 | MENU</div>
    <p class="lcd-line">1. MESSAGES</p>
    <p class="lcd-line">2. WAP BROWSER (NEWS)</p>
    <p class="lcd-line">3. PRACTICE</p>
    <p class="lcd-line">4. SCHEDULE</p>
    <p class="lcd-line">5. SNAKE II</p>
    """
elif st.session_state.page == "MESSAGES":
    screen_html = """
    <div class="lcd-header">INBOX (2)</div>
    <p class="lcd-line">✉ BENGAL LIGHTS</p>
    <p class="lcd-line" style="font-size:11px;">"WHERE IS THE VAN?"</p>
    <p class="lcd-line">✉ POWERTOOL REC</p>
    <p class="lcd-line" style="font-size:11px;">"STAY OUT OF AKL."</p>
    """
elif st.session_state.page == "NEWS":
    screen_html = """
    <div class="lcd-header">WAP: GLOBAL NEWS</div>
    <p class="lcd-line">>>> bFM TOP 10</p>
    <p class="lcd-line">B.LIGHTS @ #4</p>
    <p class="lcd-line">---------------</p>
    <p class="lcd-line">>>> LONDON BEAT</p>
    <p class="lcd-line">VINYL SOLD OUT</p>
    """

# --- RENDER HARDWARE ---
st.markdown(f"""
    <div class="nokia-bezel">
        <div class="nokia-screen">
            {screen_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- THE NUMERICAL DIALPAD ---
st.write("")
pad_container = st.container()
with pad_container:
    # Soft Keys
    c1, c2, c3 = st.columns(3)
    with c1: st.button("CLR", on_click=nav, args=("HOME",))
    with c2: st.button("▲")
    with c3: st.button("SEL")
    
    # Row 1
    r1c1, r1c2, r1c3 = st.columns(3)
    with r1c1: st.button("1", on_click=nav, args=("MESSAGES",))
    with r1c2: st.button("2", on_click=nav, args=("NEWS",))
    with r1c3: st.button("3")
    
    # Row 2
    r2c1, r2c2, r2c3 = st.columns(3)
    with r2c1: st.button("4")
    with r2c2: st.button("5")
    with r2c3: st.button("6")

    # Row 3 (Bottom)
    r3c1, r3c2, r3c3 = st.columns(3)
    with r3c1: st.button("7")
    with r3c2: st.button("8")
    with r3c3: st.button("9")
