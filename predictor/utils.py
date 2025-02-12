import pickle
import os

# Load models
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIABETES_MODEL_PATH = os.path.join(BASE_DIR, 'saved_models/diabetes_model.sav')
HEART_MODEL_PATH = os.path.join(BASE_DIR, 'saved_models/heart_model.sav')

diabetes_model = pickle.load(open(DIABETES_MODEL_PATH, 'rb'))
heart_model = pickle.load(open(HEART_MODEL_PATH, 'rb'))
