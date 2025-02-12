# predictor/views.py
import pickle
from django.shortcuts import render
from .forms import DiabetesForm, HeartDiseaseForm
from django.conf import settings
import os
import pandas as pd
import numpy as np

def load_models():
    try:
        diabetes_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'predictor/ml_models/diabetes_model.sav'), 'rb'))
        heart_disease_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'predictor/ml_models/heart_model.sav'), 'rb'))
        return diabetes_model, heart_disease_model
    except (FileNotFoundError, pickle.UnpicklingError) as e:
        raise Exception(f"Error loading models: {e}")

diabetes_model, heart_disease_model = load_models()

def index(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def diabetes_prediction(request):
    form = DiabetesForm()
    prediction_result = None
    risk_factors = None
    print("View called")  # Debug print

    if request.method == 'POST':
        print("POST request received")  # Debug print
        form = DiabetesForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug print
            # Get form data
            input_data = [
                form.cleaned_data['pregnancies'],
                form.cleaned_data['glucose'],
                form.cleaned_data['blood_pressure'],
                form.cleaned_data['skin_thickness'],
                form.cleaned_data['insulin'],
                form.cleaned_data['bmi'],
                form.cleaned_data['dpf'],
                form.cleaned_data['age']
            ]
            
            print(f"Input data: {input_data}")  # Debug print
            
            try:
                input_df = pd.DataFrame([input_data], columns=[
                    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
                ])
                prediction = diabetes_model.predict(input_df)
                prediction_result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
                prediction_made = True
                print(f"Prediction made: {prediction_result}")  # Debug print

                risk_factors = {
                    'Blood_Pressure': input_data[2],
                    'Glucose': input_data[1],
                    'BMI': input_data[5],
                }
            except Exception as e:
                print(f"Error in prediction: {e}")  # Debug print
                prediction_result = None
        else:
            print(f"Form errors: {form.errors}")  # Debug print

    context = {
        'form': form,
        'prediction_made': prediction_result is not None,
        'prediction_result': prediction_result,
        'risk_factors': risk_factors,
    }
    print(f"Context being sent to template: {context}")  # Debug print
    return render(request, 'diabetes.html', context)


def heart_disease_prediction(request):
    prediction_made = False
    prediction = None
    error = None

    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            try:
                
                
                # Get cleaned data and convert to proper numeric types
                input_data = [
                    int(form.cleaned_data['age']),
                    int(form.cleaned_data['sex']),
                    int(form.cleaned_data['cp']),
                    int(form.cleaned_data['trestbps']),
                    int(form.cleaned_data['chol']),
                    int(form.cleaned_data['fbs']),
                    int(form.cleaned_data['restecg']),
                    int(form.cleaned_data['thalach']),
                    int(form.cleaned_data['exang']),
                    float(form.cleaned_data['oldpeak']),
                    int(form.cleaned_data['slope']),
                    int(form.cleaned_data['ca']),
                    int(form.cleaned_data['thal'])
                ]
                
                # Make prediction
                input_array = np.array(input_data).reshape(1, -1)
                prediction = heart_disease_model.predict(input_array)[0]
                prediction_made = True
                
                # Debug information
                print("Input data:", input_data)
                print("Prediction:", prediction)
                
            except Exception as e:
                error = f"Error during prediction: {str(e)}"
                print(error)
    else:
        form = HeartDiseaseForm()

    return render(request, 'heart.html', {
        'form': form,
        'prediction': prediction,
        'prediction_made': prediction_made,
        'error': error
    })