
import streamlit as st
import pickle
import pandas as pd
with open("model.pkl", "rb") as file:
    model = pickle.load(file)
st.title("Breast Cancer Classification")
st.write("Eter tumour measurements to predict the result.")
radius = st.number_input("Mean Radius", value=14.0)
texture = st.number_input("Mean Texture", value=20.0)
perimeter = st.number_input("Mean Perimeter", value=90.0)
area = st.number_input("Mean Area", value=600.0)
smoothness = st.number_input("Mean Smoothness", value=0.1)
if st.button("Predict"):
    input_data = pd.DataFrame([[radius,texture,perimeter,area,smoothness
    ]], columns=["mean radius","mean texture","mean perimeter","mean area","mean smoothness"
    ])
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.error("Prediction: Malignant")
    else:
        st.success("Prediction: Benign")    
    st.warning("Educational demonstration only. Not for medical diagnosis.")
