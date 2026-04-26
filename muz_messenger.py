import streamlit as st

# --- NOKIA 3310 "PRO" STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #2c3e50 !important; }
    .nokia-bezel {
        background-color: #8e9aaf; padding: 30px 15px; border-radius: 40px;
        border: 8px solid #4a4e69; max-width: 380px; margin: auto;
    }
    .nokia-screen {
        background-color: #c7d19e; color: #2b3d20 !important;
        font-family: 'Courier New', monospace; padding: 15px;
        border: 4px solid #2b3d20; height: 420px; border_radius: 5px;
    }
    .nokia-text { color: #2b3d20 !important; font-weight: bold; font-size: 16px; margin: 0; }
    .ticker { background-color: #b5c18e; padding: 5px; font-size: 12px; border-bottom: 1px solid #2b3d20; }
    </style>
    """, unsafe_allow_html=True)

# --- THE WORLD STATE ---
if 'menu_path' not in st.session_state:
    st.session_state.menu_path = ["HOME"]
if 'current_band' not in st.session_state:
    st.session_state.current_band = "BENGAL LIGHTS"

# --- THE HUD (NEWS TICKER) ---
news_items = [
    "UK: Post-Punk revival hits London... ",
    "AKL: Whammy Bar runs out of Export Gold... ",
    "USA: Pitchfork gives Bandicoot 8.2... ",
    "INDUSTRY: Powertool Records CEO seen in Silverdale... "
]
st.markdown(f'<div class="ticker"><marquee>{ " | ".join(news_items) }</marquee></div>', unsafe_allow_html=True)

# --- THE SCREEN ---
st.markdown('<div class="nokia-bezel"><div class="nokia-screen">', unsafe_allow_html=True)

current = st.session_state.menu_path[-1]

if current == "HOME":
    st.markdown(f'<p class="nokia-text">-- {st.session_state.current_band} --</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">1. Messages</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">2. World News</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">3. Promoter Log</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">4. A&R Scout</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">5. Snake II</p>', unsafe_allow_html=True)

elif current == "MESSAGES":
    st.markdown('<p class="nokia-text">[ INBOX ]</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">> Band: "Gig was lush."</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">> Rival: "Check the charts."</p>', unsafe_allow_html=True)

elif current == "WORLD NEWS":
    st.markdown('<p class="nokia-text">[ GLOBAL FEED ]</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">- NZ: Sure Boy tour sold out in 4 mins.</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">- UK: Wet Leg seen wearing Bacio Merch.</p>', unsafe_allow_html=True)

elif current == "A&R SCOUT":
    st.markdown('<p class="nokia-text">[ SCENE SCOUT ]</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">BANDICOOT: Hype 88%</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">GOD BOWS: Hype 42%</p>', unsafe_allow_html=True)
    st.markdown('<p class="nokia-text">-- Powertool spying on both --</p>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# --- NOKIA BUTTONS (The Nested Engine) ---
st.write("")
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("BACK"):
        if len(st.session_state.menu_path) > 1: st.session_state.menu_path.pop()
with c2:
    st.button("▲") # Navigation would go here
with c3:
    if st.button("SEL"):
        # Very simple hardcoded dive for the demo
        if current == "HOME": st.session_state.menu_path.append("MESSAGES")
