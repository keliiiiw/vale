import streamlit as st
import random

st.set_page_config(page_title="Happy Valentine", page_icon="💖", layout="centered")

if "open_letter" not in st.session_state:
    st.session_state.open_letter = False

st.markdown("""
<style>

/* Disable scroll */
html, body {
    overflow: hidden !important;
}

/* Background */
.stApp {
    background: linear-gradient(to bottom right, #ffc0cb, #ff69b4);
    color: white;
    text-align: center;
    font-family: 'Georgia', serif;
}

/* Big flower decoration */
.flower {
    position: fixed;
    bottom: -30px;
    right: -20px;
    font-size: 180px;
    opacity: 0.15;
    z-index: 0;
    animation: floatFlower 6s ease-in-out infinite;
}

@keyframes floatFlower {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
}

/* Falling hearts */
.heart {
    position: fixed;
    top: -10px;
    font-size: 20px;
    animation: fall linear infinite;
    z-index: 1;
}

@keyframes fall {
    to { transform: translateY(110vh); }
}

/* Title */
.title {
    font-size: 42px;
    font-weight: bold;
    margin-top: 80px;
    animation: fadeInTitle 2s ease;
    position: relative;
    z-index: 2;
}

@keyframes fadeInTitle {
    from {opacity: 0; transform: translateY(30px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Button */
div.stButton > button {
    background-color: white;
    color: #ff1493;
    border-radius: 40px;
    font-size: 18px;
    padding: 10px 35px;
    border: none;
    transition: 0.4s;
    z-index: 3;
}

div.stButton > button:hover {
    background-color: #ff1493;
    color: white;
    transform: scale(1.08);
}

/* Letter */
.letter {
    position: fixed;
    left: 50%;
    transform: translate(-50%, 40px) scale(0.95);
    width: 85%;
    max-width: 420px;
    background: #fff0f5;
    color: #c71585;
    padding: 28px;
    border-radius: 25px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.25);
    text-align: center;
    font-size: 16px;
    opacity: 0;
    bottom: 10%;
    transition: all 1.4s cubic-bezier(0.22, 1, 0.36, 1);
    z-index: 5;
}

.letter.show {
    opacity: 1;
    transform: translate(-50%, 0px) scale(1);
}

.letter-content {
    animation: fadeContent 2s ease forwards;
    opacity: 0;
}

@keyframes fadeContent {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* Mobile */
@media (max-width: 400px) {
    .title { font-size: 32px; }
    .flower { font-size: 130px; }
    .letter { font-size: 14px; padding: 20px; }
}

</style>
""", unsafe_allow_html=True)

# Big Flower
st.markdown('<div class="flower">🌹</div>', unsafe_allow_html=True)

# Falling hearts
for i in range(20):
    left = random.randint(0, 100)
    duration = random.uniform(6, 12)
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

# Title
st.markdown('<div class="title">💖 HAPPY VALENTINE MOWY 💖</div>', unsafe_allow_html=True)

st.write("")

if not st.session_state.open_letter:
    if st.button("NEXT 💌"):
        st.session_state.open_letter = True

if st.session_state.open_letter:
    st.markdown("""
    <div class="letter show">
        <div class="letter-content">
            <h2>💌 For My Love 💌</h2>
            maaf kalo ini simple banget,<br>
            tapi intinya aku sayang banget sama kamu, maaf ya<br>
            kalo aku masih ngga bisa nepatin janji aku, aku<br>
            selalu kangen sama kamu, tingkah imut kamu, suara kamu<br>
            aku bener bener selalu kangen semua hal tentang kamu, aku<br>
            pengen banget ngasih kamu bunga tapi aku bener bener binggung<br>
            next time aku bakal usahain bunga itu bener bener sampe di kamu..<br><br>
            <b>i love u Chelsea Morenofa 💖</b>
        </div>
    </div>
    """, unsafe_allow_html=True)
