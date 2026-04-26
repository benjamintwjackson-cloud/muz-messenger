import streamlit as st

# --- CLASSIC MSN SKIN CSS ---
st.markdown("""
    <style>
    /* Force high-contrast text and background */
    .stApp { background-color: #FFFFFF !important; color: #000000 !important; }
    
    /* Header: The Iconic MSN Blue Gradient */
    .msn-header {
        background: linear-gradient(to bottom, #73a3d4 0%, #005da3 100%);
        color: white !important;
        padding: 12px;
        font-family: 'Tahoma', 'Segoe UI', sans-serif;
        font-weight: bold;
        border-radius: 8px 8px 0 0;
        display: flex; align-items: center;
        border: 1px solid #004a80;
    }

    /* Status Bar: "What's on your mind?" */
    .status-area {
        background-color: #e9eff7;
        border: 1px solid #adc4e5;
        padding: 8px;
        margin-top: -1px;
        font-size: 13px;
        color: #444 !important;
    }

    /* Chat Bubbles: Soft Blue/Grey */
    .chat-bubble {
        background: #f1f6fb;
        border: 1px solid #c5d7ef;
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 15px;
        color: #000 !important;
    }

    .band-label { color: #d32f2f !important; font-weight: bold; }
    .rival-label { color: #1976d2 !important; font-weight: bold; }
    
    /* Buttons: Silver XP Style */
    .stButton>button {
        background: linear-gradient(to bottom, #ffffff 0%, #e0e0e0 100%);
        border: 1px solid #707070;
        color: #333 !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE APP CONTENT ---
st.markdown('<div class="msn-header">🟢 MUZ Messenger - Bengal Lights (Online)</div>', unsafe_allow_html=True)
st.markdown('<div class="status-area"><i>"Waiting for the Master Dock to sync..."</i></div>', unsafe_allow_html=True)

st.write("") # Spacer

with st.container():
    st.markdown('''<div class="chat-bubble"><span class="band-label">Bengal Lights says:</span><br>
    Yo, the sound engineer at Whammy is being a total diva. Can you Nudge him?</div>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="chat-bubble"><span class="rival-label">Powertool Records says:</span><br>
    Saw your radio numbers. Cute. We just bought the ad space on the bFM breakfast slot for the whole month.</div>''', unsafe_allow_html=True)
