import streamlit as st
import time
import random

st.set_page_config(page_title="Happy Valentine", page_icon="💖", layout="centered")

# --- SESSION STATE ---
if "show_message" not in st.session_state:
    st.session_state.show_message = False

# --- CUSTOM CSS ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #ffc0cb, #ff69b4);
    color: white;
    text-align: center;
    font-family: 'Georgia', serif;
    overflow: hidden;
}

/* Falling hearts animation */
.heart {
    position: fixed;
    top: -10px;
    font-size: 20px;
    animation: fall linear infinite;
}

@keyframes fall {
    to {
        transform: translateY(110vh);
    }
}

/* Main Title */
.title {
    font-size: 55px;
    font-weight: bold;
    margin-top: 100px;
    animation: fadeIn 2s ease-in-out;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Message Box */
.message-box {
    background-color: rgba(255,255,255,0.25);
    padding: 30px;
    border-radius: 25px;
    font-size: 22px;
    margin-top: 30px;
    animation: fadeIn 2s ease-in-out;
    backdrop-filter: blur(10px);
}

/* Elegant Button */
div.stButton > button {
    background-color: white;
    color: #ff1493;
    border-radius: 30px;
    font-size: 20px;
    padding: 12px 40px;
    border: none;
    transition: 0.4s;
}

div.stButton > button:hover {
    background-color: #ff1493;
    color: white;
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

# --- Generate Falling Hearts ---
for i in range(20):
    left = random.randint(0, 100)
    duration = random.uniform(5, 10)
    delay = random.uniform(0, 5)
    st.markdown(
        f"""
        <div class="heart" style="
            left:{left}%;
            animation-duration:{duration}s;
            animation-delay:{delay}s;">
            💖
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Main Content ---
st.markdown('<div class="title">💖 HAPPY VALENTINE MOWY 💖</div>', unsafe_allow_html=True)

st.write("")

if not st.session_state.show_message:
    if st.button("NEXT 💌"):
        st.session_state.show_message = True
        st.balloons()  # confetti effect
        time.sleep(0.5)

if st.session_state.show_message:
    st.markdown("""
    <div class="message-box">
    Happy Valentine cantik 💕<br><br>
    maaf kalo ini simple banget,<br>
    tapi intinya aku sayang banget sama kamu,<br><br>
    <b>i love u Chelsea Morenofa 💖</b>
    </div>
    """, unsafe_allow_html=True)
