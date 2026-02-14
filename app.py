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

/* Falling hearts */
.heart {
    position: fixed;
    top: -10px;
    font-size: 20px;
    animation: fall linear infinite;
    z-index: 0;
}

@keyframes fall {
    to { transform: translateY(110vh); }
}

/* Title */
.title {
    font-size: 42px;
    font-weight: bold;
    margin-top: 80px;
    animation: fadeIn 2s ease-in-out;
    position: relative;
    z-index: 2;
    padding: 0 15px;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
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
}

div.stButton > button:hover {
    background-color: #ff1493;
    color: white;
    transform: scale(1.1);
}

/* Letter */
.letter {
    position: fixed;
    bottom: -100%;
    left: 50%;
    transform: translateX(-50%);
    width: 85%;
    max-width: 400px;
    background: #fff0f5;
    color: #c71585;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    text-align: center;
    font-size: 16px;
    transition: bottom 1.5s ease-in-out;
    z-index: 5;
}

.letter.show {
    bottom: 15%;
}

.letter h2 {
    font-size: 20px;
    margin-bottom: 15px;
}

/* Responsive for very small phones */
@media (max-width: 400px) {
    .title {
        font-size: 32px;
    }
    .letter {
        font-size: 14px;
        padding: 20px;
    }
}

</style>
""", unsafe_allow_html=True)

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

st.markdown('<div class="title">💖 HAPPY VALENTINE MOWY 💖</div>', unsafe_allow_html=True)

st.write("")
st.write("")

if not st.session_state.open_letter:
    if st.button("NEXT 💌"):
        st.session_state.open_letter = True

if st.session_state.open_letter:
    st.markdown("""
    <div class="letter show">
        <h2>💌 For My Love 💌</h2>
        Happy Valentine cantik 💕<br><br>
        maaf kalo ini simple banget,<br>
        tapi intinya aku sayang banget sama kamu,
        maaf kalo aku masih ngga bisa nepatin janji aku
        karena emang kamu selalu ngangenin, tingkah kamu,
        suara kamu, bener bener imut banget pls, aku pengen
        banget ngasih kamu bunga jujur, hufftt intinya<br><br>
        <b>i love u Chelsea Morenofa 💖</b>
    </div>
    """, unsafe_allow_html=True)
