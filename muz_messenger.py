import streamlit as st

# --- STATE (Burning VHS Engine) ---
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

# --- THE "MUZ-BIT HANDHELD" CSS (Zero Margin Build) ---
st.markdown("""
<style>
    /* 1. Kill Streamlit Margins and Header to prevent scrolling */
    [data-testid="stAppViewContainer"] > .main {
        padding: 0px !important;
        margin-top: -60px; /* Pulls the phone up to the top */
    }
    [data-testid="stHeader"] { visibility: hidden; }
    
    .stApp { background-color: #1a1c22 !important; }

    /* 2. The Physical Chassis */
    .handheld-container {
        width: 320px; height: 500px;
        background-color: #d1d5db; /* Classic Gray */
        border-radius: 40px;
        box-shadow: 0px 15px 30px rgba(0,0,0,0.7);
        position: relative; /* All buttons use this for positioning */
        margin: auto;
    }
    
    /* 3. The Green LCD Screen (Dot-Matrix Style) */
    .lcd-screen {
        background-color: #9bbc0f; /* High-Contrast Green */
        border: 8px solid #306230; /* Screen border like image 6 */
        height: 200px;
        width: 280px;
        box-sizing: border-box;
        padding: 10px;
        font-family: 'Courier New', monospace;
        color: #0f380f !important;
        text-align: left;
        
        position: absolute; top: 30px; left: 20px;
    }

    .lcd-line { font-weight: 900; font-size: 15px; margin: 0; text-transform: uppercase; line-height: 1.2; }
    .selected { background-color: #306230; color: #9bbc0f !important; padding: 2px; }

    /* 4. THE VISUAL D-PAD (A single plus shape) */
    .dpad-area {
        width: 90px; height: 90px;
        background-color: #262626; /* Charcoal D-Pad from image 6 */
        clip-path: polygon(33% 0%, 66% 0%, 66% 33%, 100% 33%, 100% 66%, 66% 66%, 66% 100%, 33% 100%, 33% 66%, 0% 66%, 0% 33%, 33% 33%);
        position: absolute; bottom: 100px; left: 20px;
    }

    /* 5. A/B Buttons (The circular logic) */
    .buttons-area {
        position: absolute; bottom: 100px; right: 20px;
        display: flex; gap: 15px; flex-direction: column; /* Staggered, GameBoy style */
    }

    /* CIRCULAR CSS LOGIC: Making standard Streamlit buttons round */
    .circ-btn > button {
        width: 60px !important; height: 60px !important;
        border-radius: 50% !important; /* Perfect circles */
        background-color: #d32f2f !important; /* GameBoy Red/Purple */
        color: white !important; font-weight: bold; border: 3px solid #111 !important;
    }

    /* Select/Start Buttons (Rubber Look) */
    .select-start-area {
        position: absolute; bottom: 20px; left: 100px;
        display: flex; gap: 10px;
    }
    .sl-st-btn > button {
        background-color: #3f3f46 !important; /* lower-case gray rubber */
        color: white !important; border: 1px solid #111 !important;
    }

    /* Invisible Click Areas for D-Pad cardinal directions */
    .dpad-clicker > button {
        width: 30px !important; height: 30px !important;
        position: absolute !important;
        opacity: 0 !important; /* Invisible, just a click area */
    }
</style>
""", unsafe_allow_html=True)

# --- LCD CONTENT ---
content = ""
if st.session_state.page == "HOME":
    content = f"<b>MUZ-BIT v1.0 | {st.session_state.hours:02d}:00</b><hr>"
    for i, item in enumerate(MENU_ITEMS):
        if i == st.session_state.cursor:
            content += f"<p class='lcd-line selected'>▶ {item}</p>"
        else:
            content += f"<p class='lcd-line'>  {item}</p>"
elif st.session_state.page == "MESSAGES":
    content = "<b>INBOX</b><hr><p class='lcd-line'>✉ BENGAL LIGHTS</p><p style='font-size:11px'>Ready for Whammy?</p>"
elif st.session_state.page == "WAP NEWS":
    content = "<b>WAP NEWS</b><hr><p class='lcd-line'>UK: PUNK SCENE BLOWING UP</p><p class='lcd-line'>NZ: bFM TOP 10 #1</p>"

# --- THE PHYSICAL CHASSIS ASSEMBLY ---
st.markdown(f"""
    <div class="handheld-container">
        <div class="lcd-screen">{content}</div>
        
        <div class="dpad-area"></div>
        <div class="buttons-area">
            <div class="circ-btn"><p style='font-size:11px;color:#000;'>B</p></div>
            <div class="circ-btn"><p style='font-size:11px;color:#000;'>A</p></div>
        </div>
        
        <div class="select-start-area">
            <p style='font-size:10px;color:#000;'>SELECT</p>
            <p style='font-size:10px;color:#000;'>START</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- THE FUNCTIONAL BUTTONS (Absolute positioned click areas) ---

# 1. D-PAD CLICKS (Invisible buttons over the plus shape cardinal points)
# Up (Positioned over visual plus)
with st.container():
    st.markdown('<div class="dpad-clicker" style="bottom:160px;left:50px;"></div>', unsafe_allow_html=True)
    st.button("", key="dp_up", on_click=move_cursor, args=(-1,))
# Down
with st.container():
    st.markdown('<div class="dpad-clicker" style="bottom:100px;left:50px;"></div>', unsafe_allow_html=True)
    st.button("", key="dp_down", on_click=move_cursor, args=(1,))

# 2. A/B CLICKS (Styled circular buttons positioned on the right)
# Button A (Enter)
with st.container():
    st.markdown('<div class="circ-btn" style="position:absolute;bottom:100px;right:20px;z-index:10;"></div>', unsafe_allow_html=True)
    st.button("A", key="btn_a", on_click=press_a, help="Enter")
# Button B (Back/Home)
with st.container():
    st.markdown('<div class="circ-btn" style="position:absolute;bottom:135px;right:85px;z-index:10;"></div>', unsafe_allow_html=True)
    st.button("B", key="btn_b", on_click=press_b, help="Back")

# 3. SELECT/START (Styled rectangular below)
# SELECT (Back)
with st.container():
    st.markdown('<div class="sl-st-btn" style="position:absolute;bottom:40px;left:90px;z-index:10;"></div>', unsafe_allow_html=True)
    st.button("select", key="btn_sel", on_click=press_b, help="Back")
# START (Advance 2h)
with st.container():
    st.markdown('<div class="sl-st-btn" style="position:absolute;bottom:40px;left:180px;z-index:10;"></div>', unsafe_allow_html=True)
    st.button("start", key="btn_sta", on_click=press_start, help="Advance 2H")
