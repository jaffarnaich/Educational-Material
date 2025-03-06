import streamlit as st
import random

def main():
    st.title("📅 Word of the Day")

    words = [
        {"word": "Serendipity", "meaning": "Finding something good without looking for it."},
        {"word": "Petrichor", "meaning": "The smell of the earth after rain."},
        {"word": "Supine", "meaning": "Lying on the back."},
        {"word": "Limerence", "meaning": "The state of being infatuated with another person."},
        {"word": "Nefarious", "meaning": "Wicked, villainous, or criminal."},
        {"word": "Ephemeral", "meaning": "Lasting for a very short time."},
        {"word": "Sonder", "meaning": "The realization that each passerby has a life as vivid and complex as your own."},
        {"word": "Vellichor", "meaning": "The strange wistfulness of used bookstores."},
        {"word": "Aurora", "meaning": "Dawn or sunrise."},
        {"word": "Eloquence", "meaning": "Fluent or persuasive speaking or writing."},
        {"word": "Luminescence", "meaning": "Emission of light by a substance not resulting from heat."},
        {"word": "Ebullient", "meaning": "Cheerful and full of energy."},
        {"word": "Effervescent", "meaning": "Vivacious and enthusiastic."},
        {"word": "Halcyon", "meaning": "Denoting a period of time in the past that was idyllically happy and peaceful."},
        {"word": "Ineffable", "meaning": "Too great or extreme to be expressed or described in words."},
        {"word": "Lagniappe", "meaning": "An unexpected or indirect benefit."},
        {"word": "Nemesis", "meaning": "A long-standing rival; an archenemy."},
        {"word": "Panacea", "meaning": "A solution or remedy for all difficulties or diseases."},
        {"word": "Quintessential", "meaning": "Representing the most perfect or typical example of a quality or class."},
    ]

    word = random.choice(words)

    st.subheader(f"🔹 {word['word']}")
    st.write(f"📌 Meaning: {word['meaning']}")
