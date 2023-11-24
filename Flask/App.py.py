#from ctypes import _NamedFuncPointer
import pickle
from platform import uname_result
import numpy as np

import pandas as pd
from flask import Flask, request, render_template

model1 = pickle.load(open('C:\Users\moham\OneDrive\Desktop\222\productivity (4).pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict')
def index():
    return render_template('predict.html')

@app.route('/data_predict', methods=['GET', 'POST'])
def predict():
    quarter = int(request.form['quarter'])
    
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
    
    team = int(request.form['Team Number'])
    time = int(request.form['Time Allocated'])
    items = int(request.form['Unfinished Items'])
    over_time = int(request.form['Over time'])
    incentive = int(request.form['Incentive'])
    idle_time = int(request.form['Idle Time'])
    idle_men = int(request.form['Idle Men'])
    style_change = int(request.form['Style Change'])
    no_of_workers = int(request.form['Number of Workers'])
    Trageted_Productivity = int(request.form['Trageted Productivity'])
    Actual_Productivity = int(request.form['Actual Productivity'])
    date = int(request.form['date'])
    
    f= [team,time]
    print(f)

    features = np.array([quarter, department, day, team, time, items, over_time, incentive, idle_time, idle_men, style_change,no_of_workers,Trageted_Productivity,Actual_Productivity,date])
    print(features)
    # prediction = model1.predict(pd.DataFrame([[quarter, department, day, team, time, items, over_time, incentive, idle_time, idle_men, style_change, no_of_workers]], columns=['quarter', 'department', 'day_of_week', 'team', 'time_allocated', 'unfinished_items', 'over_time', 'incentive', 'idle_time', 'idle_men', 'style_change', 'no_of_workers']))
    prediction = model1.predict(features.reshape(1,-1))
    prediction = round(prediction[0], 4) * 100

    return render_template('productivity.html', prediction_text="Productivity is {:.2f}%".format(prediction))

if __name__== '__main__':
    app.run(debug=True)