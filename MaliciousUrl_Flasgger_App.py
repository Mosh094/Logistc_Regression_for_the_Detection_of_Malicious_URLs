# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 02:10:20 2020

@author: HP EliteBook 840
"""

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import joblib
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in=open('logit.pkl', 'rb')
classifier=pickle.load(pickle_in)
cv_model = open('vectorizer.pkl', 'rb')
cv = joblib.load(cv_model)

@app.route('/')
def welcome():
    return "welcome All"

@app.route('/predict',methods=['GET'])
def malicious_url_prediction():

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
    int_features =  request.args.get('url')
    data=[int_features]
    vect =cv.transform(data)
    prediction = classifier.predict(vect)[0]
    return "The URL is " + str (prediction)


if __name__=='__main__':
    app.run()