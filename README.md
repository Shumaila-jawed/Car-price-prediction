# Car-price-prediction
Car price predictor app
# 🚗 Car Price Prediction using Machine Learning

Predict the estimated price of a used car using Machine Learning and an interactive Streamlit web application.

---

## 📌 Project Overview

This project uses a trained Machine Learning model to predict car prices based on several features such as:

- Brand
- Model
- Manufacturing Year
- Engine Size
- Fuel Type
- Transmission
- Mileage
- Condition

The application is built with **Python**, **Scikit-learn**, and **Streamlit**, providing a simple and user-friendly interface for making predictions.

---

## ✨ Features

- Predict car prices instantly
- Interactive Streamlit web application
- Machine Learning Regression Model
- One-Hot Encoding for categorical variables
- Clean and responsive interface
- Easy to deploy on Hugging Face Spaces or Streamlit Cloud

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

## 📂 Project Structure

```
Car-Price-Prediction/
│
├── app.py
├── model.pkl
├── feature_names.pkl
├── requirements.txt
├── README.md
├── dataset.csv
└── notebook.ipynb
```

---

## 📊 Input Features

### Numerical Features

- Year
- Engine Size
- Mileage

### Categorical Features

- Brand
- Model
- Fuel Type
- Transmission
- Condition

---

## ⚙️ Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. One-Hot Encoding
6. Train/Test Split
7. Model Training
8. Model Evaluation
9. Save Model using Joblib
10. Build Streamlit Web App
11. Deploy Application

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Car-Price-Prediction.git
```

Move into the project directory

```bash
cd Car-Price-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📈 Model Inputs

The model expects the following information:

- Brand
- Model
- Year
- Engine Size
- Fuel Type
- Transmission
- Mileage
- Condition

These features are automatically converted into the encoded format before prediction.

---

## 📷 Application Preview

*(Add screenshots here after deployment.)*

Example:

```
Home Page Screenshot

Prediction Result Screenshot
```

---

## 📌 Future Improvements

- Add more car brands
- Improve model accuracy
- Deploy on Hugging Face Spaces
- Add data visualization dashboard
- Support multiple ML models for comparison

---

## 👩‍💻 Author

**Shumaila**

AI | Machine Learning | Data Science | AI Automation

---

## ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
