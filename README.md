# Diabetic Retinopathy Prediction

![Model Comparison]![image](https://github.com/user-attachments/assets/1736c698-adc7-4191-b444-e5249942c8b0)


## 📌 Project Overview

This project predicts **Diabetic Retinopathy** using patient health indicators:
- Age
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Cholesterol

It uses a **trained machine learning model** and a **Streamlit web interface** for real-time predictions, helping in **early screening and awareness**.

---

## ⚙️ Features

✅ Clean, interactive **Streamlit app** for user-friendly predictions.  
✅ Multiple models evaluated (Logistic Regression, Decision Tree, SVM, Neural Network, etc.).  
✅ Final model deployed for instant predictions.  
✅ Visual comparison of model accuracies for transparency.

---

## 🚀 How to Run Locally

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/SukanyaVarpe/Diabetic-Retinopathy-Prediction.git
cd Diabetic-Retinopathy-Prediction
2️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
🩺 Model Details
Features Used: Age, Systolic BP, Diastolic BP, Cholesterol

Models Compared:

Logistic Regression

Decision Tree

Random Forest

SVM

Gradient Boosting

XGBoost

KNN

Neural Network (MLP)

Best Accuracy Achieved: ~75.24% using Neural Network (MLP)

🛠️ Dependencies
Python 3.x

Streamlit

Pandas

Numpy

Joblib

Scikit-learn

Matplotlib

Seaborn

📊 Example Screenshots
Model Accuracy Comparison Chart:



Streamlit Prediction Interface:![image](https://github.com/user-attachments/assets/983831ad-9b3d-406d-a28e-10f070934fc9)

✍️ Usage
Enter patient values:

Age (35.16 - 103.28)

Systolic BP (69.67 - 151.70)

Diastolic BP (62.81 - 133.46)

Cholesterol (69.97 - 148.23)

Click Predict.

The app will display:

✅ “NO Diabetic Retinopathy.” or

❌ “Diabetic Retinopathy Detected.”
