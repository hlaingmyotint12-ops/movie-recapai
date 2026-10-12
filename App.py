
import streamlit as st

st.set_page_config(
    page_title="Movie Recap App",
    page_icon="🎬"
)

st.title("🎬 Movie Recap App")

st.write("Welcome to my Movie Recap App!")

movie_name = st.text_input("Enter movie name")

if st.button("Generate Recap"):
    if movie_name:
        st.subheader("Movie Recap")
        st.write(
            f"You selected the movie: {movie_name}"
        )
    else:
        st.warning("Please enter a movie name.")
      
