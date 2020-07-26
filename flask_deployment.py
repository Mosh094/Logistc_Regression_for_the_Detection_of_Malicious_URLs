# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:38:12 2020

@author: HP EliteBook 840
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("logit.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
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
        201:
            description: The output values
        
    """
    url=request.args.get("url")
    prediction=classifier.predict([[url]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Predict Safety of URL 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        201:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run()