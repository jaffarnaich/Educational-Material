import streamlit as st
import random

def main():
    st.title("🎮 Word Scramble Game")

    # List of words and their correct forms
    words = {
        "etacduo": "educate",
        "draer": "reader",
        "gaennirl": "learning",
        "kgininth": "thinking",
        "rnitwe": "writer",
        "tneap": "paten",
        "scein": "since",
        "mrof": "form",
        "srof": "fors",
        "sahw": "wash",
        "tub": "but",
        "sawh": "wash",
        "qicklu": "quickly",
        "laziy": "lazy",    
        "tredi": "tired",
        "kics": "sick",
    }

    # Select a random word
    scrambled_word, correct_word = random.choice(list(words.items()))

    st.write(f"🔠 Unscramble the word: **{scrambled_word}**")

    # Get user input
    user_guess = st.text_input("Your Guess:")

    if st.button("Submit"):
        if user_guess.lower() == correct_word:
            st.success("🎉 Correct! Well done!")
            else:
                st.error(f"❌ Incorrect. The correct word was: **{correct_word}**")

    # Play Again Button
    if st.button("🔄 Try Another"):
        st.rerun()
