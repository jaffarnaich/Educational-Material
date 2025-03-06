import streamlit as st
import quiz
import word_of_the_day
import education_game
import word_matching_game
from translation import show_translation_page
from abbreviations import show_abbreviations_page



# Set page configuration
st.set_page_config(page_title="Education Material", page_icon="📚", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", [
    "Home", "Quiz","Word of the Day", 
     "Education Game", "Word Matching Game",
    "Translation", "Abbreviations"
])

# Home Page
if page == "Home":
    st.title("📚 Welcome to the Education Material Project")
    st.image("logo.jpg", width=200)
    st.write("This website provides educational resources including quizzes, flashcards, and grammar tools.")

# Other Pages
elif page == "Quiz":
    quiz.main()

elif page == "Word of the Day":
    word_of_the_day.main()

elif page == "Education Game":
    education_game.main()

elif page == "Word Matching Game":
    word_matching_game.main()

elif page == "Translation":
    show_translation_page()

elif page == "Abbreviations":
    show_abbreviations_page()
