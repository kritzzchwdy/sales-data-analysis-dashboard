# 📊 Sales Data Analysis Dashboard

A data analytics project built as part of the **Navyan Internship Program**.  
This project analyzes sales data to uncover business insights through cleaning, analysis, and visualization using Python.

---

## 🔍 Project Overview

This project simulates how companies analyze their sales data to make better decisions.  
It transforms raw sales records into a visual dashboard that tracks performance, profit trends, and regional growth.

---

## 📁 Dataset

- **Source:** [Kaggle — Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Columns Used:** Order ID, Product, Category, Sales, Profit, Order Date, Region

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data loading, cleaning, analysis |
| Matplotlib | Data visualization & dashboard |
| NumPy | Numerical operations |

---

## 📌 Steps Performed

1. **Load** — Imported dataset using Pandas
2. **Clean** — Handled missing values, fixed date formats, removed duplicates
3. **Analyze** — Calculated total sales, profit, profit margin, top products & regions
4. **Visualize** — Built a 5-chart dashboard using Matplotlib

---

## 📊 Dashboard Preview

> Run the script to generate `sales_dashboard.png`

The dashboard includes:
- 🏆 Top 5 Products by Sales
- 🌍 Sales by Region
- 📦 Category Distribution (Pie Chart)
- 📅 Monthly Sales Trend (Line Chart)
- 💹 Profit by Category

---

## ▶️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/kritzzchwdy/sales-data-analysis-dashboard.git

# 2. Install dependencies
pip install pandas matplotlib numpy

# 3. Run the script
python sales_dashboard.py
```

> If you have the Superstore CSV, place it in the same folder and uncomment the `pd.read_csv()` line in the script.

---

## 📈 Key Metrics Output (Sample)

```
✅ Dataset loaded and cleaned.
💰 Total Sales   : ₹7,43,210
📈 Total Profit  : ₹1,28,540
📊 Profit Margin : 17.3%
```

---

## 📂 Project Structure

```
sales-data-analysis-dashboard/
│
├── sales_dashboard.py     # Main Python script
├── sales_dashboard.png    # Output dashboard image
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## 👩‍💻 Author

Kritika Chaudhary
BTech CSE | IMS Engineering College  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/kritika-chaudhary-619664327)

---

## 📜 License

This project was completed as part of the Navyan Internship Program.  
For reference and learning purposes only.
