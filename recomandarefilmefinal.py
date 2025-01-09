import json
import streamlit as st

def load_movies(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def recommend_movies(movies, preferred_genres):
    recommendations = []
    for movie in movies:
        if any(genre in preferred_genres for genre in movie["genre"]):
            recommendations.append(movie["title"])
    return recommendations


def main():
    st.title("Recomandări de Filme 🎬")

    movies = load_movies("movies.json")
    name = st.text_input("Introduceți numele dvs.:")
    genres = ["Action", "Drama", "Sci-Fi", "Thriller", "Crime", "Comedy", "Horror"]
    preferred_genres = st.multiselect("Selectați genurile preferate:", genres)

    if st.button("Sugerează filme"):
        if name and preferred_genres:
            recommendations = recommend_movies(movies, preferred_genres)
            if recommendations:
                st.write(f"Filme recomandate pentru {name}:")
                for movie in recommendations:
                    st.write(f"- {movie}")
            else:
                st.write("Nu există filme care să corespundă genurilor selectate.")
        else:
            st.write("Vă rugăm să completați toate câmpurile.")

if __name__ == "__main__":
    main()