import streamlit as st

# --- STATE ---
if 'page' not in st.session_state: st.session_state.page = "HOME"
if 'hours' not in st.session_state: st.session_state.hours = 0
if 'day' not in st.session_state: st.session_state.day = 1

def nav(target): st.session_state.page = target
def advance_time():
    st.session_state.hours = (st.session_state.hours + 2) % 24
    if st.session_state.hours == 0: st.session_state.day += 1

# --- THE "FORCE GRID" CSS ---
st.markdown("""
<style>
    /* Kill default padding to fit on one screen */
    [data-testid="stAppViewContainer"] { background-color: #1a1c22 !important; }
    .main .block-container { padding: 10px !important; max-width: 320px; margin: auto; }
    [data-testid="stHeader"] { visibility: hidden; }

    /* The LCD Screen */
    .nokia-screen {
        background-color: #c7d19e;
        border: 4px solid #2b3d20;
        height: 240px;
        padding: 10px;
        font-family: 'Courier New', monospace;
        color: #2b3d20 !important;
        margin-bottom: 10px;
        box-sizing: border-box;
    }
    .lcd-header { border-bottom: 2px solid #2b3d20; margin-bottom: 5px; font-weight: bold; font-size: 11px; display: flex; justify-content: space-between; }
    .lcd-line { font-weight: 900; font-size: 14px; margin: 0; text-transform: uppercase; }

    /* FORCE 3-COLUMN GRID (Prevents stacking on mobile) */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 5px !important;
    }
    div[data-testid="stHorizontalBlock"] > div {
        width: 33% !important;
        min-width: 0px !important;
    }

    /* Keypad Styling */
    .stButton > button {
        width: 100% !important;
        height: 45px !important;
        background-color: #3d405b !important;
        color: white !important;
        border: 1px solid #111 !important;
        font-size: 18px !important;
        padding: 0px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- LCD RENDER ---
time_str = f"D{st.session_state.day} {st.session_state.hours:02d}:00"
content = ""

if st.session_state.page == "HOME":
    content = f"<div class='lcd-header'><span>MUZ-3310</span><span>{time_str}</span></div>" \
              "<p class='lcd-line'>1. MESSAGES</p><p class='lcd-line'>2. WAP (NEWS)</p>" \
              "<p class='lcd-line'>3. PRACTICE</p><p class='lcd-line'>4. SCHEDULE</p><p class='lcd-line'>5. SNAKE II</p>"
elif st.session_state.page == "MESSAGES":
    content = "<div class='lcd-header'><span>INBOX</span></div>" \
              "<p class='lcd-line'>✉ BENGAL LIGHTS</p><p style='font-size:11px;'>READY FOR SOUNDCHECK?</p>" \
              "<p class='lcd-line'>✉ POWERTOOL</p><p style='font-size:11px;'>STAY AWAY FROM K-ROAD.</p>"
elif st.session_state.page == "NEWS":
    content = "<div class='lcd-header'><span>WAP BROWSER</span></div>" \
              "<p class='lcd-line'>[ NEWS FEED ]</p><p style='font-size:12px;'>- bFM TOP 10: B.LIGHTS AT #3</p>" \
              "<p style='font-size:12px;'>- UK: VINYL SHIPMENT ARRIVED</p>"

st.markdown(f"<div class='nokia-screen'>{content}</div>", unsafe_allow_html=True)

# --- THE KEYPAD (3-Column Layout) ---

# Control Row
c1, c2, c3 = st.columns(3)
c1.button("📞", on_click=advance_time) # Green: Advance Time
c2.button("▲")
c3.button("❌", on_click=nav, args=("HOME",)) # Red: Hang Up / Back

# Numbers
r1_1, r1_2, r1_3 = st.columns(3)
r1_1.button("1", on_click=nav, args=("MESSAGES",))
r1_2.button("2", on_click=nav, args=("NEWS",))
r1_3.button("3")

r2_1, r2_2, r2_3 = st.columns(3)
r2_1.button("4")
r2_2.button("5")
r2_3.button("6")

r3_1, r3_2, r3_3 = st.columns(3)
r3_1.button("7")
r3_2.button("8")
r3_3.button("9")

r4_1, r4_2, r4_3 = st.columns(3)
r4_1.button("*")
r4_2.button("0")
r4_3.button("#")
