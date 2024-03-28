import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
import seaborn as sns
import streamlit as st
import joblib

# Load the model
model = joblib.load('HousingPrices-Amsterdam-August-2021 (1).pkl')

data = pd.read_csv('HousingPrices-Amsterdam-August-2021.csv')
df = data.copy()

st.markdown("<h1 style='text-align: center; font-family: helvetica; color: #1F4172;'>Amsterdam House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='margin: -30px; color: #F11A7B; text-align: center; font-family: cursive'> BUILT BY Matini The Data Guy </h4>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.image('pngwing.com (1).png', width=350, use_column_width=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<p>A house prediction project involves using data analysis and machine learning to predict the prices or other factors related to houses. It uses historical data about houses, like their location, size, and features, to make these predictions. It can be helpful for real estate professionals and individuals looking to buy or sell a house.</p>", 
             unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.dataframe(data, use_container_width=True)


st.sidebar.image('pngwing.com (2).png', caption='Welcome User')

st.markdown("<br>", unsafe_allow_html=True)
st.dataframe(data, use_container_width=True)

input_choice = st.sidebar.radio('Choose your input type', ['Slider Input', 'Number Input'])

if input_choice == 'Slider Input':
    Room = st.sidebar.slider('Average Room', data['Room'].min(), data['Room'].max())
    Area = st.sidebar.slider('Average Area', data['Area'].min(), data['Area'].max())
    Zip = st.sidebar.slider('Average Zip', data['Zip'].min(), data['Zip'].max())
    Lon = st.sidebar.slider('Area Lon', data['Lon'].min(), data['Lon'].max()) 
    Lat = st.sidebar.slider('Average Lat', data['Lat'].min(), data['Lat'].max())
    Price = st.sidebar.slider('Average Price', data['Price'].min(), data['Price'].max())

else:
    Room = st.sidebar.slider('Average Room', data['Room'].min(), data['Room'].max())
    Area = st.sidebar.slider('Average Area', data['Area'].min(), data['Area'].max())
    Zip = st.sidebar.slider('Average Zip', data['Zip'].min(), data['Zip'].max())
    Lon = st.sidebar.slider('Area Lon', data['Lon'].min(), data['Lon'].max()) 
    Lat = st.sidebar.slider('Average Lat', data['Lat'].min(), data['Lat'].max())
    Price = st.sidebar.slider('Average Price', data['Price'].min(), data['Price'].max())


# Create input variables DataFrame
input_vars = pd.DataFrame({ 
    'Room': [Room],
    'Area': [Area],
    'Zip': [Zip],
    'Lon': [Lon],
    'Lat': [Lat],
    'Price': [Price],
})

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h5 style='margin: -30px; color: olive; font-family: helvetica'>User Input Variable</h5>", unsafe_allow_html=True)
st.dataframe(input_vars)

st.markdown("<br>", unsafe_allow_html=True)

# Predict the house price
predicted = model.predict(input_vars)
st.success(f'The Predicted price of your house is {predicted[0]}')