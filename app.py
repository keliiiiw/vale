import streamlit as st
import random

st.set_page_config(page_title="Happy Valentine", page_icon="💖", layout="centered")

# Session state
if "open_letter" not in st.session_state:
    st.session_state.open_letter = False

# --- CSS STYLE ---
st.markdown("""
<style>

/* Disable scroll */
html, body, [class*="css"]  {
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
    font-size: 22px;
    animation: fall linear infinite;
    z-index: 0;
}

@keyframes fall {
    to {
        transform: translateY(110vh);
    }
}

/* Title */
.title {
    font-size: 55px;
    font-weight: bold;
    margin-top: 120px;
    animation: fadeIn 2s ease-in-out;
    position: relative;
    z-index: 2;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(30px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Elegant Button */
div.stButton > button {
    background-color: white;
    color: #ff1493;
    border-radius: 40px;
    font-size: 20px;
    padding: 12px 45px;
    border: none;
    transition: 0.4s;
    z-index: 2;
}

div.stButton > button:hover {
    background-color: #ff1493;
    color: white;
    transform: scale(1.1);
}

/* Letter container */
.letter {
    position: fixed;
    bottom: -100%;
    left: 50%;
    transform: translateX(-50%);
    width: 60%;
    background: #fff0f5;
    color: #c71585;
    padding: 40px;
    border-radius: 25px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    text-align: center;
    font-size: 20px;
    transition: bottom 1.5s ease-in-out;
    z-index: 5;
}

/* Show letter */
.letter.show {
    bottom: 20%;
}

/* Love decoration inside letter */
.letter h2 {
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# Generate falling hearts
for i in range(25):
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

# Main title
st.markdown('<div class="title">💖 HAPPY VALENTINE MOWY 💖</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# Button
if not st.session_state.open_letter:
    if st.button("NEXT 💌"):
        st.session_state.open_letter = True

# Letter animation
if st.session_state.open_letter:
    st.markdown("""
    <div class="letter show">
        <h2>💌 For My Love 💌</h2>
        Happy Valentine cantik 💕<br><br>
        maaf kalo ini simple banget,<br>
        tapi intinya aku sayang banget sama kamu, maaf ya kalo aku
        masih belom bisa tepatin janji aku, aku beneran kangen terus
        sama kamu, cewe imut yang paling lucu, yang selalu buat aku
        kangen, jujur aku mau banget ngasih bunga tapi ngga tau
        gimana caranya :( intinya<br><br>
        <b>i love u Chelsea Morenofa 💖</b>
    </div>
    """, unsafe_allow_html=True)
