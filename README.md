🎬 Watchly — AI Movie Recommendation System

Watchly is a content-based movie recommendation web application built with Python, Machine Learning, and Streamlit. It suggests movies similar to a selected title by analyzing metadata such as genres, keywords, cast, crew, and plot overview.


 Features


🎥 Content-based movie recommendations
🤖 Machine learning recommendation engine
🍿 Interactive Streamlit web interface
🖼️ Movie poster integration via the OMDb API
⚡ Fast similarity search

 Tech Stack

CategoryToolsLanguagePythonWeb AppStreamlitData HandlingPandas, NumPyMachine LearningScikit-learnNLPNLTKSerializationPickleAPI RequestsRequestsPoster DataOMDb API


📂 Project Structure

Watchly/
│
├── app.py
├── dataset/
│   ├── movie_list.pkl
│   ├── similarity.pkl
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── README.md
└── requirements.txt




📊 How It Works


Load the TMDB movies and credits datasets.
Merge and preprocess the movie metadata.
Extract genres, cast, crew, keywords, and overview.
Combine extracted fields into a single "tags" column per movie.
Vectorize tags using CountVectorizer.
Compute cosine similarity between all movie vectors.
Return the top 5 most similar movies for a given selection.



📸 Screenshots


<img width="1600" height="815" alt="image" src="https://github.com/user-attachments/assets/0a0d542c-c3c0-46df-be60-0189ec82a670" />




📁 Dataset


TMDB 5000 Movies Dataset
TMDB 5000 Credits Dataset



🔮 Future Enhancements

⭐ IMDb ratings integration
🎞️ Movie trailers
❤️ Watchlist feature
🔍 Smart search
🌙 Enhanced Netflix-style UI
☁️ Cloud deployment









