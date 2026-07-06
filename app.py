import streamlit as st
import pickle
import requests

# ==========================
# OMDb API Key
# ==========================
API_KEY = "25d197e"   # <-- put your real key here

# ==========================
# Load Data
# ==========================
movies = pickle.load(open('dataset/movie_list.pkl', 'rb'))
similarity = pickle.load(open('dataset/similarity.pkl', 'rb'))

# ==========================
# Fetch Movie Poster
# ==========================
def fetch_poster(movie_name):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={"25d197e"}"

    response = requests.get(url) 

    data = response.json()

    if data.get("Response") == "True":
        poster = data.get("Poster", "")
        return poster if poster != "N/A" else ""
    return ""

# ==========================
# Recommendation Function
# ==========================
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_name = movies.iloc[i[0]].title
        recommended_movies.append(movie_name)
        recommended_posters.append(fetch_poster(movie_name))

    return recommended_movies, recommended_posters

# ==========================
# Streamlit UI
# ==========================
st.set_page_config(page_title="Watchly", page_icon="🎬")

st.title("🎬 Watchly")
st.write("Find movies similar to your favorite one!")

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(len(names))

    for i in range(len(names)):
        with cols[i]:
            if posters[i]:
                st.image(posters[i])
            st.caption(names[i])