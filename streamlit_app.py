import streamlit as st
from transformers import pipeline

# Tytuł i obraz nagłówkowy
st.title("📊 Aplikacja NLP - Analiza Wydźwięku i Tłumaczenie Tekstu")
st.image("komunikacja.jpg", caption="Analiza tekstu i tłumaczenie na żywo")

# Wprowadzenie
st.subheader("Automatyczna analiza tekstu i tłumaczenie")
st.write("Witaj w aplikacji do analizy wydźwięku oraz tłumaczenia tekstu! "
         "To narzędzie pozwala na ocenę emocjonalnego wydźwięku tekstu w języku angielskim "
         "oraz tłumaczenie tekstu na język niemiecki.")

# Powitanie i efekt startowy
st.success('Aplikacja uruchomiona pomyślnie! Wybierz opcję, aby kontynuować.')
st.balloons()

# Wybór opcji
option = st.selectbox(
    "Wybierz opcję:",
    [
        "Analiza wydźwięku emocjonalnego (angielski)",
        "Tłumaczenie tekstu z angielskiego na niemiecki",
    ],
)

# Sekcja dla analizy wydźwięku
if option == "Analiza wydźwięku emocjonalnego (angielski)":
    st.subheader("Analiza Wydźwięku Emocjonalnego")
    text = st.text_area(label="Wpisz tekst po angielsku:")
    if text:
        try:
            with st.spinner("Analizuję wydźwięk..."):
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)
                st.success("Analiza zakończona!")
                st.write("Wynik analizy:", answer)
        except Exception as e:
            st.error("Wystąpił błąd podczas analizy. Spróbuj ponownie.")

# Sekcja dla tłumaczenia tekstu
elif option == "Tłumaczenie tekstu z angielskiego na niemiecki":
    st.subheader("Tłumaczenie Tekstu na Język Niemiecki")
    text = st.text_area(label="Wpisz tekst po angielsku:")

    if text:
        try:
            with st.spinner("Tłumaczę..."):
                translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
                translation = translator(text)
                st.success("Tłumaczenie zakończone!")
                st.write("Przetłumaczony tekst:", translation[0]['translation_text'])
        except Exception as e:
            st.error("Wystąpił błąd podczas tłumaczenia. Spróbuj ponownie.")

# Instrukcja użytkowania
st.header("📜 Instrukcja")
st.write("1. Wybierz opcję: analiza wydźwięku lub tłumaczenie.")
st.write("2. Wpisz tekst w języku angielskim.")
st.write("3. Odczytaj wynik analizy lub tłumaczenia poniżej pola tekstowego.")

# Informacja o autorze
st.write("🔖 Projekt wykonany przez s26132")