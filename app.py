from urllib import response
from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy


KNN_model= pickle.load(open("KNN_flight_model.pkl","rb"))

app=Flask(__name__)

@app.route('/') # codepie.com
def home():
    return render_template('home.html')
    # return "I AM ACTIVE"

if __name__=="__main__":
    app.run(debug=True)


