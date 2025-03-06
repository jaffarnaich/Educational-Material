import streamlit as st
from googletrans import Translator

def show_translation_page():
    st.title("🌍 Translation Page")
    text = st.text_area("Enter text to translate:")
    target_language = st.selectbox("Select target language:", ["eng","fr", "es", "ur", "hi"])

    if st.button("Translate"):
        if text:
            translator = Translator(to_lang=target_language)
            translated_text = translator.translate(text)
            st.success(f"**Translated Text:** {translated_text}")
        else:
            st.warning("⚠️ Please enter text to translate.")

if __name__ == "__main__":
    show_translation_page()
