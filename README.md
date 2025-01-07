## Dataset
The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. Additionally, the dataset can be used by researchers to explore the relationships between various medical and demographic factors and the likelihood of developing diabetes.

## Usage:

1. Install pyenv
2. Use pyenv local 3.11.11
3. python -m venv venv
4. activate venv
5. pip install requirements

```bash
python predict.py
```

Predict.py has sample data to supply. You can perform realtime prediction by using argparse.

## Training

Model is trained on the provided dataset against:

```
numeric_features = ["age", "bmi", "HbA1c_level", "blood_glucose_level"]
categorical_features = ["gender", "smoking_history", "hypertension", "heart_disease"]
```

Training used gridsearch fit to get the best, most accurate model using the dataset.
