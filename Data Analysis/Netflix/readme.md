# 🎬 Netflix Movies Data Analysis

This project explores a dataset of movies available on Netflix. The analysis focuses on understanding patterns in movie genres, popularity, vote averages, and yearly trends in movie releases.

---

## 📁 Dataset

- **Filename**: `movies data.csv`
- **Rows**: 9,827  
- **Columns**: 9  
- **Key Columns**: `Title`, `Genre`, `Vote_Average`, `Popularity`, `Release_Date`

---

## 📊 Exploratory Data Analysis (EDA)

### 🔍 Initial Observations

- Dataset contains **9,827 rows and 9 columns**.
- **No missing or duplicate values** initially.
- `Release_Date` column is converted to **year** for simplification.
- Columns like `Overview`, `Original_Language`, and `Poster_Url` were **dropped** as they are not required for the analysis.
- `Genre` contains **comma-separated** values and was **split and exploded** into individual rows for each genre.

### 🧼 Data Preprocessing

- `Vote_Average` column categorized into:
  - **Not Popular**
  - **Below Average**
  - **Average**
  - **Popular**
  
- `Genre` column converted to `category` datatype for efficient analysis.
- Visualizations generated using **Seaborn** and **Matplotlib**.

---

## 🧠 Key Insights

- 🎭 **Most Common Genre**: Drama
- ⭐ **Highest Vote Category**: Average (~25.88%)
- 🔥 **Most Popular Movie**: *Spider-Man: No Way Home* (Genres: Action, Adventure, Science Fiction)
- 🧊 **Least Popular Movies**:
  - *The United States vs. Billie Holiday* (Genres: Music, History, Drama)
  - *Threads* (Genres: Drama, War, Science Fiction)
- 📆 **Year with Most Movies Released**: 2021 (~1,636 movies)

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib

---

## 📂 Project Structure

```
📁 netflix-movie-analysis
│
├── 📄 movies data.csv
├── 📄 Netflix.py
└── 📄 README.md
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/divyanshooter/python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd netflix-movie-analysis
   ```
3. Run the EDA script:
   ```bash
   python Netflix.py
   ```

---
