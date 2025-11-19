📘 Bankruptcy Prediction Model (93% Accuracy)

A machine-learning system that predicts whether a company is likely to go bankrupt using key financial indicators.
Built using Random Forest, deployed with Streamlit, and trained on structured financial ratio data.

🚀 Features

Predicts company bankruptcy risk

User-friendly Streamlit interface

Real-time input table

Clipboard auto-fill for quick testing

Financial ratio–based model

Random Forest classifier with 93% accuracy

🧠 Tech Stack
Area	Tools
Programming	Python
ML Models	Random Forest, Logistic Regression, SVM, Decision Tree
Libraries	Pandas, NumPy, Scikit-Learn
Web App	Streamlit
Notebooks	Jupyter Notebook
📊 Model Performance

Accuracy: 93%

Precision: High

Recall: High

F1 Score: Balanced

Uses feature importance to select top predictors like:

ROA

Debt Ratio

Net Income

Working Capital

📁 Project Structure
bankruptcy-prediction-model/
│
├── stream.py                     # Streamlit web application
├── random_forest_model.pkl       # Trained Random Forest model
├── american_bankruptcy.csv       # Dataset used for training
├── us-company-bankruptcy.ipynb   # Full machine learning pipeline
├── README.md                     # Documentation
└── .gitignore

🖥 Run the Web App Locally
1️⃣ Create a virtual environment
python -m venv venv

2️⃣ Activate it
venv\Scripts\activate

3️⃣ Install dependencies
pip install streamlit pandas numpy scikit-learn pyperclip

4️⃣ Run the app
streamlit run stream.py


Your app will open automatically in your browser.

📈 Sample Model Prediction

The app outputs one of the following:

Company is Alive ✔

Company can Fail ⚠️

Based on finance-based features entered by the user.

🔮 Future Improvements

Cloud deployment (Streamlit Cloud / Render)

Add LSTM or Deep Learning models

Auto-feature extraction

Industry segmentation

👩‍💻 Developer

Janhavi Sunil Rewale
Data Science Student
