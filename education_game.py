import streamlit as st
import random

def main():
    st.title("🎮 Word Scramble Game")

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
        "k": "sick",
    }

    # Select a word only if it’s not already stored
    if "scrambled_word" not in st.session_state:
        st.session_state.scrambled_word, st.session_state.correct_word = random.choice(list(words.items()))

    scrambled_word = st.session_state.scrambled_word
    correct_word = st.session_state.correct_word

    st.write(f"🔠 Unscramble the word: **{scrambled_word}**")

    user_guess = st.text_input("Your Guess:")

    if st.button("Submit"):
        if user_guess.lower() == correct_word:
            st.success("🎉 Correct! Well done!")
        else:
            st.error(f"❌ Incorrect. Try again!")

    if st.button("🔄 Try Another"):
        # Reset word selection
        st.session_state.scrambled_word, st.session_state.correct_word = random.choice(list(words.items()))
        st.rerun()

if __name__ == "__main__":
    main()
