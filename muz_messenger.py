import streamlit as st
import streamlit.components.v1 as components

# --- SYSTEM SETTINGS ---
st.set_page_config(layout="centered")

# --- THE HANDHELD COMPONENT ---
# This is raw HTML/JS. Streamlit cannot touch or "reflow" this.
handheld_html = """
<style>
    body { background-color: #1a1c22; display: flex; justify-content: center; align-items: flex-start; height: 100vh; margin: 0; font-family: monospace; overflow: hidden; }
    
    /* The Physical Case */
    .chassis {
        background-color: #d1d5db; width: 320px; height: 560px;
        border-radius: 20px 20px 60px 20px; border: 4px solid #9ca3af;
        position: relative; box-shadow: 10px 10px 0px #000;
        user-select: none;
    }

    /* The Screen */
    .screen-bezel { background-color: #374151; padding: 20px; border-radius: 10px; margin: 20px; }
    .screen {
        background-color: #9bbc0f; height: 160px; border: 4px solid #306230;
        padding: 10px; color: #0f380f; overflow: hidden;
    }
    .selected { background-color: #306230; color: #9bbc0f; }

    /* D-PAD (The Plus) */
    .dpad {
        position: absolute; bottom: 120px; left: 30px;
        width: 90px; height: 90px;
    }
    .dp-btn {
        position: absolute; background: #262626; border: 2px solid #000;
        color: white; font-size: 10px; display: flex; align-items: center; justify-content: center;
    }
    .dp-up { width: 30px; height: 30px; left: 30px; top: 0; border-radius: 4px 4px 0 0; }
    .dp-down { width: 30px; height: 30px; left: 30px; top: 60px; border-radius: 0 0 4px 4px; }
    .dp-left { width: 30px; height: 30px; left: 0; top: 30px; border-radius: 4px 0 0 4px; }
    .dp-right { width: 30px; height: 30px; left: 60px; top: 30px; border-radius: 0 4px 4px 0; }
    .dp-mid { width: 30px; height: 30px; left: 30px; top: 30px; background: #262626; border: none; }

    /* A/B Buttons (Circles) */
    .btn-a, .btn-b {
        position: absolute; width: 55px; height: 55px;
        border-radius: 50%; background: #8b0000; border: 3px solid #580000;
        color: white; font-weight: bold; display: flex; align-items: center; justify-content: center;
        box-shadow: 2px 2px 0px #000;
    }
    .btn-b { bottom: 160px; right: 85px; }
    .btn-a { bottom: 130px; right: 20px; }

    /* Select/Start (Pills) */
    .pill {
        position: absolute; bottom: 40px; width: 50px; height: 12px;
        background: #71717a; border-radius: 10px; transform: rotate(-25deg);
        border: 2px solid #3f3f46; cursor: pointer;
    }
    .p-select { left: 100px; }
    .p-start { left: 170px; }
    .pill-label { position: absolute; font-size: 8px; color: #333; bottom: 25px; font-weight: bold; }
</style>

<div class="chassis">
    <div class="screen-bezel">
        <div class="screen" id="display">
            LOADING MUZ-BIT...
        </div>
    </div>

    <div class="dpad">
        <div class="dp-btn dp-up" onclick="nav(-1)">▲</div>
        <div class="dp-btn dp-mid"></div>
        <div class="dp-btn dp-down" onclick="nav(1)">▼</div>
        <div class="dp-btn dp-left">◀</div>
        <div class="dp-btn dp-right">▶</div>
    </div>

    <div class="btn-b" onclick="goHome()">B</div>
    <div class="btn-a" onclick="confirm()">A</div>

    <div class="pill p-select" onclick="goHome()"></div>
    <div class="pill-label" style="left:100px;">SELECT</div>
    <div class="pill p-start" onclick="advanceTime()"></div>
    <div class="pill-label" style="left:170px;">START</div>
</div>

<script>
    let menu = ["MESSAGES", "WAP NEWS", "PRACTICE", "SCHEDULE", "SNAKE II"];
    let cursor = 0;
    let page = "HOME";
    let hours = 0;

    function render() {
        const display = document.getElementById('display');
        let html = `<div style="display:flex; justify-content:space-between; font-size:10px; font-weight:bold; border-bottom:1px solid #306230; margin-bottom:5px;">
                        <span>MUZ-BIT</span><span>${hours.toString().padStart(2, '0')}:00</span>
                    </div>`;

        if (page === "HOME") {
            menu.forEach((item, i) => {
                let cls = (i === cursor) ? "class='selected'" : "";
                html += `<div ${cls} style="font-size:14px; font-weight:bold; text-transform:uppercase;">${(i===cursor ? "▶ " : "  ") + item}</div>`;
            });
        } else if (page === "MESSAGES") {
            html += "<b>INBOX</b><br><small>B.LIGHTS: Ready?</small><br><small>PT: Back off.</small>";
        } else if (page === "WAP NEWS") {
            html += "<b>WAP BROWSER</b><br><small>bFM: #1 SPOT!</small><br><small>UK: VINYL SHORTAGE</small>";
        }
        display.innerHTML = html;
    }

    function nav(dir) {
        cursor = (cursor + dir + menu.length) % menu.length;
        render();
    }

    function confirm() {
        page = menu[cursor];
        render();
    }

    function goHome() {
        page = "HOME";
        render();
    }

    function advanceTime() {
        hours = (hours + 2) % 24;
        render();
    }

    render();
</script>
"""

# Render the component
components.html(handheld_html, height=600)
