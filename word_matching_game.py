import streamlit as st
import random

def main():
    st.title("🎯 Word Matching Game")
    st.write("Match words with their correct meanings. Choose a level to begin!")

    level = st.radio("Select Level:", ["Easy", "Medium", "Hard"])

    word_data = {
        "Easy": {"Happy": "Feeling pleasure", "Big": "Large in size",},
        "Medium": {"Serendipity": "Finding something good by chance", "Petrichor": "Smell of earth after rain"},
        "Hard": {"Obfuscate": "To make unclear", "Perspicacious": "Having keen perception",}
    }

    words = list(word_data[level].keys())
    meanings = list(word_data[level].values())
    unique_meanings = list(set(meanings))
    random.shuffle(unique_meanings)

    user_answers = {}
    for word in words:
        user_answers[word] = st.selectbox(f"🔹 **{word}**", ["Select Meaning"] + unique_meanings)

    if st.button("Submit"):
        score = sum(1 for word in words if user_answers[word] == word_data[level][word])
        st.success(f"🎯 You got **{score}/{len(words)}** correct!")

if __name__ == "__main__":
    main()
