# Credit Card Churn Analysis

## Project Overview

This project analyzes customer churn in the banking sector using Python, SQL, and Excel. The goal is to understand customer behavior, identify the factors contributing to churn, and gain business insights through Exploratory Data Analysis (EDA).

The project demonstrates an end-to-end analytics workflow including dataset inspection, data cleaning using Pandas, feature engineering with SQL, and visualization using Python libraries.

---

## Objectives

- Inspect and understand the raw dataset.
- Clean and preprocess customer data using Python (Pandas).
- Create additional business features using SQL joins.
- Perform Exploratory Data Analysis (EDA).
- Generate insights about customer churn.

---

## Tools & Technologies

- Microsoft Excel (Dataset Inspection)
- MySQL (SQL Joins & Feature Engineering)
- Python
- Pandas
- Matplotlib
- Seaborn

---

## Project Workflow

### 1. Dataset Inspection
- Loaded and reviewed the raw dataset in Microsoft Excel.
- Understood the dataset structure and column information.

### 2. Data Cleaning (Python - Pandas)
- Checked missing values.
- Removed inconsistencies.
- Verified data types.
- Cleaned and prepared the dataset for analysis.

### 3. Feature Engineering (SQL)
Used SQL joins to create two additional business-related features:
- Reward_Rate
- Annual_Fee

The enriched dataset was exported as **Final_Bank_Churners.csv** for analysis.

### 4. Exploratory Data Analysis (EDA)

Performed EDA using:
- Pandas
- Matplotlib
- Seaborn

Created visualizations including:
- Count Plots
- Bar Charts
- Box Plots
- Histograms
- Correlation Analysis

---

## Key Insights

- Approximately **84%** of customers are existing customers, while **16%** have churned.
- Customer demographics influence churn patterns.
- Credit utilization varies across customer groups.
- Different card categories show different churn behavior.
- Reward Rate and Annual Fee provide additional business context for customer analysis.

---

## Project Structure

```
Credit-Card-Churn-Analysis/
│
├── BankChurners.csv
├── cleaned_bank_churners.csv
├── Final_Bank_Churners.csv
├── data_cleaning.py
├── eda.py
├── credit_card_churn.sql
├── churn_rate_1.sql
├── churn_rate_2.sql
├── cleaned_final_table.sql
├── screenshots/
├── README.md
└── requirements.txt
```

---

## Skills Demonstrated

- Data Cleaning using Pandas
- SQL Joins
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Data Visualization
- Business Insight Generation
- Python Programming
- SQL Query Writing

---

## Libraries Used

- Pandas
- Matplotlib
- Seaborn

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Build machine learning models for churn prediction.
- Compare multiple classification algorithms.
- Develop an interactive dashboard using Power BI or Streamlit.

---

## Author

**Vanshdeep Sharma**

Aspiring Data Analyst

- GitHub: https://github.com/VanshdeepSharma2005
- LinkedIn: *(Add your LinkedIn profile link here.)*
