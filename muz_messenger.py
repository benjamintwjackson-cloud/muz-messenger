import streamlit as st
import streamlit.components.v1 as components

# --- SYSTEM SETTINGS ---
st.set_page_config(layout="centered", page_title="MUZ-BIT Handheld")

# --- THE HANDHELD COMPONENT (HTML/JS) ---
handheld_html = """
<style>
    body { background-color: #1a1c22; display: flex; justify-content: center; align-items: flex-start; height: 100vh; margin: 0; font-family: monospace; overflow: hidden; user-select: none; -webkit-tap-highlight-color: transparent; }
    
    /* The Physical Case */
    .chassis {
        background-color: #d1d5db; width: 320px; height: 580px;
        border-radius: 20px 20px 60px 20px; border: 4px solid #9ca3af;
        position: relative; box-shadow: 10px 10px 0px #000;
    }

    /* The Screen */
    .screen-bezel { background-color: #374151; padding: 20px 20px 35px 20px; border-radius: 10px; margin: 20px; position: relative; }
    .screen {
        background-color: #9bbc0f; height: 170px; border: 4px solid #306230;
        padding: 8px; color: #0f380f; overflow: hidden; position: relative;
    }
    .selected { background-color: #306230; color: #9bbc0f; }

    /* LCD Indicators */
    .indicator-bar { display: flex; justify-content: flex-end; gap: 5px; height: 12px; margin-bottom: 2px; }
    .icon { font-size: 10px; font-weight: bold; }

    /* D-PAD (Classic Plus) */
    .dpad { position: absolute; bottom: 130px; left: 30px; width: 90px; height: 90px; }
    .dp-btn { position: absolute; background: #262626; border: 2px solid #000; color: #444; display: flex; align-items: center; justify-content: center; cursor: pointer; }
    .dp-up { width: 30px; height: 30px; left: 30px; top: 0; border-radius: 4px 4px 0 0; }
    .dp-down { width: 30px; height: 30px; left: 30px; top: 60px; border-radius: 0 0 4px 4px; }
    .dp-left { width: 30px; height: 30px; left: 0; top: 30px; border-radius: 4px 0 0 4px; }
    .dp-right { width: 30px; height: 30px; left: 60px; top: 30px; border-radius: 0 4px 4px 0; }
    .dp-mid { width: 30px; height: 30px; left: 30px; top: 30px; background: #262626; border: none; }

    /* A/B Buttons (Circular) */
    .btn-a, .btn-b {
        position: absolute; width: 55px; height: 55px;
        border-radius: 50%; background: #8b0000; border: 3px solid #580000;
        color: rgba(255,255,255,0.5); font-weight: bold; display: flex; align-items: center; justify-content: center;
        box-shadow: 2px 2px 0px #000; cursor: pointer;
    }
    .btn-b { bottom: 170px; right: 85px; }
    .btn-a { bottom: 140px; right: 20px; }

    /* Select/Start (Rubber Pills) */
    .pill {
        position: absolute; bottom: 55px; width: 50px; height: 12px;
        background: #71717a; border-radius: 10px; transform: rotate(-25deg);
        border: 2px solid #3f3f46; cursor: pointer; box-shadow: 2px 2px 0px #9ca3af;
    }
    .p-select { left: 100px; }
    .p-start { left: 170px; }
    .pill-label { position: absolute; font-size: 9px; color: #555; bottom: 35px; font-weight: bold; }
</style>

<div class="chassis">
    <div class="screen-bezel">
        <div class="screen" id="display">
            BOOTING...
        </div>
    </div>

    <div class="dpad">
        <div class="dp-btn dp-up" onclick="nav(-1)">▲</div>
        <div class="dp-btn dp-mid"></div>
        <div class="dp-btn dp-down" onclick="nav(1)">▼</div>
        <div class="dp-btn dp-left"></div>
        <div class="dp-btn dp-right"></div>
    </div>

    <div class="btn-b" onclick="goHome()">B</div>
    <div class="btn-a" onclick="confirm()">A</div>

    <div class="pill p-select" onclick="goHome()"></div>
    <div class="pill-label" style="left:100px;">SELECT</div>
    <div class="pill p-start" onclick="advanceTime()"></div>
    <div class="pill-label" style="left:175px;">START</div>
</div>

<script>
    let menu = ["MESSAGES", "WAP NEWS", "PRACTICE", "SCHEDULE", "MUZTRIS"];
    let cursor = 0;
    let page = "HOME";
    let hours = 0;
    let day = 1;
    
    // Game State
    let hasDashChallenge = false;
    let unreadMsgs = true;
    let taskAlert = false;

    function render() {
        const display = document.getElementById('display');
        let header = `<div class="indicator-bar">
                        ${unreadMsgs ? '<span class="icon">✉</span>' : ''}
                        ${taskAlert ? '<span class="icon">!</span>' : ''}
                        <span style="flex-grow:1; font-size:9px;">D${day} ${hours.toString().padStart(2, '0')}:00</span>
                      </div>`;
        
        let body = "";

        if (page === "HOME") {
            // If dash is accepted, add to menu if not already there
            let activeMenu = [...menu];
            if (hasDashChallenge) activeMenu.push("BACKLINE DASH");
            
            activeMenu.forEach((item, i) => {
                let cls = (i === cursor) ? "class='selected'" : "";
                body += `<div ${cls} style="font-size:12px; font-weight:bold;">${(i===cursor ? "▶ " : "  ") + item}</div>`;
            });
        } else if (page === "MESSAGES") {
            body = "<b>INBOX</b><hr><small><b>B.LIGHTS:</b> Gear is packed. Challenge Powertool?</small><br><br><small onclick='unlockDash()'>[ACCEPT CHALLENGE]</small>";
        } else if (page === "WAP NEWS") {
            body = "<b>WAP BROWSER</b><hr><small>UK: MUZ-BIT console sells out!</small><br><small>NZ: Bengal Lights #1</small>";
        } else if (page === "PRACTICE") {
            body = "<b>PRACTICE</b><hr><small>1. REHEARSE (+5 Skill)</small><br><small>2. REST (-10 Ego)</small><br><small>3. MOCK SOUNDCHECK</small>";
        } else if (page === "SCHEDULE") {
            body = "<b>SCHEDULE</b><hr><small>FRI: Whammy (Gig)</small><br><small>SAT: bFM Interview</small><br><small>SUN: Record Pressing</small>";
        } else if (page === "MUZTRIS") {
            body = "<div style='text-align:center;'><br><b>MUZTRIS</b><br>---<br># # # #<br>  # #<br>  # #</div>";
        } else if (page === "BACKLINE DASH") {
            body = "<b>TIGER DASH</b><hr><div style='font-size:20px; text-align:center;'><br>🚐 .. 🔊 .. ⚡</div>";
        }

        display.innerHTML = header + body;
    }

    function nav(dir) {
        let activeMenu = [...menu];
        if (hasDashChallenge) activeMenu.push("BACKLINE DASH");
        cursor = (cursor + dir + activeMenu.length) % activeMenu.length;
        render();
    }

    function confirm() {
        let activeMenu = [...menu];
        if (hasDashChallenge) activeMenu.push("BACKLINE DASH");
        page = activeMenu[cursor];
        if (page === "MESSAGES") unreadMsgs = false;
        render();
    }

    function goHome() { page = "HOME"; render(); }

    function advanceTime() {
        hours = (hours + 2) % 24;
        if (hours === 0) day++;
        taskAlert = (hours === 10); // Simulated task at 10am
        render();
    }

    function unlockDash() {
        hasDashChallenge = true;
        taskAlert = true;
        alert("CHALLENGE ACCEPTED: TIGER DASH UNLOCKED");
        goHome();
    }

    render();
</script>
"""

# Render the component
components.html(handheld_html, height=620)
