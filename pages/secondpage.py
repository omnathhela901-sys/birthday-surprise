import streamlit as st
import base64
import os
import random
import time
import streamlit.components.v1 as components

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


#------BACKGROUND-----
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


# --- 1. TITLE CODE ---
st.markdown("""
<style>

.glow-title {
    font-family: "Copperplate", "Copperplate Gothic Light", fantasy;
    font-size: 80px;
    font-weight: 700;
    text-align: center;
    color: #ff4d4d;  /* Light red */

    margin-top: 40px;

    /* Glow Effect */
    text-shadow:
        0 0 10px #ff4d4d,
        0 0 20px #ff1a1a,
        0 0 30px #ff1a1a,
        0 0 40px #ff0000,
        0 0 60px #ff0000,
        0 0 80px #ff0000;

    animation: glowPulse 2s infinite alternate;
}

@keyframes glowPulse {
    from {
        text-shadow:
            0 0 8px #ff6666,
            0 0 15px #ff3333,
            0 0 25px #ff1a1a,
            0 0 35px #ff0000;
    }
    to {
        text-shadow:
            0 0 15px #ff9999,
            0 0 30px #ff4d4d,
            0 0 45px #ff1a1a,
            0 0 60px #ff0000;
    }
}

</style>

<h1 class="glow-title">🌸READY F♡R S♡ME L♡VELY GAME!!🌸</h1>
""", unsafe_allow_html=True)

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
💗A L♡VELY LITTLE MESSAGE BEF♡RE Y♡U BEGIN💗<br>
    🌺S♡ME REAS♡N WHY Y♡U ARE SPECIAL F♡R ME<br> 
ALTH♡UGH Y♡UR SPECIALITY CAN'T BE JUDGE ♡N S♡ME NUMBERS <br>
THERE IS C♡UNTLESS REAS♡N WHY Y♡U ARE SPECIAL T♡ ME AND H♡W DEEPLY I'M IN L♡VE WITH Y♡U🌺<br>
<br>
✨🎀G♡ ♡N FLIP THE CARDS🎀✨<br>
{\__/}<br>
( • . •)<br>
/ >💗<br>

</p>
""", unsafe_allow_html=True)


#----------BACKGROUND COLOR--------
def set_custom_css():
    """
    Injects custom CSS to set the black-to-pink gradient background
    and style the main content area.
    """
    st.markdown(
        """
        <style>
        /* TARGET: The main application container (stApp)
        This is where the entire background color/image is set. 
        */
        .stApp {
            /* Fallback and base color */
            background-color: #000000;

            /* The Gradient Definition: 
            to bottom: direction of the fade (starts at top, ends at bottom)
            #000000 0%: Solid black starts at the very top (0%)
            #000000 60%: Black continues down to 60% of the screen height
            #FF69B4 100%: Hot/Deep Pink glows from the bottom (100%)

            By keeping the top 60% solid black, the fade looks smooth and 
            only happens in the bottom 40% of the view.
            */
            background-image: linear-gradient(
                to bottom, 
                #000000 0%,           /* Black at the top */
                #000000 60%,          /* Black continues down to 60% */
                #FF69B4 100%          /* Hot Pink at the very bottom */
            );

            /* Ensure the content is visible over the black/dark background */
            color: #FFFFFF; 
        }

        /* OPTIONAL: If you want to customize the main content block itself 
        (e.g., removing its default background or margin)
        */
        .main .block-container {
            /* Maximize the width of content */
            max-width: 90%;
            padding-top: 1rem;
            padding-right: 1rem;
            padding-left: 1rem;
            padding-bottom: 1rem;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


set_custom_css()


# --- 1. Custom CSS for Background Gradient (from previous request) ---
def set_custom_background_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #000000;
            background-image: linear-gradient(
                to bottom, 
                #000000 0%,           /* Black at the top */
                #000000 60%,          /* Black continues down to 60% */
                #FF69B4 100%          /* Hot Pink at the very bottom */
            );
            color: #FFFFFF; /* Ensure text is visible */
            overflow: hidden; /* Hide anything that goes beyond the screen, important for animation */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- 2. CSS for Cherry Blossom Animation ---
def set_cherry_blossom_animation_css():
    st.markdown(
        """
        <style>
        /* Keyframes for the falling animation */
        @keyframes fall {
            0% {
                transform: translateY(-10vh) translateX(0); /* Start slightly above view, some horizontal wobble */
                opacity: 0.8;
            }
            100% {
                transform: translateY(105vh) translateX(50px); /* Fall below view, some horizontal wobble */
                opacity: 0;
            }
        }

        /* Keyframes for a slight horizontal sway/wobble */
        @keyframes sway {
            0% { transform: translateX(0); }
            50% { transform: translateX(20px); } /* Sway to the right */
            100% { transform: translateX(0); }
        }

        /* Style for individual cherry blossom leaves */
        .cherry-blossom {
            position: fixed; /* Fixed position so they float over content */
            width: 15px; /* Size of the leaf */
            height: 15px;
            background-color: #FFC0CB; /* Light pink color */
            border-radius: 50%; /* Make them round like petals */
            filter: blur(2px); /* Soft blur for glowing effect */
            box-shadow: 0 0 8px #FFC0CB, 0 0 12px #FFB6C1; /* Outer glow */
            pointer-events: none; /* Make sure they don't block clicks */
            z-index: 9999; /* Ensure they are on top of everything */
            animation: fall linear infinite, sway ease-in-out infinite alternate;
        }

        /* Create multiple leaves with different animation delays and durations 
        to make the effect look more natural and continuous.
        You can add many more of these for a denser effect.
        */
        .cherry-blossom:nth-child(1) { left: 10%; animation-duration: 10s, 3s; animation-delay: 0s, 0s; width: 12px; height: 12px; opacity: 0.9;}
        .cherry-blossom:nth-child(2) { left: 20%; animation-duration: 12s, 4s; animation-delay: 1s, 0.5s; width: 18px; height: 18px; opacity: 0.7;}
        .cherry-blossom:nth-child(3) { left: 30%; animation-duration: 9s, 3.5s; animation-delay: 2s, 1s; width: 14px; height: 14px; opacity: 0.8;}
        .cherry-blossom:nth-child(4) { left: 40%; animation-duration: 11s, 2.8s; animation-delay: 3s, 0.2s; width: 16px; height: 16px; opacity: 0.6;}
        .cherry-blossom:nth-child(5) { left: 50%; animation-duration: 8s, 4.2s; animation-delay: 4s, 1.5s; width: 10px; height: 10px; opacity: 1;}
        .cherry-blossom:nth-child(6) { left: 60%; animation-duration: 13s, 3.1s; animation-delay: 0.5s, 0.8s; width: 20px; height: 20px; opacity: 0.75;}
        .cherry-blossom:nth-child(7) { left: 70%; animation-duration: 10.5s, 3.8s; animation-delay: 2.5s, 0.3s; width: 13px; height: 13px; opacity: 0.9;}
        .cherry-blossom:nth-child(8) { left: 80%; animation-duration: 9.5s, 2.5s; animation-delay: 1.5s, 1.2s; width: 17px; height: 17px; opacity: 0.85;}
        .cherry-blossom:nth-child(9) { left: 90%; animation-duration: 14s, 4.5s; animation-delay: 3.5s, 0.7s; width: 11px; height: 11px; opacity: 0.65;}
        .cherry-blossom:nth-child(10) { left: 5%; animation-duration: 11.5s, 3.3s; animation-delay: 4.5s, 1.8s; width: 19px; height: 19px; opacity: 0.7;}
        .cherry-blossom:nth-child(11) { left: 25%; animation-duration: 9.8s, 3.9s; animation-delay: 0.8s, 0.1s; width: 14px; height: 14px; opacity: 0.95;}
        .cherry-blossom:nth-child(12) { left: 45%; animation-duration: 12.5s, 2.7s; animation-delay: 1.8s, 1.3s; width: 16px; height: 16px; opacity: 0.8;}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- 3. Streamlit App Layout ---

# Apply the custom CSS for background and animation
set_custom_background_css()
set_cherry_blossom_animation_css()

# --- Inject the HTML for the cherry blossom leaves ---
# We create several div elements, each styled by the .cherry-blossom class
# and its nth-child selectors for varied animations.
st.markdown(
    """
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    <div class="cherry-blossom"></div>
    """,
    unsafe_allow_html=True
)

# --- the Falling Hearts Animation ---

HEART_ANIMATION_CSS = """
<style>
/* 1. Define the particle container to cover the whole page */
.heart-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none; /* Allows clicking on Streamlit elements underneath */
    overflow: hidden; /* Prevents hearts from creating scrollbars */
    z-index: 999; /* Ensure hearts are on top of other content */
}

/* 2. Define the heart shape and colors */
.heart {
    position: absolute;
    width: 10px;
    height: 10px;
    background-color: #ffc0cb; /* Default color (will be overridden) */
    transform: rotate(-45deg);
    /* GLOW EFFECT */
    box-shadow: 0 0 8px rgba(255, 255, 255, 0.7); 
}

/* Create the top and left circles of the heart shape */
.heart:before,
.heart:after {
    content: '';
    position: absolute;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: inherit; /* Inherit the color from .heart */
}

.heart:before {
    top: -5px;
    left: 0;
}

.heart:after {
    top: 0;
    left: 5px;
}

/* 3. Define the falling animation */
@keyframes fall {
    0% {
        transform: translate(0, -10vh) rotateZ(0deg);
        opacity: 0.8;
    }
    100% {
        transform: translate(var(--x-end), 100vh) rotateZ(var(--r-end));
        opacity: 0;
    }
}

/* 4. Generate individual heart elements with random properties */
"""

# --- Configuration: Setting the number of hearts to 100 ---
num_hearts = 100

# The following loop generates the individual heart styling
# This creates a mix of two colors: Dark Pink (#FF1493) and Red (#FF0000)

for i in range(1, num_hearts + 1):
    # Determine color (alternating mix of dark pink and red)
    color = "#FF1493" if i % 2 == 0 else "#FF0000"

    # Random properties for each heart's starting position, delay, duration, etc.
    start_x = random.uniform(0, 100)  # Starting X position (0% to 100%)
    duration = random.uniform(8, 15)  # Animation duration (8s to 15s)
    delay = random.uniform(0, 5)  # Animation delay (0s to 5s)
    end_x_offset = random.uniform(-100, 100)  # Final X offset (for a slight sway)
    end_rotation = random.uniform(-720, 720)  # Final rotation (for spinning)

    # Append the CSS for the individual heart
    HEART_ANIMATION_CSS += f"""
.heart:nth-child({i}) {{
    background-color: {color};
    left: {start_x}vw;
    animation: fall {duration}s linear {delay}s infinite;
    --x-end: {end_x_offset}px;
    --r-end: {end_rotation}deg;
    animation-fill-mode: forwards;
}}
"""

# Close the style tag
HEART_ANIMATION_CSS += "</style>"

# --- HTML structure for the hearts container ---

# Generate the heart elements to be placed inside the container
HEART_HTML = ""
for i in range(num_hearts):
    HEART_HTML += '<div class="heart"></div>'

# Wrap the hearts in the container
HEART_CONTAINER_HTML = f"""
<div class="heart-container">
    {HEART_HTML}
</div>
"""
st.markdown(HEART_ANIMATION_CSS, unsafe_allow_html=True)
st.markdown(HEART_CONTAINER_HTML, unsafe_allow_html=True)

#----CRDS FLIP ANIMATIONS----
html_code = """
<style>

.container {
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 40px;
    flex-wrap: wrap;
}

.card {
    width: 220px;
    height: 280px;
    perspective: 1000px;
}

.inner-card {
    width: 100%;
    height: 100%;
    position: relative;
    transition: transform 0.8s;
    transform-style: preserve-3d;
    cursor: pointer;
}

.inner-card.flipped {
    transform: rotateY(180deg);
}

.front, .back {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 20px;
    padding: 20px;
    color: Black;
    font-family: Copperplate, fantasy;
    font-size: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    backface-visibility: hidden;

    border: 2px solid #ff4d4d;
    box-shadow: 0 0 15px #ff4d4d, 0 0 30px #ff0000;
}

/* RED FRONT */
.front {
    background: linear-gradient(135deg, #ff6b6b, #ff1a1a);
}

/* PINK BACK */
.back {
    background: linear-gradient(135deg, #ff9bd6, #ff5ec4);
    transform: rotateY(180deg);
}

</style>

<div class="container">
"""

reasons = [
    "Your smile brightens everything ❤️",
    "You care deeply for me💕",
    "You make me feel special ✨",
    "i love your dedication 💛",
    "You support me always 🤍",
    "You are bheery much beautiful💗",
    "You make me happy every time😂"
]

for i, r in enumerate(reasons, start=1):
    html_code += f"""
    <div class="card">
        <div class="inner-card" onclick="this.classList.toggle('flipped')">
            <div class="front"><b>Reas♡n {i}</b></div>
            <div class="back">{r}</div>
        </div>
    </div>
    """

html_code += "</div>"

components.html(html_code, height=1100, scrolling=True)



# ---------------- WHEEL AND QIUZZ ----------------
st.markdown("""
<style>
.stButton>button {
    background-color:#9900ff;
    color:white;
    padding:14px 32px;
    font-size:18px;
    border-radius:8px;
    box-shadow:0 0 12px #9900ff,0 0 25px #e600ff;
}

.wheel-container {
    position: relative;
    display: flex;
    color:white;
    justify-content: center;
    margin-top: 20px;
}

.wheel {
    width: 260px;
    height: 260px;
    border-radius: 50%;
    border: 8px solid #9900ff;
    box-shadow: 0 0 25px #9900ff, 0 0 45px #ff00ff;
    background: conic-gradient(
        #ff99ff 0deg 51deg,
        #d580ff 51deg 103deg,
        #b366ff 103deg 154deg,
        #9966ff 154deg 206deg,
        #b366ff 206deg 257deg,
        #d580ff 257deg 309deg,
        #ff99ff 309deg 360deg
    );
    transition: transform 0.2s linear;
}

.pointer {
    position: absolute;
    top: -18px;
    font-size: 28px;
}

.feedback-ok {
    color: green;
    font-weight: bold;
}

.feedback-wrong {
    color: red;
    font-weight: bold;
}

.dare-result {
    margin-top: 25px;
    padding: 18px;
    border: 3px solid #9900ff;
    border-radius: 15px;
    text-align: center;
    font-size: 1.3em;
    font-weight: bold;
    color: #4b0082;
}
.dare-result {
    margin-top: 25px;
    padding: 18px;
    text-transform: uppercase;
    border: 3px solid #9900ff;
    border-radius: 15px;
    text-align: center;
    font-size: 1.3em;
    font-weight: bold;
    color: #ff7ad9;
    text-shadow: 0 0 10px #ff00cc, 0 0 20px #ff66ff;
    background: rgba(255, 255, 255, 0.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.quiz-question {
    color: #ffb6c1; /* light pink */
    font-weight: 900;
    text-transform: uppercase;
    font-size: 22px;
    text-shadow:
        0 0 6px #c70039,
        0 0 12px #d2042d,
        0 0 20px #9b111e;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* ===== QUESTION CARD ===== */
.question-card {
    background: linear-gradient(145deg, #2b0000, #4d0000);
    border-radius: 18px;
    padding: 18px 22px;
    margin: 18px 0;
    box-shadow:
        0 0 12px #8b0000,
        0 0 25px #b11226;
    border: 2px solid #7a0012;
}
/* Question text */
.quiz-question {
    color: #ffb6c1; /* light pink */
    font-weight: 900;
    text-transform: uppercase;
    font-size: 22px;
    text-shadow:
        0 0 6px #c70039,
        0 0 12px #d2042d,
        0 0 20px #9b111e;
    margin-bottom: 10px;
}

/* ===== FEEDBACK ===== */
.feedback-ok {
    color: #00ff9c;
    font-weight: bold;
    animation: pop 0.4s ease-in-out;
}

.feedback-wrong {
    color: #ff0033;
    font-weight: bold;
    animation: shake 0.4s;
}

/* SUCCESS POP */
@keyframes pop {
    0% { transform: scale(0.8); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}

/* SHAKE ANIMATION */
@keyframes shake {
    0% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    50% { transform: translateX(5px); }
    75% { transform: translateX(-5px); }
    100% { transform: translateX(0); }
}
""",unsafe_allow_html=True)



# ---------------- QUIZ DATA ----------------
questions = [
    {
        "q": "WHICH YEAR Y♡U TEXT ME IN WHATSAPP ?",
        "options": ["2020", "2022", "2018", "2024"],
        "answer": "2022"
    },
    {
        "q":"H♡W MANY YEAR WE HAVE BEEN T♡GETHER?",
        "options": ["TW♡", "F♡UR", "EIGHT", "SEVEN"],
        "answer": "EIGHT"
    },
    {
        "q": "H♡W I EXPRESS MY FEELING T♡ Y♡U FIRST TIME,BY SAYING..?",
        "options": ["I L♡VE Y♡U","I HAVE FEELING F♡R Y♡U","THE M♡♡N IS BEAUTIFUL ISN'T IT", "N♡NE ♡F AB♡VE"],
        "answer": "THE M♡♡N IS BEAUTIFUL ISN'T IT"
    },
    {
        "q": "MY FAV F♡♡DD?",
        "options": ["S♡UTH INDIAN", "FAST F♡♡D", "BIRYANI", "WHAT EVER G♡LUUU MAKE F♡R ME"],
        "answer": "WHAT EVER G♡LUUU MAKE F♡R ME"
    },
    {
        "q": "H♡W MUCH I L♡VE Y♡U?",
        "options": [
            "VEEERYYYY MUCH",
            "VEEERYYY VEEERYYY MUCH",
            "N♡NE ♡F THESE",
            "INFINITYYYYY"
        ],
        "answer": "INFINITYYYYY"
    },
    {
        "q": "H♡W WAS ♡UR FIRST HUG?",
        "options": ["BAD", "G♡♡D", "A M♡MENT FR♡ZEN IN TIME", "N♡T S♡ G♡♡D N♡T S♡ BAD"],
        "answer": "A M♡MENT FR♡ZEN IN TIME"
    },
    {
        "q": "MY DREAM F♡REIGN PLACE?",
        "options": ["JAPAN", "DUBAI", "PARIS", "ALL ♡F AB♡VE"],
        "answer": "ALL ♡F AB♡VE"
    }
]

dares = [

"🥰 Beautiful date",
"🤩 Virtual m♡vie date",
"🥳Anything y♡u want",
"😎Dance with y♡u",
"😝Better luck next time",
"😱Saying yes f♡r a day",
"😊 M♡m♡ and g♡lgappa date",
]

# GLOWING TITLE
st.markdown("""
<h1 style="
    text-align:center;
    font-weight:900;
    color:#9dff9d;
    text-shadow: 0 0 8px #0b6b0b, 0 0 18px #0b6b0b;
">
L♡VELY QUIZ T♡ WIN A CHANCE T♡ SPIN A WHEEL FULL ♡F PRISE
</h1>
""", unsafe_allow_html=True)



# ---------------- SESSION STATE INIT ----------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False
    st.session_state.correct_map = {}

# ---------------- QUIZ UI ----------------
for i, q in enumerate(questions):
    st.markdown(f"""
    <div class="question-card">
        <div class="quiz-question">
            Q{i+1}. {q['q']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.radio(
        "Choose one option:",
        q["options"],
        key=f"q{i}"
    )

# ---------------- SUBMIT ----------------
if st.button("✅ Submit"):
    st.session_state.submitted = True
    st.session_state.correct_map = {}

    for i, q in enumerate(questions):
        if st.session_state[f"q{i}"] == q["answer"]:
            st.session_state.correct_map[i] = True
        else:
            st.session_state.correct_map[i] = False

# ---------------- FEEDBACK ----------------
all_correct = True

if st.session_state.submitted:
    st.markdown("### ✅ Feedback")
    for i in range(len(questions)):
        if st.session_state.correct_map.get(i):
            st.markdown(f"<div class='feedback-ok'>Q{i+1}: Perfect! Go on ✅</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='feedback-wrong'>Q{i+1}: Incorrect answer ❌ Try again</div>", unsafe_allow_html=True)
            all_correct = False

# ---------------- SPIN UNLOCK ----------------
if st.session_state.submitted and all_correct:
    st.success("🎉ALL ARE C♡RRECT! WAHHHHH MERI G♡LUUUUUU")

    wheel_placeholder = st.empty()
    result_placeholder = st.empty()

    wheel_placeholder.markdown("""
    <div class="wheel-container">
        <div class="pointer">⬇️</div>
        <div class="wheel"></div>
    </div>
    """, unsafe_allow_html=True)

    result_placeholder.markdown(
        "<div class='dare-result'>°❀•°SPIN THE WHEEL!!! SEE YOUR LUCK°•❀°</div>",
        unsafe_allow_html=True
    )

    if st.button("🎡❀•°CLICK T♡ SPIN°•❀"):
        angle = 0
        for i in range(14):
            angle += random.randint(40, 90)
            wheel_placeholder.markdown(f"""
            <div class="wheel-container">
                <div class="pointer">⬇️</div>
                <div class="wheel" style="transform: rotate({angle}deg);"></div>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.07 + i * 0.02)

        st.balloons()
        result_placeholder.markdown(
            f"<div class='dare-result'>🎉 ♡♡♡<br>{random.choice(dares)}</div>",
            unsafe_allow_html=True
        )


st.markdown("""
<style>

.glow-msg {
    text-align: center;
    font-size: 100px;   /* Exactly 60px as you requested */
    font-weight: 1000;
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
💗I'LL D♡ ANYTHING WHICH C♡MES IN WHEEL💗<br>
</p>
""", unsafe_allow_html=True)


st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(135deg, #28a745, #34d058);
    color: white;
    font-size: 16px;
    font-weight: bold;
    padding: 10px 24px;
    border-radius: 25px;
    border: none;
    box-shadow: 0 0 10px rgba(40,167,69,0.8);
}
div.stButton > button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

if st.button("CLICK ME TO MOVE"):
    st.switch_page("pages/thirdpage.py")

