"""
Created on Tue Nov 16 22:09:22 2021

@author: DSP Group 4
"""

import streamlit as st
import requests



def welcome():
    return "Welcome to the Big Mart Sales Prediction Application"


def predict_outlet_sales(ProductType, LocationType, OutletSize, OutletType):
    product_outlet_data = {'ProductType': float(ProductType), 'LocationType': float(LocationType), 'OutletSize': int(OutletSize),
                           'OutletType': float(OutletType)}
    prediction = requests.post('http://127.0.0.1:5000/predict', data=product_outlet_data)
    return prediction.content.decode('utf-8')


def main():
    # print("Inside main...")
    st.title("Sales Price Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Outlet Sales Predictor</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    ProductType = st.text_input("Product Type [0-15]", "Enter number between 0 to 15")
    OutletSize = st.selectbox(
        'Outlet Size [0-High, 1-Medium, 2-Small]',
        ('0', '1', '2'))
    LocationType = st.selectbox(
        'Location Type [0-Tier1, 1-Tier2, 2-Tier3]',
        ('0', '1', '2'))

    # FatContent = st.selectbox(
    #    'Fat Content [0-Low fat, 1-Regular]',
    #    ('0', '1'))
    # ProductVisibility = st.text_input("Product Visibility")
    # MRP = st.text_input("MRP")
    OutletType = st.selectbox(
        'Outlet Type [0-Grocery Store, 1-Supermarket Type1, 2-Supermarket Type2, 3-Supermarket Type3]',
        ('0', '1', '2', '3'))

    # Establishment_Year = st.text_input("EstablishmentYear [0-8]","Enter number between 0 to 8")
    # Outlet_Type = st.text_input("OutletType [0-3]", "Enter number between 0 to 3")

    result = ""
    if st.button("Predict"):
        result = predict_outlet_sales(ProductType, LocationType, OutletSize, OutletType)
    st.success('The Sales Price is  {}'.format(result))


if __name__ == '__main__':
    main()
