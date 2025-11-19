# 📘 Bankruptcy Prediction Model (93% Accuracy)

A machine learning system that predicts whether a company is likely to go bankrupt based on financial indicators.  
Built using **Random Forest**, deployed using **Streamlit**, and trained on structured financial ratio data.

---

## 🚀 Features
- Predicts company bankruptcy risk with **93% accuracy**
- Streamlit web application with clean UI
- Real-time financial input table
- Clipboard auto-fill for faster testing
- Financial ratio–based feature engineering
- Suitable for investors, analysts, and finance teams

---

## 🧠 Tech Stack

| Category | Tools Used |
|---------|-------------|
| **Programming** | Python |
| **Machine Learning** | Random Forest, Logistic Regression, SVM, Decision Tree |
| **Libraries** | Pandas, NumPy, Scikit-Learn |
| **Web App** | Streamlit |
| **Notebooks** | Jupyter Notebook |
| **Visualization** | Matplotlib, Seaborn |

---

## 📊 Model Performance

- **Accuracy:** 93%  
- **Precision & Recall:** High  
- **Balanced F1 Score**  
- Handles imbalanced bankruptcy datasets effectively  
- Important predictors include:
  - ROA (Return on Assets)
  - Debt Ratio
  - Net Income
  - Working Capital

---

## 📁 Project Structure

bankruptcy-prediction-model/
│
├── stream.py # Streamlit web application
├── random_forest_model.pkl # Trained Random Forest model
├── american_bankruptcy.csv # Dataset used for training/testing
├── us-company-bankruptcy.ipynb # Full machine learning pipeline
├── .gitignore # Ignored system files
└── README.md # Project documentation



## 🖥 Run the Web App Locally

### 1️⃣ Create a virtual environment
```bash
python -m venv venv
2️⃣ Activate it
venv\Scripts\activate
3️⃣ Install dependencies
pip install streamlit pandas numpy scikit-learn pyperclip
4️⃣ Run the app
streamlit run stream.py

🔍 Sample Prediction Output
The app predicts one of the following:


✅ Company is Alive


⚠️ Company can Fail



🔮 Future Enhancements


Cloud deployment (Streamlit Cloud)


Add Deep Learning models (LSTM/ANN)


Industry-specific bankruptcy analysis


Automated feature extraction



👩‍💻 Developer
Janhavi Sunil Rewale
Data Science Student

---

