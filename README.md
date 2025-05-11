# Breast Cancer Prediction Web App

This is a Flask web application that predicts whether a tumor is **Malignant** or **Benign** using a Logistic Regression model trained on the Breast Cancer Wisconsin (Diagnostic) dataset.

## 🚀 Features

- Web-based form to input tumor characteristics
- Logistic Regression model with `scikit-learn`
- Data preprocessing with `StandardScaler`
- Accuracy, classification report, and confusion matrix evaluation
- Clean separation between front-end (HTML) and back-end (Python)

---

## 🧠 Machine Learning Model

### Dataset

- File: `data.csv`
- Source: Breast Cancer Wisconsin (Diagnostic) Data Set
- Target Variable: `diagnosis` (`M` for Malignant, `B` for Benign)

### Preprocessing

- Dropped unnamed column (column index 32)
- Features scaled using `StandardScaler`
- Train/Test split: 80/20

### Model

- Algorithm: Logistic Regression
- Parameters: `max_iter=1000`, `solver='lbfgs'`
- Accuracy: ~Printed in console at runtime

---

## 🛠 Installation

### Requirements

- Python 3.x
- Flask
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

### Install dependencies

```bash
pip install flask numpy pandas scikit-learn matplotlib seaborn
```

---

## 📂 Project Structure

```
├── app.py                 # Flask backend
├── code_1.py              # ML model & predict_diagnosis function
├── templates/
│   └── index.html         # Frontend form
├── Breast_cancer_prediction/
│   └── data.csv           # Dataset
└── README.md              # This file
```

---

## 🧪 How to Run

1. Place `data.csv` in the `Breast_cancer_prediction/` folder.
2. Make sure `code_1.py` contains the `predict_diagnosis()` function.
3. Start the Flask app:

```bash
python app.py
```

4. Open the link in your browser.
5. Input tumor metrics and get the prediction.

---

