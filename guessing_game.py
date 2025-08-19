import streamlit as st
import random
import time

# 🎲 Page config
st.set_page_config(page_title="🎯 Random Number Guessing Game", page_icon="🎲", layout="centered")

# 🎯 Game title
st.markdown("<h1 style='text-align:center; color:#2E86C1;'>🎯 Random Number Guessing Game</h1>", unsafe_allow_html=True)

# 👉 Signature watermark bottom-right (no box, stylish look)
st.markdown(
    """
    <style>
    div[data-testid="stAppViewContainer"]::after {
        content: "✨ Built by Anuj Kumar Nirmal";
        position: fixed;
        bottom: 10px;
        right: 20px;
        font-size: 16px;
        font-style: italic;
        font-family: "Brush Script MT";
        color: rgba(46, 134, 193, 0.8);
        z-index: 999999;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🛠️ Session states initialization
if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 20)
if "tries" not in st.session_state:
    st.session_state.tries = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "guess" not in st.session_state:
    st.session_state.guess = 1   # 👉 Default guess value set to 1

# 🎮 User input with ValueError handling
try:
    st.session_state.guess = st.number_input(
        "🔢 Enter your guess (1 - 20):", 
        min_value=1, max_value=20, step=1, 
        key="guess_input", value=st.session_state.guess
    )

    if st.button("✅ Submit Guess") and not st.session_state.game_over:
        st.session_state.tries += 1
        if st.session_state.guess == st.session_state.num:
            duration = time.time() - st.session_state.start_time
            st.success(f"🎉 Correct! You guessed the number in {st.session_state.tries} tries.")
            st.info(f"⏱️ Time taken: {duration:.2f} seconds")
            st.balloons()
            st.session_state.game_over = True
        elif st.session_state.guess > st.session_state.num:
            st.warning("⬇️ Try a smaller number!")
        else:
            st.warning("⬆️ Try a larger number!")

# 👉 If user enters invalid input
except ValueError:
    st.error("⚠️ Invalid input! Please enter a valid number between 1 and 20.")

# 🔄 Restart button
if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        st.session_state.num = random.randint(1, 20)
        st.session_state.tries = 0
        st.session_state.start_time = time.time()
        st.session_state.game_over = False
        st.session_state.guess = 1  # 👉 Reset input back to 1 when restarting
        st.rerun()
