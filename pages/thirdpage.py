import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(page_title="Birthday surprise",page_icon="🎉", layout="wide")
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

#------BACKGROUND AND TITLE AND BG MUSIC



title_html = """
<style>
/* TITLE */
.magic-title {
    position: relative;
    font-family: "Copperplate", "Copperplate Gothic Light", fantasy;
    text-align: center;
    margin-top: 40px;
    font-size: 52px;
    font-weight: 700;

    background: linear-gradient(90deg, #ff8ccf, #ff2b2b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 12px rgba(255, 100, 150, 0.7),
        0 0 25px rgba(255, 40, 40, 0.6),
        0 0 45px rgba(255, 0, 0, 0.4);
}



@keyframes shine {
    0% { left: -120%; }
    50% { left: 120%; }
    100% { left: 120%; }
}

/* SPARKLES */
.sparkle {
    position: absolute;
    width: 6px;
    height: 6px;
    background: radial-gradient(circle, #fff, rgba(255,255,255,0));
    border-radius: 50%;
    animation: floatSparkle linear infinite;
    opacity: 0.8;
}

@keyframes floatSparkle {
    from {
        transform: translateY(0) scale(1);
        opacity: 1;
    }
    to {
        transform: translateY(-60px) scale(0);
        opacity: 0;
    }
}

/* SPARKLE CONTAINER */
.sparkle-wrap {
    position: relative;
    display: inline-block;
}
</style>

<div style="text-align:center;">
    <div class="sparkle-wrap">
        <div class="magic-title">💗MEM♡RIES W♡VEN WITH L♡VES AND TIME💗</div>

        <!-- SPARKLES -->
        <div class="sparkle" style="left:5%; bottom:-10px; animation-duration:3s;"></div>
        <div class="sparkle" style="left:25%; bottom:-10px; animation-duration:4s;"></div>
        <div class="sparkle" style="left:50%; bottom:-10px; animation-duration:3.5s;"></div>
        <div class="sparkle" style="left:75%; bottom:-10px; animation-duration:4.2s;"></div>
        <div class="sparkle" style="left:90%; bottom:-10px; animation-duration:3.8s;"></div>
    </div>
</div>
"""

components.html(title_html, height=200)

st.markdown("""
<style>

.glow-msg {
    text-align: center;
    font-size: 60px;   /* Exactly 60px as you requested */
    font-weight: 700;
    color: #c25555;  /* Light maroon */
    animation: bounceGlow 2s infinite;
    margin-top: -5px;
    margin-bottom: 30px;

    text-shadow: 
        0 0 14px rgba(194, 85, 85, 0.8),
        0 0 28px rgba(194, 85, 85, 0.6),
        0 0 38px rgba(194, 85, 85, 0.4);
}

/* Bouncing Animation */
@keyframes bounceGlow {
    0% {
        transform: translateY(0);
        text-shadow: 
            0 0 12px rgba(194, 85, 85, 0.7),
            0 0 24px rgba(194, 85, 85, 0.5);
    }
    50% {
        transform: translateY(-16px);
        text-shadow: 
            0 0 22px rgba(194, 85, 85, 1),
            0 0 40px rgba(194, 85, 85, 0.8),
            0 0 60px rgba(194, 85, 85, 0.6);
    }
    100% {
        transform: translateY(0);
        text-shadow: 
            0 0 12px rgba(194, 85, 85, 0.7),
            0 0 24px rgba(194, 85, 85, 0.5);
    }
}

</style>

<p class="glow-msg"> 
<br>
💗A BUNDLES ♡F MEM♡RIES ♡F ♡URS PRICELESS M♡MENTS💗<br>
SOCHE KUCH ALAG KARE WAISE TOH HUMLOG KA ITNA PHOTOS NHI HA<br> 
PER FIR BHI JITNA HUMARELIYE BAHUT JADA...HAR WO EK LAMHA TUMHARE SATH <br>
<br>✨🎀BEF♡RE TURNING CARDS CLICK THE HEART🎀✨<br>
</p>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at top, rgba(150,100,255,0.38), transparent 55%),
        radial-gradient(circle at top left, rgba(255,120,200,0.22), transparent 60%),
        linear-gradient(
            to bottom,
            #2d004a 0%,
            #1a002e 18%,
            #0d0016 35%,
            #050008 60%,
            #000000 100%
        );
    animation: glow 18s ease-in-out infinite alternate;
    overflow: hidden;
}

/* Remove Streamlit white */
[data-testid="stHeader"],
[data-testid="stToolbar"] {
    background: transparent;
}

/* GLOW BREATHING */
@keyframes glow {
    from { filter: brightness(1); }
    to { filter: brightness(1.15); }
}

/* STARS */
.star {
    position: fixed;
    width: 2px;
    height: 2px;
    background: white;
    border-radius: 50%;
    opacity: 0.85;
    animation: twinkle 3.5s infinite ease-in-out;
}

@keyframes twinkle {
    0%, 100% { opacity: 0.2; }
    50% { opacity: 1; }
}

/* PARTICLES */
.particle {
    position: fixed;
    width: 4px;
    height: 4px;
    background: rgba(200,170,255,0.65);
    border-radius: 50%;
    filter: blur(1px);
    animation: floatUp 14s linear infinite;
}

@keyframes floatUp {
    0% {
        transform: translateY(120vh) translateX(0);
        opacity: 0;
    }
    30% { opacity: 1; }
    100% {
        transform: translateY(-30vh) translateX(70px);
        opacity: 0;
    }
}

</style>

<!-- STARS -->
<div class="star" style="top:10%; left:18%; animation-delay:0s;"></div>
<div class="star" style="top:20%; left:42%; animation-delay:1s;"></div>
<div class="star" style="top:14%; left:68%; animation-delay:2s;"></div>
<div class="star" style="top:32%; left:55%; animation-delay:1.4s;"></div>
<div class="star" style="top:48%; left:30%; animation-delay:2.4s;"></div>
<div class="star" style="top:65%; left:80%; animation-delay:0.7s;"></div>

<!-- PARTICLES -->
<div class="particle" style="left:15%; animation-delay:0s;"></div>
<div class="particle" style="left:35%; animation-delay:2s;"></div>
<div class="particle" style="left:55%; animation-delay:4s;"></div>
<div class="particle" style="left:75%; animation-delay:1s;"></div>
<div class="particle" style="left:90%; animation-delay:3s;"></div>

""", unsafe_allow_html=True)

st.markdown("""
<style>

/* HEART SHAPE */
.heart {
    position: fixed;
    top: -10vh;
    width: 18px;
    height: 18px;
    background: rgba(255, 120, 200, 0.85);
    transform: rotate(45deg);
    animation: fallHeart 14s linear infinite;
    filter: drop-shadow(0 0 6px rgba(255,120,200,0.8))
            drop-shadow(0 0 14px rgba(255,120,200,0.6));
    pointer-events: none;
}

/* HEART CIRCLES */
.heart::before,
.heart::after {
    content: "";
    position: absolute;
    width: 18px;
    height: 18px;
    background: rgba(255, 120, 200, 0.85);
    border-radius: 50%;
}

.heart::before {
    top: -9px;
    left: 0;
}

.heart::after {
    left: -9px;
    top: 0;
}

/* FALLING ANIMATION */
@keyframes fallHeart {
    0% {
        transform: translateY(0) translateX(0) rotate(45deg);
        opacity: 0;
    }
    15% { opacity: 1; }
    100% {
        transform: translateY(120vh) translateX(60px) rotate(45deg);
        opacity: 0;
    }
}

</style>

<!-- FALLING HEARTS -->
<div class="heart" style="left:10%; animation-delay:0s;"></div>
<div class="heart" style="left:22%; animation-delay:3s;"></div>
<div class="heart" style="left:35%; animation-delay:6s;"></div>
<div class="heart" style="left:48%; animation-delay:1s;"></div>
<div class="heart" style="left:62%; animation-delay:4s;"></div>
<div class="heart" style="left:75%; animation-delay:7s;"></div>
<div class="heart" style="left:88%; animation-delay:2s;"></div>

""", unsafe_allow_html=True)



# Load music
music_path = "assets/music/bgmusic.mp3"
with open(music_path, "rb") as f:
    audio_bytes = f.read()

audio_base64 = base64.b64encode(audio_bytes).decode()

html_code = f"""
<style>
.heart-btn {{
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 45px;
    height: 45px;
    background: pink;
    transform: rotate(45deg);
    cursor: pointer;
    z-index: 9999;
    box-shadow: 0 0 10px red, 0 0 20px crimson;
    animation: pulse 1.4s infinite;
    display: flex;
    align-items: center;
    justify-content: center;
}}

/* HEART SHAPE CIRCLES */
.heart-btn::before,
.heart-btn::after {{
    content: "";
    position: absolute;
    width: 45px;
    height: 45px;
    background: pink;
    border-radius: 50%;
    z-index: 1;   /* ✅ FIX */
}}

.heart-btn::before {{
    top: -22px;
    left: 0;
}}

.heart-btn::after {{
    left: -22px;
    top: 0;
}}

/* HEART TEXT */
.heart-text {{
    position: absolute;
    transform: rotate(-45deg);
    color: red;
    font-size: 9px;
    font-weight: bold;
    text-shadow: 0 0 5px red;
    pointer-events: none;
    z-index: 5;   /* ✅ FIX */
}}

@keyframes pulse {{
    0% {{ transform: rotate(45deg) scale(1); }}
    50% {{ transform: rotate(45deg) scale(1.1); }}
    100% {{ transform: rotate(45deg) scale(1); }}
}}

.fade-out {{
    animation: fade 0.6s forwards;
}}

@keyframes fade {{
    to {{
        opacity: 0;
        transform: scale(0);
    }}
}}
</style>

<audio id="bgMusic" loop>
    <source src="data:audio/mp3;base64,{audio_base64}">
</audio>

<div class="heart-btn" id="heartBtn" onclick="playMusic()">
    <div class="heart-text">CLICK ME</div>
</div>

<script>
function playMusic() {{
    const music = document.getElementById("bgMusic");
    const btn = document.getElementById("heartBtn");

    music.volume = 0.4;
    music.play();

    btn.classList.add("fade-out");
    setTimeout(() => btn.style.display = "none", 600);
}}
</script>
"""

components.html(html_code, height=130)


def img_to_base64(img_path):
    data = Path(img_path).read_bytes()
    return f"data:image/jpg;base64,{base64.b64encode(data).decode()}"
st.set_page_config(page_title="Birthday surprise",page_icon="🎉", layout="wide")

titles = [
    "A Little Secret",
    "♡pen Gently",
    "Just F♡r Y♡u",
    "S♡mething Special",
    "Fr♡m My Heart",
    "A Quiet M♡ment",
    "Tap With L♡ve",
    "A S♡ft Mem♡ry",
    "♡nly F♡r Y♡u",
    "F♡rever ♡urs"
]

html_code = """
<style>

/* CARD ENTRANCE ANIMATION */
@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(30px) scale(0.96);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.card {
    opacity: 0;
    animation: fadeUp 0.8s ease forwards;
}

/* FLOATING HEARTS BACKGROUND */
.floating-hearts {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
}

.floating-heart {
    position: absolute;
    top: -20px;
    width: 10px;
    height: 10px;
    background: #ff3b3b;
    transform: rotate(45deg);
    opacity: 0.85;
    animation: floatDown linear infinite;
    box-shadow: 0 0 8px rgba(255, 60, 60, 0.9);
}

.floating-heart::before,
.floating-heart::after {
    content: "";
    position: absolute;
    width: 10px;
    height: 10px;
    background: #ff3b3b;
    border-radius: 50%;
}

.floating-heart::before { top: -5px; left: 0; }
.floating-heart::after { left: -5px; top: 0; }

@keyframes floatDown {
    from { transform: translateY(-20px) rotate(45deg); opacity: 1; }
    to { transform: translateY(110vh) rotate(45deg); opacity: 0; }
}

/* CONTAINER */
.container {
    display: flex;
    padding-bottom: 80px;
    justify-content: center;
    gap: 25px;
    margin-top: 40px;
    flex-wrap: wrap;
    position: relative;
    z-index: 1;
}

/* CARD */
.card {
    width: 230px;
    animation:
        fadeUp 0.8s ease forwards,
        heartBeatGlow 2.6s ease-in-out infinite;

    height: 330px;
    border-radius: 22px;
    background: linear-gradient(145deg, #e88abf, #d85a9e, #c83c87);
    position: relative;
    perspective: 1000px;
    box-shadow: 0 0 22px rgba(216, 90, 158, 0.75);
}

/* INNER FLIP */
.inner-card {
    width: 100%;
    height: 100%;
    position: relative;
    transition: transform 0.9s ease;
    transform-style: preserve-3d;
    cursor: pointer;
}

.inner-card.flipped {
    transform: rotateY(180deg);
}

/* FRONT & BACK */
.front, .back {
    position: absolute;
    inset: 0;
    backface-visibility: hidden;
    border-radius: 22px;
    overflow: hidden;
}

.front {
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: Copperplate, fantasy;
    font-size: 20px;
    color: white;
}

.back {
    transform: rotateY(180deg);
    display: flex;
    flex-direction: column;
}


@keyframes heartBeatGlow {
    0% {
        box-shadow:
            0 0 12px rgba(255, 80, 150, 0.4),
            0 0 22px rgba(255, 50, 120, 0.3);
        transform: scale(1);
    }
    25% {
        box-shadow:
            0 0 18px rgba(255, 90, 170, 0.7),
            0 0 36px rgba(255, 60, 140, 0.6);
        transform: scale(1.02);
    }
    40% {
        box-shadow:
            0 0 12px rgba(255, 80, 150, 0.4),
            0 0 22px rgba(255, 50, 120, 0.3);
        transform: scale(1);
    }
    100% {
        box-shadow:
            0 0 12px rgba(255, 80, 150, 0.4),
            0 0 22px rgba(255, 50, 120, 0.3);
        transform: scale(1);
    }
}


.back img {
    width: 100%;
    height:auto;
    max-height: 68%;
    object-fit: contain;
    background:#000;
    
    image-rendering:auto;
    image-rendering:crisp-edges;
    image-rendering:high-quality;
    
    border-radius:18px 18px 0 0;
    border-bottom:1px solid rgba(255,255,255,0.3);
    filter:contrast(1.05) saturate(1.05);
    
}

/* MESSAGE */
.message {
    height: 30%;
    mini-height:25%;
    line-height:1.4;
    font-variant:small-caps;
    overflow:visible
    world-wrap:break-word;
    background: linear-gradient(135deg, #ffd1dc, #ffb3c7);
    padding: 12px 14px;
    text-align: center;
    font-family: Georgia, serif;
    font-size: 15px;
    color: #ff1f1f;
    display: flex;
    align-items: center;
    justify-content: center;
    text-shadow: 0 0 6px rgba(255, 50, 50, 0.8),
                 0 0 12px rgba(255, 30, 30, 0.6);
}

</style>

<!-- FLOATING HEARTS -->
<div class="floating-hearts">
    <div class="floating-heart" style="left:10%; animation-duration:7s;"></div>
    <div class="floating-heart" style="left:30%; animation-duration:9s;"></div>
    <div class="floating-heart" style="left:50%; animation-duration:8s;"></div>
    <div class="floating-heart" style="left:70%; animation-duration:10s;"></div>
    <div class="floating-heart" style="left:90%; animation-duration:7.5s;"></div>
</div>

<div class="container">
"""

memories = [
    ("assets/images/memory1.jpg", "That unf♡rgettable m♡ment ♡ur first selfie😌."),
    ("assets/images/memory2.jpg", "the m♡st perfect picture f♡r me🥰."),
    ("assets/images/memory3.jpg", "h♡lding hands and enj♡ying m♡rning view and g♡ssips🤭."),
    ("assets/images/memory4.jpg", "♡ur first sc♡♡ty ride...best feeling ever next time i'll drive😎."),
    ("assets/images/memory5.jpg", "sh♡pping t♡gether-aap kapde dekhrehe the me apk♡😳"),
    ("assets/images/memory6.jpg", "M♡ments that still warm the heart..r♡mance in d♡min♡s😚"),
    ("assets/images/memory7.jpg", "setting t♡gether n♡ talks ♡nly eye c♡ntact😍."),
    ("assets/images/memory8.jpg", "playing h♡liii together🥳."),
    ("assets/images/memory9.jpg", "playing badmint♡n every m♡rning best mem♡ry😄."),
    ("assets/images/memory10.jpg", "eating burger with♡ut patties if y♡u kn♡w y♡u kn♡w😝.")
]

for i, (img, text) in enumerate(memories):
    html_code += f"""
    <div class="card" style="animation-delay:{i * 0.12}s;">
        <div class="inner-card">
            <div class="front">{titles[i]}</div>
            <div class="back">
                <img src="{img_to_base64(img)}">
                <div class="message">{text}</div>
            </div>
        </div>
    </div>
    """

html_code += """
</div>

<!-- STEP 3: CLICK FLIP SCRIPT -->
<script>
document.querySelectorAll('.inner-card').forEach(card => {
    card.addEventListener('click', () => {
        card.classList.toggle('flipped');
    });
});
</script>
"""

components.html(html_code, height=1500, scrolling=False)


def beautiful_envelope(poetry_text):
    envelope_html = f"""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Playfair+Display:ital,wght@1,500&display=swap');

    .container {{
      height: 900px; 
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: visible;
    }}

    /* Main Envelope Body */
    .envelope {{
      position: relative;
      width: 450px;
      height: 300px;
      background: linear-gradient(135deg, #e0aaff 0%, #ff99c8 100%);
      box-shadow: 0 0 20px rgba(255, 153, 200, 0.5);
      cursor: pointer;
      transition: all 0.5s ease;
      animation: pulse-glow 2s infinite ease-in-out;
      z-index: 1;
    }}

    @keyframes pulse-glow {{
      0% {{ box-shadow: 0 0 15px rgba(255, 153, 200, 0.4); }}
      50% {{ box-shadow: 0 0 35px rgba(255, 153, 200, 0.8); }}
      100% {{ box-shadow: 0 0 15px rgba(255, 153, 200, 0.4); }}
    }}

    .envelope:before {{
      content: "";
      position: absolute;
      z-index: 10;
      border-top: 150px solid transparent;
      border-right: 225px solid #f2d5f8;
      border-bottom: 150px solid #f2d5f8;
      border-left: 225px solid transparent;
      top: 0;
    }}

    .envelope:after {{
      content: "";
      position: absolute;
      z-index: 10;
      border-top: 150px solid transparent;
      border-right: transparent;
      border-bottom: 150px solid #e7c6ff;
      border-left: 225px solid #e7c6ff;
      top: 0;
    }}

    .flap {{
      position: absolute;
      top: 0;
      width: 0;
      height: 0;
      border-left: 225px solid transparent;
      border-right: 225px solid transparent;
      border-top: 160px solid #d896ff;
      transform-origin: top;
      transition: transform 0.6s ease;
      z-index: 11;
    }}

    .seal {{
      position: absolute;
      top: 140px;
      left: 200px;
      width: 50px;
      height: 50px;
      background: #9d4edd;
      border-radius: 50%;
      z-index: 12;
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
      font-size: 24px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.3);
      transition: opacity 0.4s;
    }}
    .seal:after {{ content: "❤"; }}

    /* ADJUSTED: Dark Pink Background and Smaller Text */
    .letter {{
      position: absolute;
      bottom: 10px;
      left: 25px;
      width: 400px;
      height: 250px;
      background: #ff4d6d; /* Dark Pink Background */
      padding: 30px;
      box-sizing: border-box;
      transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 5;
      font-family: 'Dancing Script', cursive;
      text-align: center;
      font-size: 1.2rem; /* Decreased size */
      line-height: 1.4;
      color: #ffffff; /* White text for better contrast on dark pink */
      box-shadow: inset 0 0 50px rgba(0,0,0,0.2);
      border: 1px solid #ff758f;
      overflow: hidden;
    }}

    .open .flap {{
      transform: rotateX(180deg);
      z-index: 1;
    }}

    .open .seal {{
      opacity: 0;
      pointer-events: none;
    }}

    .letter-out .letter {{
      transform: translateY(-150px) scale(1.1);
      height: 580px; 
      z-index: 100;
      box-shadow: 0 20px 50px rgba(0,0,0,0.4);
    }}

    /* ADJUSTED: Falling Hearts are now RED */
    .heart {{
      position: absolute;
      color: #ff0000; /* Vibrant Red */
      font-size: 18px;
      top: -20px;
      z-index: 101;
      user-select: none;
      pointer-events: none;
      animation: fall linear forwards;
    }}

    @keyframes fall {{
      to {{
        transform: translateY(650px) rotate(360deg);
      }}
    }}
    </style>

    <div class="container">
      <div id="env" class="envelope" onclick="nextStep()">
        <div class="flap"></div>
        <div class="seal"></div>
        <div id="letter-box" class="letter">
          <div style="border: 2px solid rgba(255,255,255,0.3); padding: 20px; height: 100%; display: flex; align-items: center; justify-content: center; flex-direction: column; position: relative;">
            {poetry_text}
          </div>
        </div>
      </div>
    </div>

    <script>
    let step = 0;

    function createHeart() {{
        const letterBox = document.getElementById('letter-box');
        const heart = document.createElement('div');
        heart.classList.add('heart');
        heart.innerHTML = '❤';
        heart.style.left = Math.random() * 100 + '%';
        heart.style.animationDuration = (Math.random() * 3 + 2) + 's';
        heart.style.opacity = (Math.random() * 0.5) + 0.5;
        letterBox.appendChild(heart);

        setTimeout(() => {{ heart.remove(); }}, 5000);
    }}

    function nextStep() {{
      const env = document.getElementById('env');
      if (step === 0) {{
        env.classList.add('open');
        step = 1;
      }} else if (step === 1) {{
        env.classList.add('letter-out');
        step = 2;

        setInterval(createHeart, 250);

        confetti({{
          particleCount: 150,
          spread: 70,
          origin: {{ y: 0.6 }},
          colors: ['#ff0000', '#ff4d6d', '#ffffff']
        }});
      }}
    }}
    </script>
    """
    components.html(envelope_html, height=1000)


# --- App Execution ---

poetry = """
ADMIRING THE BEAUTY-I<br>
Ha rehte ha tumhare akho k khayal me<br>
tumhe yaad krte ha chand ko nihaar ke<br>
gujar jati ha raatiya tumhaari hi yaad me<br>
Ek sawal gunjh jati ha pyari si awaj m<br>
Thakte nhi ho hume yuhi nihar ke<br>
hum sochte ha jis akho ne khushiyaan dikhyi usse thak jye toh mohabbat ky ha<br>
tumhe batorle apne bahome ye lamha yuhin tham jye isme harzz hi ky ha.<br>
<br>----YOUR LOVELY PERSON
"""

beautiful_envelope(poetry)


def beautiful_envelope(poetry_text):
    envelope_html = f"""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Playfair+Display:ital,wght@1,500&display=swap');

    .container {{
      height: 900px; 
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: visible;
    }}

    /* Main Envelope Body */
    .envelope {{
      position: relative;
      width: 450px;
      height: 300px;
      background: linear-gradient(135deg, #e0aaff 0%, #ff99c8 100%);
      box-shadow: 0 0 20px rgba(255, 153, 200, 0.5);
      cursor: pointer;
      transition: all 0.5s ease;
      animation: pulse-glow 2s infinite ease-in-out;
      z-index: 1;
    }}

    @keyframes pulse-glow {{
      0% {{ box-shadow: 0 0 15px rgba(255, 153, 200, 0.4); }}
      50% {{ box-shadow: 0 0 35px rgba(255, 153, 200, 0.8); }}
      100% {{ box-shadow: 0 0 15px rgba(255, 153, 200, 0.4); }}
    }}

    .envelope:before {{
      content: "";
      position: absolute;
      z-index: 10;
      border-top: 150px solid transparent;
      border-right: 225px solid #f2d5f8;
      border-bottom: 150px solid #f2d5f8;
      border-left: 225px solid transparent;
      top: 0;
    }}

    .envelope:after {{
      content: "";
      position: absolute;
      z-index: 10;
      border-top: 150px solid transparent;
      border-right: transparent;
      border-bottom: 150px solid #e7c6ff;
      border-left: 225px solid #e7c6ff;
      top: 0;
    }}

    .flap {{
      position: absolute;
      top: 0;
      width: 0;
      height: 0;
      border-left: 225px solid transparent;
      border-right: 225px solid transparent;
      border-top: 160px solid #d896ff;
      transform-origin: top;
      transition: transform 0.6s ease;
      z-index: 11;
    }}

    .seal {{
      position: absolute;
      top: 140px;
      left: 200px;
      width: 50px;
      height: 50px;
      background: #9d4edd;
      border-radius: 50%;
      z-index: 12;
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
      font-size: 24px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.3);
      transition: opacity 0.4s;
    }}
    .seal:after {{ content: "❤"; }}

    /* ADJUSTED: Dark Pink Background and Smaller Text */
    .letter {{
      position: absolute;
      bottom: 10px;
      left: 25px;
      width: 400px;
      height: 250px;
      background: #ff4d6d; /* Dark Pink Background */
      padding: 30px;
      box-sizing: border-box;
      transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 5;
      font-family: 'Dancing Script', cursive;
      text-align: center;
      font-size: 1.2rem; /* Decreased size */
      line-height: 1.4;
      color: #ffffff; /* White text for better contrast on dark pink */
      box-shadow: inset 0 0 50px rgba(0,0,0,0.2);
      border: 1px solid #ff758f;
      overflow: hidden;
    }}

    .open .flap {{
      transform: rotateX(180deg);
      z-index: 1;
    }}

    .open .seal {{
      opacity: 0;
      pointer-events: none;
    }}

    .letter-out .letter {{
      transform: translateY(-150px) scale(1.1);
      height: 580px; 
      z-index: 100;
      box-shadow: 0 20px 50px rgba(0,0,0,0.4);
    }}

    /* ADJUSTED: Falling Hearts are now RED */
    .heart {{
      position: absolute;
      color: #ff0000; /* Vibrant Red */
      font-size: 18px;
      top: -20px;
      z-index: 101;
      user-select: none;
      pointer-events: none;
      animation: fall linear forwards;
    }}

    @keyframes fall {{
      to {{
        transform: translateY(650px) rotate(360deg);
      }}
    }}
    </style>

    <div class="container">
      <div id="env" class="envelope" onclick="nextStep()">
        <div class="flap"></div>
        <div class="seal"></div>
        <div id="letter-box" class="letter">
          <div style="border: 2px solid rgba(255,255,255,0.3); padding: 20px; height: 100%; display: flex; align-items: center; justify-content: center; flex-direction: column; position: relative;">
            {poetry_text}
          </div>
        </div>
      </div>
    </div>

    <script>
    let step = 0;

    function createHeart() {{
        const letterBox = document.getElementById('letter-box');
        const heart = document.createElement('div');
        heart.classList.add('heart');
        heart.innerHTML = '❤';
        heart.style.left = Math.random() * 100 + '%';
        heart.style.animationDuration = (Math.random() * 3 + 2) + 's';
        heart.style.opacity = (Math.random() * 0.5) + 0.5;
        letterBox.appendChild(heart);

        setTimeout(() => {{ heart.remove(); }}, 5000);
    }}

    function nextStep() {{
      const env = document.getElementById('env');
      if (step === 0) {{
        env.classList.add('open');
        step = 1;
      }} else if (step === 1) {{
        env.classList.add('letter-out');
        step = 2;

        setInterval(createHeart, 250);

        confetti({{
          particleCount: 150,
          spread: 70,
          origin: {{ y: 0.6 }},
          colors: ['#ff0000', '#ff4d6d', '#ffffff']
        }});
      }}
    }}
    </script>
    """
    components.html(envelope_html, height=1000)

poetry = """
<br>
<br>
ADMIRING THE BEAUTY-II<br>
Itne Dur reh kr bhi pass mehsoos hoti ho<br>
tumhare julfon ko kaano m sawar de ky khaas lagti ho<br>
chehre pe bindi laga de ankhon m kajal sajade kya kya khayaalon m dub jate ha<br>
ye khubsurat si chehare me khoa khoa se rehte ha<br>
tumhari pyari si akhe ky karajati h<br>
tumhari pyari si muskaan ye aayino ki shaan bhadha jaati h<br>
Shabdon me piro lete ha tumhe kyuki faasle kam nhi hoti tumhara sath ye lamha yuhi tham kyu nhi jaati.<br>
"""
beautiful_envelope(poetry)

st.markdown("""
<style>

.glow-msg {
    text-align: center;
    font-size: 72px;          /* Increased text size */
    font-weight: 700;
    color: #ff9eb5;           /* Soft pastel pink */
    margin-top: -5px;
    margin-bottom: 30px;
    line-height: 1.3;

    /* Soft glowing effect (NO animation) */
    text-shadow: 
        0 0 10px rgba(255, 158, 181, 0.7),
        0 0 20px rgba(255, 158, 181, 0.5),
        0 0 35px rgba(255, 158, 181, 0.35);
}

</style>

<p class="glow-msg">
<br>
💗Happy birthday my goluu moluu💗<br>
<br>
✨🎀Hamesha khush reho health reho Or safe reho padho likho future m successful bhi toh hona ha<br>
or mere rehoo hehe....kitne saal hogya sath reh aise future m bhi rehna ha or<br>
apko satai bhi ha uske liye sorry...ladai jhagda toh hote rehta ha uske bina <br>
humlog k din kaha kaatega per har ladai k baad sath rehte ha humlog<br>
I know future m bhi bahut problems ayngi per sath reh kr dekhnge sab..<br>
Bahut bharosa krte ha kabhi todna mt humko pata ha tum bhi krti ha bahut humbhi nhi todnge<br>
Ye sab baat hata kr Josh josh m soch toh liye website bana kr surprise krnge yeahh..<br> 
Sach bol reh halat khrb hogya bahut efforts laga din k chat ghnta Or <br>
toh mera laptop itna acha ha itna lag itna slow ky bole per at last soche ha<br>
toh krnge hi Or ye mt sochna ki kisi ka code utha kr dal diye har ek chiz apna<br> 
haath se kiye ha yeha tak ki jo background color h wo bhi ha"chat gpt Or AI tools" k <br>
help liye ha per bahut mehnat laga ha Or honestly batana kaisa laga.🎀✨<br> 
<br>
💕Laamuuuuuu my cutie pie 💕<br>
""", unsafe_allow_html=True)
