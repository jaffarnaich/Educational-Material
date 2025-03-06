import streamlit as st
from database import insert_quiz_result, fetch_quiz_results
import pandas as pd

def main():
    st.title("📝 Interactive Quiz")

    questions = {
        "What is the synonym of 'happy'?": ["Sad", "Excited", "Joyful", "Angry"],
        "Which of these is an idiom?": ["Break the ice", "Drink water", "Walk fast", "Run slowly"]
    }

    score = 0
    total_questions = len(questions)  # ✅ Fix: Define total questions
    user_name = st.text_input("Enter your name:")

    for question, options in questions.items():
        user_answer = st.radio(question, options)
        if user_answer == options[2]:  # ✅ Assuming index 2 holds correct answers
            score += 1

    if st.button("Submit Answers"):
        if user_name.strip():  # ✅ Prevent empty name submissions
            insert_quiz_result(user_name, score, total_questions)  # ✅ Fixed function call
            st.success(f"🎉 You scored {score}/{total_questions}!")
        else:
            st.error("⚠ Please enter your name before submitting!")

    if st.button("📥 Download Quiz Data"):
        data = fetch_quiz_results()  # ✅ fetch_quiz_results doesn't need arguments
        if data:
            df = pd.DataFrame(data, columns=["ID", "User", "Score", "Total Questions"])
            st.download_button(label="Download CSV", data=df.to_csv(index=False), file_name="quiz_results.csv", mime="text/csv")
        else:
            st.warning("⚠ No quiz data available to download!")

if __name__ == "__main__":
    main()
