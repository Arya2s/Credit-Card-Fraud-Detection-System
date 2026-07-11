# 💳 Credit Card Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 💳 Credit Card Fraud Detection System

A Machine Learning web application that detects fraudulent credit card transactions using a *Random Forest Classifier. The application is built with **Python* and *Streamlit*, allowing users to test transactions using random samples or manually entered values.

---

## 📌 Features

- Detect fraudulent credit card transactions.
- Random transaction testing using the processed dataset.
- Manual transaction prediction.
- Displays Fraud Probability (Risk Score).
- User-friendly Streamlit web interface.
- Built using a Random Forest Machine Learning model.

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📂 Project Structure


Credit-Card-Fraud-Detection-System/
│
├── app.py                  # Streamlit Web Application
├── credit card.ipynb       # Model Training Notebook
├── fraud_model.pkl         # Trained Random Forest Model
├── columns.pkl             # Saved Feature Columns
├── .gitignore
└── README.md


> *Note:* The dataset is intentionally *not uploaded* to GitHub because it is large and available publicly on Kaggle.

---

# 📊 Dataset

This project uses the *Credit Card Fraud Detection Dataset* from Kaggle.

Dataset Link:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## Dataset Setup

### Step 1

Download the dataset from Kaggle.

The downloaded file is named:


creditcard.csv


Place this file in the project folder.

---

### Step 2

Run the Jupyter Notebook:


credit card.ipynb


The notebook performs:

- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Saves the trained model

After preprocessing, save the processed dataset as:


processed_data.csv


This file is required for running the Streamlit application.

---

## Required Files

After running the notebook, your project folder should contain:


app.py
credit card.ipynb
fraud_model.pkl
columns.pkl
creditcard.csv
processed_data.csv


---

# ▶️ Run the Application

Open the project folder in VS Code.

Open the terminal and run either:

bash
streamlit run app.py


or

bash
python -m streamlit run app.py


The application will open in your browser at:


http://localhost:8501


---

# 🚀 How the Application Works

### Random Sample

- Selects a random transaction from the processed dataset.
- Predicts whether the transaction is fraudulent.
- Displays the fraud probability.

### Manual Input

- Users can manually enter transaction details.
- Predicts fraud probability using the trained Random Forest model.

---

# 🤖 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

The model was trained using the processed credit card fraud dataset.

---

# 📈 Output

The application classifies transactions into:

- ✅ Safe Transaction
- ⚠️ Medium Risk Transaction
- 🚨 Fraudulent Transaction

along with the fraud probability score.

---

# ⚠️ Important Notes

- The original dataset (creditcard.csv) is *not included* in this repository because of its large size.
- Before running app.py, make sure you have:
  - Downloaded creditcard.csv from Kaggle.
  - Executed credit card.ipynb.
  - Generated processed_data.csv.
  - Generated fraud_model.pkl.
  - Generated columns.pkl.

Without these files, the Streamlit application will not run correctly.

---

# 👨‍💻 Author

*Arya2s*

GitHub:
https://github.com/Arya2s

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub!
