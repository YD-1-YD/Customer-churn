# Customer Churn Prediction System

## 🔗 Live Demo

**Streamlit Application:**
https://customer-churn-pccvxim2xclxg7bf6z6qm2.streamlit.app/

## 🔗 GitHub Repository

**Repository:**
https://github.com/YD-1-YD/Customer-churn

---

#  Project Overview

Customer churn is one of the most critical business challenges faced by subscription-based companies. Acquiring a new customer is significantly more expensive than retaining an existing one. Therefore, identifying customers who are likely to leave a service is essential for improving customer retention and reducing revenue loss.

This project develops an end-to-end Machine Learning solution that predicts customer churn using the IBM Telco Customer Churn Dataset. The project covers the complete machine learning lifecycle, including data cleaning, exploratory data analysis, feature engineering, model building, evaluation, interpretation, and deployment.

The final solution is deployed as an interactive Streamlit web application that allows users to input customer information and obtain churn predictions in real time.

---

#  Business Problem

Telecommunication companies experience customer attrition due to various reasons such as pricing, service quality, contract terms, and customer support experiences.

The objective of this project is to:

* Identify customers who are likely to churn.
* Understand the factors influencing customer churn.
* Help businesses take proactive retention measures.
* Support data-driven decision-making using predictive analytics.

---

#  Dataset Information

### Dataset Name

IBM Telco Customer Churn Dataset

### Source

IBM Sample Data

### Dataset Size

* Rows: 7,043
* Columns: 21

### Target Variable

| Variable | Description                                     |
| -------- | ----------------------------------------------- |
| Churn    | Indicates whether the customer left the company |

### Features Include

* Customer Demographics
* Contract Information
* Internet Services
* Billing Information
* Payment Methods
* Customer Tenure

---

#  Tech Stack

## Programming Language

* Python

## Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

## Machine Learning Algorithms

* Logistic Regression
* Random Forest Classifier

## Deployment

* Streamlit Cloud

## Version Control

* Git
* GitHub

---

#  Project Workflow

## 1. Data Collection

The IBM Telco Customer Churn Dataset was imported and analyzed.

## 2. Data Cleaning

Performed:

* Removed unnecessary columns
* Converted TotalCharges to numeric format
* Handled missing values
* Checked duplicate records
* Verified data types

## 3. Exploratory Data Analysis (EDA)

Conducted detailed analysis using visualizations:

* Churn Distribution
* Contract Type Analysis
* Monthly Charges Analysis
* Tenure Analysis
* Correlation Heatmap
* Customer Segmentation Analysis

### Key Insights

* Month-to-month contract customers are more likely to churn.
* Customers with longer tenure are less likely to churn.
* Higher monthly charges increase churn probability.
* Customers using electronic checks show higher churn rates.

---

## 4. Feature Engineering

Created additional features:

### AvgMonthlySpend

Average customer spending per month.

```python
AvgMonthlySpend = TotalCharges / (tenure + 1)
```

Benefits:

* Captures customer spending behavior.
* Improves model interpretability.

---

## 5. Data Preprocessing

### Label Encoding

Applied to:

* Churn

### One-Hot Encoding

Applied to categorical features:

* Gender
* Contract
* Internet Service
* Payment Method
* Customer Service Features

---

## 6. Train-Test Split

Dataset split:

* Training Data: 80%
* Testing Data: 20%

```python
test_size = 0.2
random_state = 42
```

---

#  Machine Learning Models

## Logistic Regression

Used as a baseline classification model.

### Advantages

* Fast training
* Interpretable coefficients
* Works well on structured datasets

---

## Random Forest Classifier

Used to capture nonlinear relationships.

### Advantages

* Robust to outliers
* Handles feature interactions
* Provides feature importance scores

---

#  Model Evaluation

The following evaluation metrics were used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

---

#  Model Performance

| Metric    | Logistic Regression | Random Forest |
| --------- | ------------------- | ------------- |
| Accuracy  | 80.84%              | 78.92%        |
| Precision | 67.45%              | 63.51%        |
| Recall    | 53.74%              | 48.40%        |
| F1 Score  | 59.82%              | 54.93%        |
| ROC-AUC   | 84.67%              | 82.85%        |

---

#  Best Model

### Logistic Regression

Selected as the final model because it achieved:

* Highest Accuracy
* Highest Precision
* Highest Recall
* Highest F1 Score
* Highest ROC-AUC Score

Final ROC-AUC Score:

**84.67%**

---

#  Confusion Matrix Analysis

The confusion matrix was used to evaluate:

* True Positives
* True Negatives
* False Positives
* False Negatives

Business interpretation:

Reducing false negatives is critical because failing to identify a customer who is likely to churn can result in revenue loss.

---

#  Feature Importance Analysis

Top churn influencing factors identified:

1. TotalCharges
2. Tenure
3. AvgMonthlySpend
4. MonthlyCharges
5. InternetService_Fiber Optic
6. PaymentMethod_Electronic Check
7. Contract_Two Year
8. PaperlessBilling
9. OnlineSecurity
10. Gender

---

#  Deployment

The final model was deployed using Streamlit Cloud.

Features:

* Interactive user interface
* Real-time churn prediction
* Probability-based output
* Cloud-hosted application

---

#  Application Screenshots

### Customer Churn Prediction Dashboard

<img width="1919" height="968" alt="image" src="https://github.com/user-attachments/assets/07f3fdb2-efbd-4363-bcfe-50235603ded5" />



### ROC Curve

<img width="536" height="393" alt="ROC Curve" src="https://github.com/user-attachments/assets/ced6dcc4-177d-4a4a-800e-a88776afe592" />


### Feature Importance Plot

<img width="1057" height="547" alt="Feature importance" src="https://github.com/user-attachments/assets/f4897554-4aae-4019-b81f-a5501ca65a8a" />

### Confusion Matrix

<img width="510" height="393" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/7b344d02-bade-4a2a-994a-921436c8e5b8" />

---

# 💡 Business Recommendations

Based on the analysis:

### 1. Encourage Long-Term Contracts

Customers with month-to-month contracts exhibit higher churn rates.

### 2. Improve Customer Retention Programs

Focus on customers with:

* High monthly charges
* Short tenure

### 3. Strengthen Customer Support

Provide incentives and proactive engagement for high-risk customers.

### 4. Target At-Risk Segments

Use churn prediction scores to prioritize retention campaigns.

---

# 🔮 Future Improvements

Planned enhancements:

* XGBoost Implementation
* Hyperparameter Tuning using GridSearchCV
* Cross Validation
* SHAP Explainability
* Docker Containerization
* AWS Deployment
* CI/CD Pipeline
* MLflow Experiment Tracking

---

#  Project Structure

```text
Customer-churn/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│
├── models/
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb
│
├── reports/
│
├── src/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Author

**YD Mallikarjuna**
Aspiring Data Scientist | Machine Learning Enthusiast | B.Tech CSE-AIML Student

---

---

## Open to Collaborate

I am continuously working to improve this project by adding advanced machine learning techniques, better model explainability, and production-grade deployment features.

If you're interested in contributing, collaborating, or discussing ideas to enhance this project, feel free to connect with me. Contributions, suggestions, and feedback are always welcome!

📧 Feel free to reach out and let's build something impactful together.

⭐ If you find this project useful, consider giving it a star and sharing your feedback.
