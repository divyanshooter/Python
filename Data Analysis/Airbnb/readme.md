# 🏡 Airbnb Data Analysis and Visualization

This project performs an exploratory data analysis (EDA) on Airbnb listing data using Python. It involves data cleaning, transformation, and insightful visualizations using libraries like **Seaborn**, **Matplotlib**, and **Plotly**.

---

## 📁 Dataset

The dataset is read from a CSV file named `data.csv`, which contains details about Airbnb listings including prices, review dates, room types, and more.

---

## 📦 Libraries Used

- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/python/)

---

## ⚙️ Data Cleaning & Preparation

- Missing values in `'last review'` and `'reviews per month'` are handled.
- Irrelevant columns like `'house_rules'` and `'license'` are dropped.
- String prices and service fees are cleaned and converted to float.
- Duplicate entries are removed.
- Columns like `'room type'` are converted to appropriate data types.
- Unnecessary nulls in `'NAME'` and `'host name'` are dropped.

---

## 📈 Output Examples

The project provides insights like:

- Most common room types and their pricing.
- Neighborhoods with the highest number of listings.
- Review activity trends over time.
- Outlier detection in price distribution.

---

## 🛠 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/divyanshooter/python.git
   cd Data Analysis/Airbnb
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Python script:
   ```bash
   python Airbnb.py
   ```

> Ensure `data.csv` is present in the same directory as your script.

---

## 📌 To-Do (Optional Enhancements)

- Add interactive dashboards using Plotly Dash or Streamlit.
- Perform sentiment analysis on review texts.
- Build predictive models for pricing.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and submit a PR.
