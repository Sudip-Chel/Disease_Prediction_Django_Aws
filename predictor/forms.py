# predictor/forms.py
from django import forms

class DiabetesForm(forms.Form):
    pregnancies = forms.IntegerField(
        min_value=0, max_value=20,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    glucose = forms.IntegerField(
        min_value=0, max_value=300,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    blood_pressure = forms.IntegerField(
        min_value=0, max_value=150,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    skin_thickness = forms.IntegerField(
        min_value=0, max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    insulin = forms.IntegerField(
        min_value=0, max_value=900,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    bmi = forms.FloatField(
        min_value=0.0, max_value=70.0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    dpf = forms.FloatField(
        min_value=0.0, max_value=3.0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    age = forms.IntegerField(
        min_value=0, max_value=120,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(
        min_value=1, 
        max_value=120,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    sex = forms.ChoiceField(
        choices=[(1, 'Male'), (0, 'Female')],  # Changed to numerical values
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cp = forms.ChoiceField(
        choices=[
            (0, 'Typical Angina'),
            (1, 'Atypical Angina'),
            (2, 'Non-anginal Pain'),
            (3, 'Asymptomatic')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    trestbps = forms.IntegerField(
        min_value=50,
        max_value=250,
        label='Resting Blood Pressure',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    chol = forms.IntegerField(
        min_value=100,
        max_value=600,
        label='Cholesterol',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    fbs = forms.ChoiceField(
        choices=[(0, 'No'), (1, 'Yes')],
        label='Fasting Blood Sugar > 120 mg/dl',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    restecg = forms.ChoiceField(
        choices=[
            (0, 'Normal'),
            (1, 'ST-T Wave Abnormality'),
            (2, 'Left Ventricular Hypertrophy')
        ],
        label='Resting ECG Results',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    thalach = forms.IntegerField(
        min_value=50,
        max_value=250,
        label='Maximum Heart Rate',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    exang = forms.ChoiceField(
        choices=[(0, 'No'), (1, 'Yes')],
        label='Exercise Induced Angina',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    oldpeak = forms.FloatField(
        min_value=0,
        max_value=10,
        label='ST Depression',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )
    slope = forms.ChoiceField(
        choices=[
            (0, 'Upsloping'),
            (1, 'Flat'),
            (2, 'Downsloping')
        ],
        label='Slope of Peak Exercise ST Segment',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    ca = forms.ChoiceField(
        choices=[(str(i), str(i)) for i in range(4)],  # 0-3
        label='Number of Major Vessels',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    thal = forms.ChoiceField(
        choices=[
            (0, 'Normal'),
            (1, 'Fixed Defect'),
            (2, 'Reversible Defect')
        ],
        label='Thalassemia',
        widget=forms.Select(attrs={'class': 'form-control'})
    )