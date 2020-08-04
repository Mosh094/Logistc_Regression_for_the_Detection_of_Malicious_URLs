# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 02:10:20 2020

@author: HP EliteBook 840
"""

import pandas as pd
import numpy as np
import pickle
import joblib
import streamlit as st

pickle_in=open('logit.pkl', 'rb')
classifier=pickle.load(pickle_in)
cv_model = open('vectorizer.pkl', 'rb')
cv = joblib.load(cv_model)

def welcome():
    return "welcome All"

def malicious_url_prediction(url):

    """Let's predict the safety of urls 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: url
        in: query
        type: string
        required: true

    responses:
        200:
            description: The output values
        
    """
    int_features =  st.text_input("url")
    data=[int_features]
    vect =cv.transform(data)
    prediction = classifier.predict(vect)[0]
    print(prediction)
    return prediction

def main():
    st.title("Malicious URL Prediction App")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Malicious URL Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    url = st.text_input("url","Type Here")
    result=""
    if st.button("Predict"):
        result=malicious_url_prediction(url)
    st.success('The URL is {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()