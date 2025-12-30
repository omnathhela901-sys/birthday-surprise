#/////////////////////........PAGE 1........\\\\\\\\\\\\\\\\\\

import streamlit as st
import base64
import os

#-----------------PAGE ICON------------------
st.set_page_config(page_title="Birthday surprise",page_icon="🎉",layout="wide")
# ---- HIDE SIDEBAR & STREAMLIT NAVIGATION ----
hide_sidebar_style = """
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)
remove_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    padding: 0 !important;
    margin: 0 !important;
}

.main .block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}
iframe {
    border: none !important;
}
</style>
"""

st.markdown(remove_streamlit_style, unsafe_allow_html=True)

#----------HEART AND BALLOON FALLING ANIMATION--------
hearts_css = """
<style>
@keyframes heartFall {
  0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
  100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
}
.heart-container {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 999;
}
.heart {
  position: absolute;
  width: 20px;
  height: 20px;
  background-color: red;
  transform: rotate(45deg);
  animation: heartFall linear infinite;
  opacity: 0.9;
}
/* Heart shape using pseudo elements */
.heart:before,
.heart:after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  background-color: red;
  border-radius: 50%;
}
.heart:before {
  top: -10px;
  left: 0;
}
.heart:after {
  left: -10px;
  top: 0;
}
/* Multiple hearts with random positions & speeds */
.heart:nth-child(1) { left: 10%; animation-duration: 6s; animation-delay: 0s; }
.heart:nth-child(2) { left: 20%; animation-duration: 5s; animation-delay: 1s; }
.heart:nth-child(3) { left: 30%; animation-duration: 7s; animation-delay: 0.5s; }
.heart:nth-child(4) { left: 40%; animation-duration: 6.5s; animation-delay: 1s; }
.heart:nth-child(5) { left: 50%; animation-duration: 8s; animation-delay: 0.2s; }
.heart:nth-child(6) { left: 60%; animation-duration: 5.3s; animation-delay: 1.2s; }
.heart:nth-child(7) { left: 70%; animation-duration: 7.4s; animation-delay: 0.6s; }
.heart:nth-child(8) { left: 80%; animation-duration: 6.1s; animation-delay: 0.1s; }
.heart:nth-child(9) { left: 90%; animation-duration: 5.7s; animation-delay: 1.1s; }
.heart:nth-child(10) { left: 95%; animation-duration: 7.3s; animation-delay: 0.3s; }
</style>
<div class="heart-container">
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
</div>
"""
st.markdown(hearts_css, unsafe_allow_html=True)

combo_css = """
<style>
/* ========================== */
/*        BALLOONS           */
/* ========================== */
@keyframes balloonFloat {
  0% { transform: translateY(100vh) scale(1); opacity: 1; }
  100% { transform: translateY(-20vh) scale(1.1); opacity: 0; }
}
.balloon-layer {
  position: fixed;
  left: 0; top: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 900;
}
.balloon {
  position: absolute;
  width: 50px;
  height: 70px;
  background: #ff77c6;
  border-radius: 50%;
  animation: balloonFloat linear infinite;
  opacity: 0.85;
}
.balloon:after {
  content: '';
  position: absolute;
  width: 2px;
  height: 60px;
  background: #444;
  left: 50%;
  top: 70px;
}
/* balloon positions */
.balloon:nth-child(1) { left: 10%; animation-duration: 8s; }
.balloon:nth-child(2) { left: 25%; animation-duration: 9s; }
.balloon:nth-child(3) { left: 40%; animation-duration: 7.5s; }
.balloon:nth-child(4) { left: 65%; animation-duration: 10s; }
.balloon:nth-child(5) { left: 85%; animation-duration: 8.5s; }
/* ========================== */
/*       FALLING HEARTS       */
/* ========================== */
@keyframes heartFall {
  0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
  100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
}
.heart-layer {
  position: fixed;
  left: 0; top: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 950;
}
.heart {
  position: absolute;
  width: 20px;
  height: 20px;
  background: #ff4da6;
  transform: rotate(45deg);
  animation: heartFall linear infinite;
  opacity: 0.9;
}
.heart:before,
.heart:after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  background: #ff4da6;
  border-radius: 50%;
}
.heart:before { top: -10px; left: 0; }
.heart:after { left: -10px; top: 0; }

/* heart positions */
.heart:nth-child(1) { left: 12%; animation-duration: 6s; animation-delay: 0s; }
.heart:nth-child(2) { left: 28%; animation-duration: 7s; animation-delay: 1s; }
.heart:nth-child(3) { left: 45%; animation-duration: 6.5s; animation-delay: 0.5s; }
.heart:nth-child(4) { left: 62%; animation-duration: 8s; animation-delay: 0.8s; }
.heart:nth-child(5) { left: 80%; animation-duration: 7.2s; animation-delay: 0.3s; }

/* ========================== */
/*      PINK GLITTER FALL     */
/* ========================== */
@keyframes glitterFall {
  0% { transform: translateY(-10vh) scale(1); opacity: 1; }
  100% { transform: translateY(110vh) scale(0.5); opacity: 0; }
}

.glitter-layer {
  position: fixed;
  left: 0; top: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 980;
}

.glitter {
  position: absolute;
  width: 8px;
  height: 8px;
  background: radial-gradient(circle, #ffffff, #ff99e9);
  border-radius: 50%;
  animation: glitterFall linear infinite;
  opacity: 0.8;
}

/* glitter positions */
.glitter:nth-child(1) { left: 15%; animation-duration: 5s; animation-delay: 0s; }
.glitter:nth-child(2) { left: 30%; animation-duration: 4s; animation-delay: 1s; }
.glitter:nth-child(3) { left: 50%; animation-duration: 6s; animation-delay: 0.3s; }
.glitter:nth-child(4) { left: 70%; animation-duration: 5.5s; animation-delay: 0.7s; }
.glitter:nth-child(5) { left: 85%; animation-duration: 4.3s; animation-delay: 1s; }

</style>

<!-- layers -->
<div class="balloon-layer">
  <div class="balloon"></div>
  <div class="balloon"></div>
  <div class="balloon"></div>
  <div class="balloon"></div>
  <div class="balloon"></div>
</div>

<div class="heart-layer">
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
</div>

<div class="glitter-layer">
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
</div>

"""

st.markdown(combo_css, unsafe_allow_html=True)

#--------FALLING GLITTER EFFECT-------

glitter_css = """
<style>
@keyframes fall {
  0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
  100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
}

.glitter-container {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 999;
}

.glitter {
  position: absolute;
  width: 8px;
  height: 8px;
  background: radial-gradient(circle, white, gold);
  border-radius: 50%;
  opacity: 0.9;
  animation: fall linear infinite;
}

/* Multiple glitters with random positions & speeds */
.glitter:nth-child(1) { left: 10%; animation-duration: 4s; animation-delay: 0s; }
.glitter:nth-child(2) { left: 20%; animation-duration: 5s; animation-delay: 1s; }
.glitter:nth-child(3) { left: 30%; animation-duration: 4.5s; animation-delay: 0.5s; }
.glitter:nth-child(4) { left: 40%; animation-duration: 6s; animation-delay: 1s; }
.glitter:nth-child(5) { left: 50%; animation-duration: 5.5s; animation-delay: 0.2s; }
.glitter:nth-child(6) { left: 60%; animation-duration: 4.8s; animation-delay: 1.2s; }
.glitter:nth-child(7) { left: 70%; animation-duration: 6.5s; animation-delay: 0.6s; }
.glitter:nth-child(8) { left: 80%; animation-duration: 5.2s; animation-delay: 0.1s; }
.glitter:nth-child(9) { left: 90%; animation-duration: 4.7s; animation-delay: 1.1s; }
.glitter:nth-child(10) { left: 95%; animation-duration: 6.1s; animation-delay: 0.3s; }
</style>

<div class="glitter-container">
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
  <div class="glitter"></div>
</div>
"""

st.markdown(glitter_css, unsafe_allow_html=True)


#-----------------BACKGROUND CHANGE------------

page_bg = """
<style>
/* App Background */
.stApp {
    background: linear-gradient(
        to bottom,
        #8B0000 0%,      /* Dark Red */
        #5B0000 40%,     /* Maroon */
        #000000 100%     /* Fading to Black */
    ) !important;
}

/* Sidebar Background (matching theme) */
[data-testid="stSidebar"] {
    background: linear-gradient(
        to bottom,
        #5B0000 0%,
        #3A0000 60%,
        #000000 100%
    ) !important;
}

/* Light text for readability */
html, body, [class*="css"] {
    color: #f8e6e6 !important;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Background (your dark red → maroon → black fade)
page_bg = """
<style>
.stApp {
    background: linear-gradient(
        to bottom,
        #8B0000 0%,
        #5B0000 40%,
        #000000 100%
    ) !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        to bottom,
        #5B0000 0%,
        #3A0000 60%,
        #000000 100%
    ) !important;
}

html, body, [class*="css"] {
    color: #f8e6e6 !important;
}

/* 🔥 Glowing Light Pink Title */
.glow-title {
    font-size: 110px;
    font-weight: 1100;
    text-align: center;
    margin-top: 30px;
    color: #ffb6d9; /* Light Pink */
    text-shadow:
        0 0 10px #ff8ac1,
        0 0 20px #ff84c0,
        0 0 40px #ff4fa4,
        0 0 80px #ff4fa4;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

#----------GLOWING TITLE-----------

st.markdown('<h1 class="glow-title">💗🎊HAPPY BIRTHDAY MY LOVEE🎊💗</h1>', unsafe_allow_html=True)

css_js = """
<style>

/* LEFT POPPER */
.party-popper-left {
    position: fixed;
    bottom: 20px;
    left: 20px;
    width: 60px;
    height: 60px;
    z-index: 9999;
}

.popper-emoji-left {
    font-size: 50px;
    transform: rotate(25deg);
}

/* RIGHT POPPER */
.party-popper-right {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    z-index: 9999;
}

.popper-emoji-right {
    font-size: 50px;
    transform: rotate(-25deg);
}

/* CONFETTI (shared style) */
.confetti {
    position: fixed;
    width: 8px;
    height: 15px;
    background: red;
    opacity: 0;
    animation: shoot 1.5s infinite;
    border-radius: 2px;
}

/* CONFETTI COLORS & OFFSETS */
.confetti:nth-child(2) { background: yellow; animation-delay: 0.2s; }
.confetti:nth-child(3) { background: cyan; animation-delay: 0.4s; }
.confetti:nth-child(4) { background: magenta; animation-delay: 0.6s; }
.confetti:nth-child(5) { background: orange; animation-delay: 0.8s; }
.confetti:nth-child(6) { background: lime; animation-delay: 1s; }

/* LEFT CONFETTI POSITIONS */
.left1 { bottom: 40px; left: 40px; }
.left2 { bottom: 40px; left: 60px; }
.left3 { bottom: 40px; left: 20px; }
.left4 { bottom: 40px; left: 80px; }
.left5 { bottom: 40px; left: 10px; }
.left6 { bottom: 40px; left: 50px; }

/* RIGHT CONFETTI POSITIONS */
.right1 { bottom: 40px; right: 40px; }
.right2 { bottom: 40px; right: 60px; }
.right3 { bottom: 40px; right: 20px; }
.right4 { bottom: 40px; right: 80px; }
.right5 { bottom: 40px; right: 10px; }
.right6 { bottom: 40px; right: 50px; }

/* FLYING ANIMATION */
@keyframes shoot {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }
    50% {
        opacity: 1;
    }
    100% {
        transform: translateY(-250px) rotate(360deg);
        opacity: 0;
    }
}

</style>

<script>
// Play sound on load
window.addEventListener('load', function() {
    const audio = new Audio("pop.mp3");
    audio.volume = 1.0;
    audio.play().catch(e => console.log("Autoplay blocked:", e));
});
</script>
"""

st.markdown(css_js, unsafe_allow_html=True)

# DOUBLE POPPERS (LEFT + RIGHT)
st.markdown("""
<!-- LEFT POPPER -->
<div class="party-popper-left">
    <div class="popper-emoji-left">🎉</div>
    <div class="confetti left1"></div>
    <div class="confetti left2"></div>
    <div class="confetti left3"></div>
    <div class="confetti left4"></div>
    <div class="confetti left5"></div>
    <div class="confetti left6"></div>
</div>

<!-- RIGHT POPPER -->
<div class="party-popper-right">
    <div class="popper-emoji-right">🎉</div>
    <div class="confetti right1"></div>
    <div class="confetti right2"></div>
    <div class="confetti right3"></div>
    <div class="confetti right4"></div>
    <div class="confetti right5"></div>
    <div class="confetti right6"></div>
</div>
""", unsafe_allow_html=True)


# --- Custom CSS for golden gradient + animated glow ---
st.markdown("""
<style>

@keyframes glowPulse {
    0% {
        text-shadow: 0 0 8px #ffdf00, 0 0 15px #ffdf00;
    }
    50% {
        text-shadow: 0 0 20px #ffcc00, 0 0 35px #ffcc00;
    }
    100% {
        text-shadow: 0 0 8px #ffdf00, 0 0 15px #ffdf00;
    }
}

.center-text {
    text-align: center;
    font-weight: 800;
    background: linear-gradient(90deg, #b8860b, #ffcc33, #b8860b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glowPulse 2s infinite ease-in-out;
    font-family: 'Helvetica', sans-serif;
}

.sub1 {
    font-size: 58px;  /* Larger font */
    margin-top: 10px;
}

.sub2 {
    font-size: 50px;  /* Slightly smaller */
    margin-top: -10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="center-text sub1"> °❀•°Wish you the very best to your life and become successful person°•❀°</p>', unsafe_allow_html=True)
st.markdown('<p class="center-text sub2">💗 A little surprise for my prettiest person 💗</p>', unsafe_allow_html=True)



# ---------- ADDING INBOX ----------
st.markdown(
    """
    <style>
    /* Center container */
    .center-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 60px;
    }

    /* Glowing subheader */
    .glow-subheader {
        font-size: 16px;
        font-weight: bold;
        color: #b6ffb6;
        text-align: center;
        text-shadow: 0 0 5px #66ff66,
                     0 0 10px #66ff66,
                     0 0 20px #33cc33,
                     0 0 40px #33cc33;
        margin-bottom: 13px;
    }

    /* Neon input box */
    .neon-input input {
        width: 320px !important;
        padding: 15px !important;
        font-size: 20px !important;
        text-align: center !important;
        border-radius: 15px !important;
        border: 2px solid #ff4d4d !important;
        background: #1a0000 !important;
        color: white !important;
        box-shadow: 0 0 5px #ff4d4d,
                     0 0 15px #ff4d4d,
                     0 0 30px #ff1a1a,
                     0 0 60px #ff1a1a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- CENTER CONTENT ----------
st.markdown('<div class="center-wrapper">', unsafe_allow_html=True)

st.markdown(
    '<div class="glow-subheader">༺♡༻ENTER SECRET CODE TO GET SURPRISE༺♡༻</div>',
    unsafe_allow_html=True
)

# Input with neon style
secret_code = st.text_input("", type="password", key="secret", placeholder="Enter secret code", label_visibility="collapsed")

st.markdown('</div>', unsafe_allow_html=True)

# Apply neon class to input
st.markdown(
    """
    <script>
    const input = window.parent.document.querySelector('input');
    if (input) {
        input.parentElement.classList.add('neon-input');
    }
    </script>
    """,
    unsafe_allow_html=True
)

# ---------- CONDITION FOR NEXT PAGE ----------
CORRECT_CODE = "16 jan 2024"

if secret_code:
    if secret_code == CORRECT_CODE:
        st.success("✅ Code correct n♡iceee maam")
        st.switch_page("pages/secondpage.py")

    else:
        st.error("❌ Wrong code! kyy goluu♡♡")

st.markdown("""
<style>
.glow-hint {
    background: #1a1a1a;
    color: #00ffcc;
    padding: 15px 20px;
    border-radius: 12px;
    margin-top: 10px;
    border: 2px solid #00ffcc;
    box-shadow: 0 0 5px #00ffcc,
                0 0 15px #00ffcc,
                0 0 30px #00ffcc;
    font-size: 18px;
    text-align: center;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Checkbox to show hint
show_hint = st.checkbox("༺Sh♡w Hinttt!༻💡")

if show_hint:
    st.markdown(
        '<div class="glow-hint">Hint:♡✾The day uuu accepted mee✾♡.</div>',
        unsafe_allow_html=True
    )
        




