import pickle
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

filename= r"G:\Excelr\Project\Project 3/bag_model2.pkl"
pickle_in = open(filename, 'rb') 
classifier = pickle.load(pickle_in)

def predi(Temperature,Vacuume,Pressure,Humidity):
 
    df2 = pd.DataFrame([[Temperature, Vacuume,Pressure,Humidity]], columns=['temperature', 'exhaust_vacuum', 'amb_pressure','r_humidity'])

    result= classifier.predict(df2)

    return result

st.title("Prediction Of Energy Production")
st.subheader("Group 3")
Temperature = st.number_input("Temperature")
Vacuume = st.number_input("Vacuume")
Pressure = st.number_input("Pressure")
Humidity= st.number_input("Humidity") 

df = pd.DataFrame([[Temperature,Vacuume ,Pressure,Humidity]], columns=['temperature', 'exhaust_vacuum', 'amb_pressure','r_humidity'])
if st.button("Predict"):
    prediction= predi(Temperature,Vacuume,Pressure,Humidity)
    st.table(df)
    st.write(prediction)




    





