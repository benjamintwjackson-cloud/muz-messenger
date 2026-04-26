import streamlit as st

# --- STATE ---
if 'page' not in st.session_state: st.session_state.page = "HOME"
if 'cursor' not in st.session_state: st.session_state.cursor = 0
if 'hours' not in st.session_state: st.session_state.hours = 0

# --- THE MENU DATA ---
MENU_ITEMS = ["MESSAGES", "WAP NEWS", "PRACTICE", "SCHEDULE", "SNAKE II"]

# --- NAVIGATION LOGIC ---
def move_cursor(direction):
    st.session_state.cursor = (st.session_state.cursor + direction) % len(MENU_ITEMS)

def press_a():
    target = MENU_ITEMS[st.session_state.cursor]
    st.session_state.page = target

def press_b():
    st.session_state.page = "HOME"

def press_start():
    st.session_state.hours = (st.session_state.hours + 2) % 24
    st.toast(f"Time Advanced: {st.session_state.hours:02d}:00")

# --- 8-BIT CSS: THE HANDHELD CASE ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #1a1c22 !important; }
    .main .block-container { padding: 10px !important; max-width: 320px; margin: auto; }
    [data-testid="stHeader"] { visibility: hidden; }

    /* The GameBoy Style Screen */
    .lcd-screen {
        background-color: #9bbc0f; /* GameBoy Green */
        border: 6px solid #306230;
        height: 220px;
        padding: 10px;
        font-family: 'Courier New', monospace;
        color: #0f380f !important;
        margin-bottom: 20px;
        box-sizing: border-box;
    }
    .lcd-line { font-weight: 900; font-size: 15px; margin: 0; text-transform: uppercase; }
    .selected { background-color: #306230; color: #9bbc0f !important; padding: 2px; }

    /* Force the Controller Grid */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 5px !important;
        justify-content: center;
    }

    /* Chunky 8-Bit Buttons */
    .stButton > button {
        width: 100% !important;
        height: 50px !important;
        background-color: #8b0000 !important; /* NES Red */
        color: white !important;
        border: 3px solid #222 !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    /* D-Pad specific color */
    div[data-testid="stHorizontalBlock"]:nth-child(even) button {
        background-color: #333 !important; /* Charcoal D-Pad */
    }
</style>
""", unsafe_allow_html=True)

# --- LCD RENDER ---
content = ""
if st.session_state.page == "HOME":
    content = f"<b>MUZ-BIT v1.0 | {st.session_state.hours:02d}:00</b><hr>"
    for i, item in enumerate(MENU_ITEMS):
        if i == st.session_state.cursor:
            content += f"<p class='lcd-line selected'>▶ {item}</p>"
        else:
            content += f"<p class='lcd-line'>  {item}</p>"
elif st.session_state.page == "MESSAGES":
    content = "<b>INBOX</b><hr><p class='lcd-line'>✉ BENGAL LIGHTS</p><p style='font-size:11px'>Ready for K-Road?</p>"
elif st.session_state.page == "WAP NEWS":
    content = "<b>WAP BROWSER</b><hr><p class='lcd-line'>UK: PUNK REVIVAL</p><p class='lcd-line'>NZ: bFM TOP 10 #1</p>"

st.markdown(f"<div class='lcd-screen'>{content}</div>", unsafe_allow_html=True)

# --- THE CONTROLLER LAYOUT ---

# 1. THE D-PAD (Up / Down)
st.write("---")
c1, c2, c3 = st.columns(3)
c2.button("▲", on_click=move_cursor, args=(-1,))

r2c1, r2c2, r2c3 = st.columns(3)
r2c1.button("◀")
r2c2.button("▼", on_click=move_cursor, args=(1,))
r2c3.button("▶")

# 2. ACTION BUTTONS (B / A)
st.write("")
ba1, ba2, ba3, ba4 = st.columns(4)
ba3.button("B", on_click=press_b, help="Back")
ba4.button("A", on_click=press_a, help="Enter")

# 3. UTILITY (Start / Select)
st.write("")
s1, s2, s3 = st.columns([1,2,1])
with s2:
    st.button("START (ADVANCE 2H)", on_click=press_start)
