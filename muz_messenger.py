import streamlit as st
import random

# --- SESSION STATE INITIALIZATION ---
if 'ego' not in st.session_state:
    st.session_state.ego = 20
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- BAND MOOD LOGIC ---
moods = ["Happy", "Bored", "Annoyed", "DIVA MODE"]
current_mood = moods[min(3, st.session_state.ego // 25)]

st.title("🟢 MUZ Messenger")
st.markdown(f"**Mood:** {current_mood} | **Ego Level:** {st.session_state.ego}%")
st.progress(st.session_state.ego / 100)

# --- THE "ANGRY MSN" LOGIC ---
if st.session_state.ego > 75:
    st.error("⚠️ Bengal Lights is 'Appearing Offline'. They are tired of practicing.")
    if st.button("Send Peace Offering ($100)"):
        st.session_state.ego -= 30
        st.session_state.money -= 100
        st.session_state.messages.append({"from": "Band", "text": "Fine, the pizza was a good start. We're back."})
