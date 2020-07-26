# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:03:08 2020

@author: HP EliteBook 840
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("logit.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_malicious_websites(url):

    """Let's Predict Safety of URL 
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

    prediction=classifier.predict([[url]])
    print(prediction)
    return prediction



def main():
    st.title("Malicious URL Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    url= st.text_input("url","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_malicious_websites(url)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
