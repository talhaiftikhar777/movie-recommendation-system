
import streamlit as st
import pickle
import pandas as pd

# Load pkl files
@st.cache_resource
def load_data():
    movies = pickle.load(open("movie_list.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()

# --------------------- UI STYLING ---------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered",
)

st.markdown("""
    <style>
        .title {
            font-size: 42px;
            text-align: center;
            font-weight: bold;
            color: #FF4B4B;
        }
        .recommend-box {
            padding: 18px;
            background-color: #f8f9fa;
            border-radius: 10px;
            border: 1px solid #ddd;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------- TITLE ---------------------
st.markdown('<h1 class="title">🎬 Movie Recommender System</h1>', unsafe_allow_html=True)
st.write("### Find movies similar to your favorites instantly!")

# Convert movies into DataFrame
movies_df = pd.DataFrame(movies)

# --------------------- INPUT SECTION ---------------------
st.write("### 🔍 Select a Movie")
selected_movie = st.selectbox(
    "",
    movies_df['title'].values
)

# --------------------- RECOMMENDATION FUNCTION ---------------------
def recommend(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[index]
    similar_movie_indexes = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]  # top 5 recommendations
    
    recommendations = []
    for i in similar_movie_indexes:
        recommendations.append(movies_df.iloc[i[0]].title)
    return recommendations

# --------------------- OUTPUT SECTION ---------------------
if st.button("🎯 Show Recommendations", use_container_width=True):
    recs = recommend(selected_movie)

    st.write("## ⭐ Recommended Movies")
    for r in recs:
        st.markdown(f"""
            <div class="recommend-box">
                🎥 <b>{r}</b>
            </div>
        """, unsafe_allow_html=True)
