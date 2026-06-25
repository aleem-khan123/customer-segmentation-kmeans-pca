# Customer Segmentation using PCA and K-Means Clustering

## Project Overview

This project applies Unsupervised Machine Learning techniques to identify meaningful customer groups based on demographic and spending behavior.

The workflow includes data preprocessing, feature scaling, dimensionality reduction using Principal Component Analysis (PCA), customer segmentation using K-Means Clustering, and visualization through Tableau and Streamlit dashboards.

The goal is to transform raw customer data into actionable business insights and customer personas.

---

## Business Problem

Businesses often collect customer information but struggle to identify distinct customer groups.

Customer segmentation helps organizations:

- Understand customer behavior
- Create targeted marketing campaigns
- Improve customer retention
- Increase revenue through personalized strategies

---

## Dataset Information

Dataset: Mall Customers Dataset

Features:

- CustomerID
- Gender
- Age
- Annual Income
- Spending Score

Dataset Size:

- Records: 200
- Features: 5

---

## Project Workflow

### 1. Data Understanding

- Dataset exploration
- Missing value analysis
- Duplicate record checking
- Statistical summary

### 2. Data Preprocessing

- Removed CustomerID
- Label Encoding for Gender
- Feature Scaling using StandardScaler

### 3. Exploratory Data Analysis

- Gender Distribution
- Age Distribution
- Income Distribution
- Spending Score Distribution
- Correlation Heatmap

### 4. Principal Component Analysis (PCA)

PCA was used to reduce dimensionality while preserving important information.

Results:

- Original Features: 4
- Principal Components: 2
- Variance Retained: ~60%

### 5. K-Means Clustering

Customer segmentation was performed using K-Means Clustering.

Cluster selection techniques:

- Elbow Method
- Silhouette Score

Optimal Number of Clusters:

K = 4

### 6. Customer Persona Development

Clusters were analyzed and converted into business-friendly customer personas.

---

## Customer Personas

| Cluster | Persona | Characteristics |
|----------|----------|----------------|
| 0 | High-Value Customers | High Income, High Spending |
| 1 | Conservative Customers | High Income, Low Spending |
| 2 | Budget-Conscious Customers | Lower Income, Lower Spending |
| 3 | Young Spenders | Moderate Income, High Spending |

---

## Key Insights

- Four distinct customer groups were identified.
- High-Value Customers represent the most profitable segment.
- Young Spenders show strong purchasing behavior despite moderate income.
- Budget-Conscious Customers respond better to discounts and promotions.
- Different marketing strategies can be applied to each segment.

---

## Streamlit Dashboard

The project includes an interactive Streamlit dashboard featuring:

- Executive Summary
- Dataset Overview
- Customer Demographics
- Correlation Analysis
- PCA Visualization
- Cluster Analysis
- Customer Personas
- Business Insights

Run Dashboard:

```bash
streamlit run app.py
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- Tableau

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Unsupervised Learning
- Data Preprocessing
- Standardization
- PCA
- K-Means Clustering
- Elbow Method
- Silhouette Score
- Customer Persona Creation
- Data Visualization
- Streamlit Dashboard Development

---

## Repository Structure

```text
Dataset/
Notebook/
Charts/
Dashboard/
Report/
README.md
requirements.txt
```

---

## Author

Aleem Shoukat

GitHub:
(https://github.com/aleem-khan123)

LinkedIn:
https://www.linkedin.com/in/aleem-shoukat-9bb3b6356/
