import streamlit as st

# --- STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = "HOME"
if 'cursor' not in st.session_state: st.session_state.cursor = 0
if 'hours' not in st.session_state: st.session_state.hours = 0

MENU_ITEMS = ["MESSAGES", "WAP NEWS", "PRACTICE", "SCHEDULE", "SNAKE II"]

def move(d): st.session_state.cursor = (st.session_state.cursor + d) % len(MENU_ITEMS)
def nav(p): st.session_state.page = p
def tick(): st.session_state.hours = (st.session_state.hours + 2) % 24

# --- THE "ULTIMATE HANDHELD" CSS ---
st.markdown("""
<style>
    /* 1. Reset the Viewport */
    [data-testid="stAppViewContainer"] { background-color: #1a1c22 !important; }
    [data-testid="stHeader"] { visibility: hidden; }
    .main .block-container { padding: 10px !important; max-width: 320px; margin: auto; }

    /* 2. The Game Boy Chassis */
    .chassis {
        background-color: #d1d5db; /* Classic Gray */
        padding: 20px;
        border-radius: 15px 15px 60px 15px; /* That iconic bottom corner curve */
        border: 4px solid #9ca3af;
        box-shadow: inset -5px -5px 0px #9ca3af, 10px 10px 20px rgba(0,0,0,0.5);
    }

    /* 3. The Dot-Matrix Screen */
    .screen {
        background-color: #9bbc0f;
        border: 15px solid #374151; /* The dark grey screen bezel */
        height: 200px;
        padding: 10px;
        font-family: 'monospace';
        color: #0f380f !important;
        box-shadow: inset 3px 3px 10px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }
    .selected { background-color: #306230; color: #9bbc0f !important; }

    /* 4. Force 3-Column Keypad without Stacking */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 5px !important;
        align-items: center;
    }
    div[data-testid="stHorizontalBlock"] > div { width: 33% !important; min-width: 0px !important; }

    /* 5. Button Styling */
    /* D-PAD (Charcoal) */
    .dpad button { background-color: #262626 !important; color: white !important; height: 45px !important; border: 1px solid #000 !important; }
    
    /* A/B Buttons (Circular Red) */
    .ab-btn button { 
        background-color: #8b0000 !important; 
        color: white !important; 
        border-radius: 50% !important; 
        height: 55px !important; width: 55px !important;
        border: 2px solid #580000 !important;
        font-weight: bold !important;
    }

    /* Select/Start (Pills) */
    .pill button { 
        background-color: #71717a !important; 
        border-radius: 20px !important; 
        height: 15px !important; 
        font-size: 10px !important;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# --- RENDER THE SCREEN ---
content = ""
if st.session_state.page == "HOME":
    content = f"<small>D1 | {st.session_state.hours:02d}:00</small><br><b>MUZ-BIT</b><hr>"
    for i, item in enumerate(MENU_ITEMS):
        cls = "selected" if i == st.session_state.cursor else ""
        content += f"<div class='{cls}'>▶ {item}</div>"
else:
    content = f"<b>{st.session_state.page}</b><hr><p>Incoming...<br>Check Master Dock for details.</p>"

st.markdown(f"<div class='chassis'><div class='screen'>{content}</div>", unsafe_allow_html=True)

# --- THE CONTROLS (D-PAD & A/B) ---
# This row contains the D-Pad on the left and A/B on the right
col_left, col_mid, col_right = st.columns([1.5, 0.5, 2])

with col_left:
    # A 3x3 styled grid for the D-Pad
    st.markdown("<div class='dpad'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c2.button("▲", on_click=move, args=(-1,))
    
    r2_1, r2_2, r2_3 = st.columns(3)
    r2_1.button("◀")
    r2_2.button("ok") # Center of D-pad
    r2_3.button("▶")
    
    r3_1, r3_2, r3_3 = st.columns(3)
    r3_1.button("▼", on_click=move, args=(1,))
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    # A/B Buttons (Staggered)
    st.markdown("<div class='ab-btn'>", unsafe_allow_html=True)
    st.write(" ") # Padding
    st.button("B", on_click=nav, args=("HOME",))
    st.button("A", on_click=nav, args=(MENU_ITEMS[st.session_state.cursor],))
    st.markdown("</div>", unsafe_allow_html=True)

# --- SELECT / START ---
st.write("")
s1, s2, s3, s4, s5 = st.columns([1,2,1,2,1])
with s2:
    st.markdown("<div class='pill'>", unsafe_allow_html=True)
    st.button("select", on_click=nav, args=("HOME",))
    st.markdown("</div>", unsafe_allow_html=True)
with s4:
    st.markdown("<div class='pill'>", unsafe_allow_html=True)
    st.button("start", on_click=tick)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True) # End Chassis
