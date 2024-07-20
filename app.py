import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

model = pickle.load(open("RandomForestRegressionModel.pkl", 'rb'))
df = pd.read_csv("cars Cleaned.csv")


@app.route('/')
def index():
    companies = sorted(df['company'].unique())
    car_models = sorted(df['name'].unique())
    year = sorted(df['year'].unique(), reverse=True)
    fuel_type = df['fuel_type'].unique()
    companies.insert(0, "Select Company")
    return render_template('index.html', companies=companies, car_models=car_models, years=year,
                           fuel_type=fuel_type)


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kms_driven'))

    prediction = model.predict(pd.DataFrame([[car_model, company, year, fuel_type, kms_driven]],
                                            columns=['name', 'company', 'year', 'fuel_type', 'kms_driven']))

    return str(np.round(prediction[0], 2))


if __name__ == "__main__":
    app.run(debug=True)
