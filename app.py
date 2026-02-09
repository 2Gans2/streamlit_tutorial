import streamlit as st
from string import ascii_letters, digits, punctuation
import random


st.title("Генератор паролей")
length = st.slider("Длинна", 8, 24, 16)
special_characters = st.checkbox("Использовать спецсимволы")
if st.button("Создать"):
    characters = ascii_letters + digits
    if special_characters:
        characters += punctuation
    password = "".join(random.choices(characters, k=length))
    st.code(password, language="text")
