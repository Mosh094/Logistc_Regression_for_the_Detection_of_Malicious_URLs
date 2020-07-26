# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:38:12 2020

@author: HP EliteBook 840
"""


from flask import Flask, request
import numpy as np
import pickle
import pandas as pd


app=Flask(__name__)   #first step
pickle_in = open("logit.pkl","rb")
classifier=pickle.load(pickle_in)   #step 2


@app.route('/')
def welcome():
    return "Welcome All" #3rd step

@app.route('/predict',methods=["Get"])
def predict_note_authentication(): #4th step, declare imputs 5 0f them and predict
    url=request.args.get("url")
    prediction=classifier.predict([[url]])
    return "Hello The predicted value is"+str(prediction)

@app.route('/predict_file',methods=["POST"]) #5th step
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
    return "The predicted values for the csv is"+ str(list(prediction))


if __name__=='__main__':
    app.run()    #first step without the items in bracket