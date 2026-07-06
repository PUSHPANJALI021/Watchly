# 🎬 Watchly — AI Movie Recommendation System

Watchly is a content-based movie recommendation web application built with **Python**, **Machine Learning**, and **Streamlit**. It suggests movies similar to a selected title by analyzing metadata such as genres, keywords, cast, crew, and plot overview

---

## Features

-  Content-based movie recommendations
-  Machine learning recommendation engine
-  Interactive Streamlit web interface
-  Movie poster integration via the OMDb API
-  Fast similarity search


---

##  Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Web App | Streamlit |
| Data Handling | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| NLP | NLTK |
| Serialization | Pickle |
| API Requests | Requests |
| Poster Data | OMDb API |

---
##  Project Structure

```
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
```

---

##  Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/watchly.git
```

**2. Navigate to the project directory**
```bash
cd watchly
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the application**
```bash
streamlit run app.py
```
or
```bash
python -m streamlit run app.py
```

---

##  How It Works

1. Load the TMDB movies and credits datasets
2. Merge and preprocess the movie metadata.
3. Extract genres, cast, crew, keywords, and overview.
4. Combine extracted fields into a single "tags" column per movie.
5. Vectorize tags using `CountVectorizer`.
6. Compute cosine similarity between all movie vectors.
7. Return the top 5 most similar movies for a given selection.

---



📸 Screenshots


<img width="1600" height="815" alt="image" src="https://github.com/user-attachments/assets/0a0d542c-c3c0-46df-be60-0189ec82a670" />

<img width="1600" height="836" alt="image" src="https://github.com/user-attachments/assets/5d3cd375-2a0a-4a8f-a67b-a9136d65e3a4" />

##  Future Enhancements

-  IMDb ratings integration
-  Movie trailers
-  Watchlist feature
-  Smart search
-  Enhanced Netflix-style UI
-  Cloud deployment













