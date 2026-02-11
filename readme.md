# 🎬 Movie Recommender System

This is a simple Movie Recommendation Web App built using **Streamlit**.  
It recommends top 5 movies based on similarity from a pre-computed movie similarity matrix.

---

## 🚀 Live Demo (Optional for Render)
Once deployed, your live app link will go here.

---

## 🧩 How It Works
- Loads movie titles and similarity matrix from `.pkl` files
- User selects a movie from a dropdown
- The app calculates and displays the top 5 similar movies

---

## 🛠️ Technologies Used

| Component | Technology |
|----------|------------|
| UI & Backend | Streamlit |
| Data Handling | Pandas |
| Model Loading | Pickle |
| Precomputed Similarity | Cosine Similarity (offline) |

---

## 📦 Project Files

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application |
| `movie_list.pkl` | Movie title storage |
| `similarity.pkl` | Similarity matrix |
| `requirements.txt` | Required libraries for deployment |
| `README.md` | Project documentation |

---

## ▶ Running Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
