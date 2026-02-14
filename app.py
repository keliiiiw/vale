import streamlit as st

st.set_page_config(page_title="Happy Valentine", page_icon="💖", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #ffb6c1, #ff69b4);
    color: white;
    text-align: center;
    font-family: 'Georgia', serif;
}
.big-title {
    font-size: 50px;
    font-weight: bold;
}
.heart {
    font-size: 90px;
    animation: pulse 1.5s infinite;
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}
.message-box {
    background-color: rgba(255,255,255,0.25);
    padding: 25px;
    border-radius: 20px;
    font-size: 20px;
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="heart">💖</div>', unsafe_allow_html=True)
st.markdown('<div class="big-title">HAPPY VALENTINE MOWY</div>', unsafe_allow_html=True)

st.write("")

if st.button("NEXT 💌"):
    st.markdown("""
    <div class="message-box">
    Happy Valentine cantik, maaf kalo ini simple banget,  
    tapi intinya aku sayang banget sama kamu,  
    i love u Chelsea Morenofa 💖
    </div>
    """, unsafe_allow_html=True)
