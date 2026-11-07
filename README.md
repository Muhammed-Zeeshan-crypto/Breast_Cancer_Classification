# Breast Cancer Classification

A beginner-friendly Machine Learning project that predicts whether a breast tumor is **Benign** or **Malignant** using Logistic Regression.

## Project Overview

This project uses the Breast Cancer Wisconsin dataset available in Scikit-learn to train a Logistic Regression model.

A Streamlit web application allows users to enter tumor measurements and receive a prediction.

## Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Matplotlib

## Machine Learning Algorithm

**Logistic Regression**

The model is trained using five features from the dataset:

- Mean Radius
- Mean Texture
- Mean Perimeter
- Mean Area
- Mean Smoothness

## Project Structure

```text
Breast_Cancer_Classification/
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Muhammed-Zeeshan-crypto/Breast_Cancer_Classification.git
```

Navigate to the project folder:

```bash
cd Breast_Cancer_Classification
```

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

## Train the Model

Run the training script:

```bash
python train_model.py
```

This trains the Logistic Regression model using the Breast Cancer dataset.

## Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## Prediction Output

The application predicts one of two classes:

- **Benign:** Non-cancerous tumor.
- **Malignant:** Cancerous tumor.

## Dataset

The project uses the Breast Cancer Wisconsin dataset provided by Scikit-learn.

## Author

**Muhammed Zeeshan**

GitHub: [Muhammed-Zeeshan-crypto](https://github.com/Muhammed-Zeeshan-crypto)

## Disclaimer

This project is developed for educational purposes only. It is not a medical diagnostic tool and must not be used to make medical decisions.
