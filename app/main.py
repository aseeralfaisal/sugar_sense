# from flask import Flask
from flask import Flask, request, jsonify
# import numpy as np
# import pickle

# model = pickle.load(open('final_model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home_view():
    return "<h1>Hi Tasin</h1>"


# @app.route('/predict', methods=['POST'])
# def predict():
#     Pregnancies = request.form.get('Pregnancies')
#     Glucose = request.form.get('Glucose')
#     BloodPressure = request.form.get('BloodPressure')
#     SkinThickness = request.form.get('SkinThickness')
#     Insulin = request.form.get('Insulin')
#     BMI = request.form.get('BMI')
#     DiabetesPedigreeFunction = request.form.get('DiabetesPedigreeFunction')
#     Age = request.form.get('Age')

#     input_query = np.array(
#         [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
#     result = model.predict(input_query)[0]

#     return jsonify({'Diabetes': str(result)})
