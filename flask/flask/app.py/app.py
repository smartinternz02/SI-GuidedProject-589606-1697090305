import datetime
import pickle
import dateutil
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import xgboost

model1 = pickle.load(open('C:\\Users\\jeeva\\OneDrive\\Desktop\\jeevan\\productivity.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict.html')
def index():
    return render_template('predict.html')

@app.route('/data_predict', methods=['POST'])
def predict():
    # quarter = int(request.form['quarter'])
    
    department = request.form['Department'].lower()
    if department in ['sewing', 'finishing']:
        department = 1
    else:
        department = 0
     
    day = request.form['Day of the week']
    if day == 'Monday':
        day = 0
    elif day == 'Tuesday':
        day = 4
    elif day == 'Wednesday':
        day = 5
    elif day == 'Thursday':
        day = 3
    elif day == 'Saturday':
        day = 1
    elif day == 'Sunday':
        day = 2
    
    quarter = int(request.form['Quarter'])
    # day = int(request.form['Day of the week'])
    # department = int(request.form['Department'])
    team = int(request.form['Team Number'])
    time = int(request.form['Time Allocated'])
    items = int(request.form['Unfinished Items'])
    over_time = int(request.form['Over time'])
    incentive = int(request.form['Incentive'])
    idle_time = int(request.form['Idle Time'])
    idle_men = int(request.form['Idle Men'])
    style_change = int(request.form['Style Change'])
    no_of_workers = int(request.form['Number of Workers'])
    values = ((i) for i in request.form.values())
    features = [style_change, no_of_workers]
    print(style_change, no_of_workers)

    prediction = model1.predict(quarter)

    # prediction = model1.predict(pd.DataFrame([[quarter, department, day, team, time, items, over_time, incentive, idle_time, idle_men, style_change, no_of_workers]], columns=['quarter', 'department', 'day_of_week', 'team_number', 'time_allocated', 'unfinished_items', 'over_time', 'incentive', 'idle_time', 'idle_men', 'style_change', 'no_of_workers']))
  
    prediction = round(prediction[0], 4) * 100
    print(prediction)

    return render_template('productivity.html', prediction_text="Productivity is {:.2f}%".format(prediction))

if __name__ == '__main__':
    app.run(debug=True)
