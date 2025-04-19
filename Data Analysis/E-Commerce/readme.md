# 📊 Sales & Profit Analysis Dashboard

This project performs an interactive analysis of sales and profit data using **Pandas** for data manipulation and **Plotly** for data visualization. The dataset is preprocessed and visualized to explore trends across time, categories, sub-categories, and segments.

---

## 📁 Dataset

The dataset (`data.csv`) is expected to be in the root directory or `./data.csv`. It includes order details such as:

- `Order Date`
- `Segment`
- `Category`
- `Sub-Category`
- `Sales`
- `Quantity`
- `Profit`

---

## 🧰 Tools Used

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Plotly](https://plotly.com/python/)

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/divyanshooter/python.git
   cd Data Analysis/E-Commerce
   ```

2. **Install dependencies:**
   We recommend using a virtual environment.

   ```bash
   pip install pandas numpy plotly
   ```

3. **Add your data file:**
   Place `data.csv` in the project root directory.

---

## 📈 Analysis Performed

- ✔️ Removed unused columns and transformed date data
- ✔️ Extracted day, month, and year from `Order Date`
- ✔️ Checked for nulls and duplicates
- ✔️ Aggregated sales and profit by:
  - Month
  - Category
  - Sub-category
  - Segment
- ✔️ Visualized data using:
  - Line Charts (Sales/Profit by Month)
  - Bar Charts (Sales/Profit by Category and Sub-category)
  - Donut Pie Chart (Category-wise Sales Distribution)
  - Grouped Bar Chart (Sales vs Profit by Segment)

---

## 📊 Sample Visuals

- **Sales by Month**  
  Line chart showing monthly sales trends.

- **Category-wise Sales**  
  Bar and donut charts showing sales split across categories.

- **Sub-category Analysis**  
  Bar charts showing detailed breakdowns of sales and profits.

- **Segment Analysis**  
  Comparative bar chart showing sales and profit by segment.

---

## 📌 Key Insights

- No missing or duplicate values in the dataset.
- Sales and profits are seasonally distributed, with peaks in certain months.
- Technology category shows significant sales contribution.
- Consumer segment has the highest sales and profit ratio.

---

## ▶️ How to Run

1. Ensure `data.csv` is present in the directory.
2. Run the script:

   ```bash
   python E-Commerce.py
   ```

3. Interactive charts will pop up in your browser.

---

## 📂 File Structure

```
sales-profit-analysis/
│
├── data.csv                # Sales dataset
├── E-Commerce.py           # Main analysis script
├── README.md               # You're here
```

---

## 🧠 Future Enhancements

- Add interactive dashboards with Dash or Streamlit
- Automate EDA report generation
- Add more detailed KPIs

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---
