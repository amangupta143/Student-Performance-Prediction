from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html', results=None)
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('writing_score')),
                writing_score=float(request.form.get('reading_score'))
            )
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("after Prediction")
            
            # Ensure result is between 0 and 100 and round to 2 decimal places
            final_result = round(float(np.clip(results[0], 0, 100)), 2)
            
            return render_template('home.html', results=final_result)
            
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return render_template('home.html', error="An error occurred during prediction. Please try again.")

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('legal.html', page_type='privacy')

@app.route('/terms-of-service')
def terms_of_service():
    return render_template('legal.html', page_type='terms')

if __name__ == "__main__":
    app.run()