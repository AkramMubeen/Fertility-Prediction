from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app=Flask(__name__)


## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            season=float(request.form.get('season')),
            age=float(request.form.get('age')),
            childish_diseases=float(request.form.get('childish_diseases')),
            trauma=float(request.form.get('trauma')),
            surgery=float(request.form.get('surgery')),
            high_fever=float(request.form.get('high_fever')),
            alcohol_freq=float(request.form.get('alcohol_freq')),
            smoking=float(request.form.get('smoking')),
            sitting_hrs=float(request.form.get('sitting_hrs'))
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("After Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)        

