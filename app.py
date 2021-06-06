#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:44:05 2021

@author: dbalas
"""
from flask import Flask, render_template, redirect, url_for, session, request
from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField
from wtforms.validators import DataRequired
#import numpy as np 
#from keras.models import load_model
import joblib

def return_prediction(model,scaler,sample_json):
    #Function to return model's prediction
    temp = sample_json["temp"]
    windspeed = sample_json["windspeed"]
    month = sample_json["month"]
    hour = sample_json["hour"]
 
    bikes = [[temp,windspeed,month,hour]]
    bikes = scaler.transform(bikes)
    
    # # returns prediction as an array
    # bike_pred = model.predict(bikes)
 
    # return round(int(bike_pred[0][0]),0)

    # to use gradient boosted tree model---change prediction function as well
    GBT_pred = model.predict(bikes)
    return round(int(GBT_pred[0]),0)

app = Flask(__name__)
# Configure a secret SECRET_KEY
app.config["SECRET_KEY"] = "22182"# Loading the model and scaler
#lb_model = load_model('LB_dnn_model.h5')
lb_scaler = joblib.load('LB_scaler.pkl')

gbt_model = joblib.load('gbt.pkl')
# Now create a WTForm Class
class LBForm(FlaskForm):
    temp = TextField('temperature (degrees C)', validators=[DataRequired()])
    windspeed = TextField('Wind Speed (km/h)', validators=[DataRequired(message="Please enter value greater than or equal to 0")])
    month = TextField('Month Number (enter January as 1, etc.)', validators=[DataRequired(message="Please enter value between 1 and 12")])
    hour = TextField('Time of Day (hour)', validators=[DataRequired(message="Please enter value between 0 and 24")])
    submit = SubmitField('Analyze')

@app.route('/', methods=['GET', 'POST'])

def index():
    """Create instance of form for input data"""
    form = LBForm()
      
      # If the form is valid on submission
    if form.validate_on_submit():
        # Grab the data from the input on the form.
        session['temp'] = form.temp.data
        session['windspeed'] = form.windspeed.data
        session['month'] = form.month.data
        session['hour'] = form.hour.data
        return redirect(url_for('prediction'))
    return render_template('home.html', form=form)

@app.route('/prediction')

def prediction():
    #Defining content dictionary 
    content = {}
    
    content['temp'] = float(session['temp'])
    content['windspeed'] = float(session['windspeed'])
    content['month'] = float(session['month'])
    content['hour'] = float(session['hour'])
 
    results = return_prediction(model=gbt_model,scaler=lb_scaler,sample_json=content)

    if request.method == 'POST':
        if request.form.get('newData') == 'VALUE1':
            return render_template('home.html')
        else: pass
    elif request.method == 'GET':
        return render_template('prediction.html', results=results)
    # return render_template('prediction.html',results=results)

if __name__ == '__main__':
    app.run(debug=True)
 

 
##### TO DO #####
## Impose limits on input fields--num, max, min

 

 
 
 
 
 
 
 
 
 
 
 
