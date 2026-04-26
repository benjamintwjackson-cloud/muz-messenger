import streamlit as st

# --- STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = "HOME"
if 'hours' not in st.session_state: st.session_state.hours = 0
if 'day' not in st.session_state: st.session_state.day = 1

def nav(target): st.session_state.page = target
def advance_time():
    st.session_state.hours += 2
    if st.session_state.hours >= 24:
        st.session_state.hours = 0
        st.session_state.day += 1
    st.toast(f"Time Advanced: {st.session_state.hours:02d}:00")

# --- CUSTOM CSS: THE 3x4 GRID & THEME ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #1a1c22 !important; }
    [data-testid="stHeader"] { visibility: hidden; }
    .main .block-container { padding: 1rem; max-width: 350px; margin: auto; }

    /* The LCD Screen */
    .nokia-screen {
        background-color: #c7d19e;
        border: 4px solid #2b3d20;
        height: 280px;
        padding: 10px;
        font-family: 'Courier New', monospace;
        color: #2b3d20 !important;
        margin-bottom: 20px;
        box-sizing: border-box;
    }
    .lcd-header { border-bottom: 2px solid #2b3d20; margin-bottom: 8px; font-weight: bold; font-size: 12px; display: flex; justify-content: space-between; }
    .lcd-line { font-weight: 900; font-size: 14px; margin: 0; text-transform: uppercase; }

    /* Keypad Layout */
    .stButton > button {
        width: 100%;
        height: 45px;
        border-radius: 6px;
        font-weight: bold;
        background-color: #3d405b;
        color: white;
        border: 1px solid #222;
        padding: 0;
        font-size: 18px;
    }
    /* Button Colors */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button { border-top: 4px solid #31a24c; } /* Green */
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) button { border-top: 4px solid #d32f2f; } /* Red */
</style>
""", unsafe_allow_html=True)

# --- THE SCREEN RENDER ---
time_str = f"D{st.session_state.day} {st.session_state.hours:02d}:00"
content = ""

if st.session_state.page == "HOME":
    content = f"""<div class='lcd-header'><span>MUZ-3310</span><span>{time_str}</span></div>
    <p class='lcd-line'>1. MESSAGES</p><p class='lcd-line'>2. WAP (NEWS)</p>
    <p class='lcd-line'>3. PRACTICE</p><p class='lcd-line'>4. SCHEDULE</p><p class='lcd-line'>5. SNAKE II</p>"""
elif st.session_state.page == "MESSAGES":
    content = """<div class='lcd-header'><span>INBOX</span></div>
    <p class='lcd-line'>✉ BENGAL LIGHTS</p><p style='font-size:11px;'>READY FOR SOUNDCHECK?</p>
    <p class='lcd-line'>✉ POWERTOOL</p><p style='font-size:11px;'>DON'T SHOW UP TO WHAMMY.</p>"""
elif st.session_state.page == "NEWS":
    content = """<div class='lcd-header'><span>WAP BROWSER</span></div>
    <p class='lcd-line'>[ NEWS FEED ]</p><p style='font-size:12px;'>- bFM TOP 10: B.LIGHTS AT #3</p>
    <p style='font-size:12px;'>- UK: PUNK SCENE BLOWING UP</p>"""

st.markdown(f"<div class='nokia-screen'>{content}</div>", unsafe_allow_html=True)

# --- THE KEYPAD (3x4 Grid + Action Row) ---

# Action Row: Green, Up, Red
c1, c2, c3 = st.columns(3)
with c1: st.button("📞", on_click=advance_time, help="Green: Advance 2 Hours")
with c2: st.button("▲")
with c3: st.button("❌", on_click=nav, args=("HOME",), help="Red: Hang up/Home")

# Row 1: 1, 2, 3
r1_1, r1_2, r1_3 = st.columns(3)
with r1_1: st.button("1", on_click=nav, args=("MESSAGES",))
with r1_2: st.button("2", on_click=nav, args=("NEWS",))
with r1_3: st.button("3")

# Row 2: 4, 5, 6
r2_1, r2_2, r2_3 = st.columns(3)
with r2_1: st.button("4")
with r2_2: st.button("5")
with r2_3: st.button("6")

# Row 3: 7, 8, 9
r3_1, r3_2, r3_3 = st.columns(3)
with r3_1: st.button("7")
with r3_2: st.button("8")
with r3_3: st.button("9")

# Row 4: *, 0, #
r4_1, r4_2, r4_3 = st.columns(3)
with r4_1: st.button("*")
with r4_2: st.button("0")
with r4_3: st.button("#")
