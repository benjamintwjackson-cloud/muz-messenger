import streamlit as st

# --- HARDENED NOKIA STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #1a1c22 !important; }
    
    /* The Physical Case */
    .nokia-bezel {
        background-color: #8e9aaf;
        padding: 30px 15px;
        border-radius: 40px;
        border: 8px solid #4a4e69;
        width: 320px; /* Fixed width for better framing */
        margin: auto;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.5);
        text-align: center;
    }
    
    /* The LCD Screen */
    .nokia-screen {
        background-color: #c7d19e;
        border: 4px solid #2b3d20;
        height: 380px;
        width: 100%;
        box-sizing: border-box; /* Crucial for keeping text inside */
        padding: 15px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        text-align: left;
    }

    /* Screen Text */
    .lcd-text {
        color: #2b3d20 !important;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 16px;
        line-height: 1.4;
        margin: 0;
        white-space: pre-wrap; /* Keeps spacing exactly as coded */
    }

    .lcd-header {
        border-bottom: 2px solid #2b3d20;
        width: 100%;
        margin-bottom: 10px;
        padding-bottom: 4px;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE SHARED ENGINE LOGIC ---
if 'menu' not in st.session_state:
    st.session_state.menu = "HOME"

# --- RENDER THE LOCKED FRAME ---
# We build the entire screen as a single HTML string
screen_content = ""

if st.session_state.menu == "HOME":
    screen_content = f"""
    <div class="lcd-header">16:20 | MUZ-3310</div>
    <p class="lcd-text">1. Check Messages</p>
    <p class="lcd-text">2. Check News</p>
    <p class="lcd-text">3. Book Practice</p>
    <p class="lcd-text">4. Check Schedule</p>
    <p class="lcd-text">5. Snake II</p>
    """
elif st.session_state.menu == "NEWS":
    screen_content = """
    <div class="lcd-header">GLOBAL NEWS</div>
    <p class="lcd-text">- bFM: Bengal Lights
    entering Top 10.</p>
    <p class="lcd-text">- UK: Vinyl prices
    hit record high.</p>
    <p class="lcd-text">- PT: Powertool signs
    new 'mystery' act.</p>
    """

# Wrap the content in the Bezel and Screen divs
st.markdown(f"""
    <div class="nokia-bezel">
        <div class="nokia-screen">
            {screen_content}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PHYSICAL INPUTS (Outside the frame) ---
st.write("")
c1, c2, c3 = st.columns([1,1,1])
with c1:
    if st.button("CLR"):
        st.session_state.menu = "HOME"
with c2:
    st.button("▲")
with c3:
    if st.button("SEL"):
        st.session_state.menu = "NEWS"
