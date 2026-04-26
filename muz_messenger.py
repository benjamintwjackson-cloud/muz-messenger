import streamlit as st

# --- CUSTOM MSN STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #f1f5f9; }
    .msn-header { 
        background: linear-gradient(to bottom, #4a90e2, #2171cd);
        color: white; padding: 10px; border-radius: 5px 5px 0 0;
        font-family: 'Tahoma', sans-serif; display: flex; align-items: center;
    }
    .status-dot { height: 12px; width: 12px; background-color: #31a24c; border-radius: 50%; display: inline-block; margin-right: 10px; border: 1px solid white; }
    .chat-bubble {
        background-color: white; padding: 12px; border-radius: 15px;
        border: 1px solid #ddd; margin-bottom: 10px; font-family: 'Tahoma', sans-serif;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .band-name { font-weight: bold; color: #2171cd; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="msn-header">
        <span class="status-dot"></span>
        MUZ Messenger - Maeve (Online)
    </div>
    """, unsafe_allow_html=True)

# --- THE FIELDWORK FEED ---
st.write("### 👥 Contacts")
with st.expander("The Bengal Lights (Current Focus)", expanded=True):
    st.progress(0.45, text="Ego: 45%")
    st.markdown('<div class="chat-bubble"><p class="band-name">Bengal Lights:</p>Yo Boss, Powertool Records just messaged us. They offered us a slot at Ding Dong Lounge... what do we do?</div>', unsafe_allow_html=True)

with st.expander("Rival: Powertool Records"):
    st.markdown('<div class="chat-bubble"><p class="band-name">Powertool:</p>Nice press release. Would be a shame if someone booked out the Powerstation for the next three months. 😉</div>', unsafe_allow_html=True)

# --- THE "MASTER DOCK" SYNC ---
st.write("---")
st.write("### 🛠 Action Center")
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Accept Offer"):
        st.success("Accepted! Sent to Master Dock for Soundcheck.")
with col2:
    if st.button("💸 Send Pizza ($40)"):
        st.toast("Ego decreased! The band is happy.")
