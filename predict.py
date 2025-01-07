import pickle
import pandas as pd

# Load the trained model
with open("diabetes_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

# Example new data
# Expected Response:
    # ['Non-Diabetic', 'Diabetic']
new_data = pd.DataFrame([
    ["Male", 50, 0, 0, "never", 30.0, 6.2, 130],
    ["Female", 65, 1, 0, "current", 32.5, 7.0, 180]
], columns=[
    "gender", "age", "hypertension", "heart_disease", "smoking_history",
    "bmi", "HbA1c_level", "blood_glucose_level"
])

# Predict diabetes
predictions = model.predict(new_data)
mapped_predictions = ["Non-Diabetic" if pred == 0 else "Diabetic" for pred in predictions]
print(mapped_predictions)
