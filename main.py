
import streamlit as st
import time

st.set_page_config(page_title="Terminal", layout="centered")

COMMAND = "> ghost_protocol --inject --ai-awaken --bypass-firewall"

st.markdown("""
    <style>
    .terminal {
        background-color: black;
        color: #00FF00;
        font-family: monospace;
        font-size: 24px;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 0 20px #00FF00;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# Configuration du timing
total_duration = 30  # secondes
typing_duration = 20  # secondes pour l'écriture
cursor_duration = total_duration - typing_duration  # secondes pour le clignotement
n_chars = len(COMMAND)
delay_per_char = typing_duration / n_chars

# Animation lettre par lettre
terminal_placeholder = st.empty()
output = ""
for char in COMMAND:
    output += char
    terminal_placeholder.markdown(f'<div class="terminal">{output}</div>', unsafe_allow_html=True)
    time.sleep(delay_per_char)

# Curseur clignotant à la fin
blink_count = int(cursor_duration / 0.8)  # un clignotement = 0.8s (0.4s on / 0.4s off)
for _ in range(blink_count):
    terminal_placeholder.markdown(f'<div class="terminal">{output}_</div>', unsafe_allow_html=True)
    time.sleep(0.4)
    terminal_placeholder.markdown(f'<div class="terminal">{output}</div>', unsafe_allow_html=True)
    time.sleep(0.4)
