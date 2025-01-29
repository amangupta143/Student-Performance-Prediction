# Student Performance Prediction

A machine learning project that predicts students' mathematics scores based on various demographic and academic factors. The project implements an end-to-end ML pipeline with data ingestion, transformation, model training, and a Flask web interface for making predictions.

## User Interface

### Landing Page
![Landing Page](https://github.com/user-attachments/assets/a721be6e-a621-4475-a0ca-41a707b65b8f)
The landing page features a modern interface with a network visualization background, highlighting the AI-powered nature of the prediction system. Users can start making predictions or learn more about the system's capabilities.

### Prediction Form
![Prediction Form](https://github.com/user-attachments/assets/dda3bb7e-a834-4284-b98b-f68c1ca22e3d)
The prediction interface collects student information through an intuitive form with the following sections:
- Demographic Information (Gender, Race/Ethnicity)
- Educational Background (Parental Education Level)
- Academic Support (Lunch Type, Test Preparation)
- Academic Scores (Writing and Reading scores)

## Features

- Predicts math scores based on:
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch Type
  - Test Preparation Course
  - Reading Score
  - Writing Score
- Multiple ML models comparison (Random Forest, XGBoost, CatBoost, etc.)
- Automated pipeline for data preprocessing and model training
- Web interface for easy predictions
- Comprehensive error handling and logging

## Project Structure

```
└── student-performance-prediction/
    ├── app.py                  # Flask application
    ├── requirements.txt        # Project dependencies
    ├── setup.py               # Package configuration
    ├── src/
    │   ├── components/        # Core ML pipeline components
    │   │   ├── data_ingestion.py
    │   │   ├── data_transformation.py
    │   │   └── model_trainer.py
    │   ├── pipeline/          # Prediction and training pipelines
    │   └── utils.py           # Utility functions
    ├── templates/             # HTML templates
    └── notebook/              # Jupyter notebooks for EDA and model training
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/amangupta143/student-performance-prediction.git
cd student-performance-prediction
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Training Pipeline

To train the model with new data:

```python
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

# Initialize and run the pipeline
data_ingestion = DataIngestion()
train_data, test_data = data_ingestion.initiate_data_ingestion()

data_transformation = DataTransformation()
train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

model_trainer = ModelTrainer()
r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
```

### Web Interface

1. Start the Flask application:
```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:5000`

3. Enter student information in the form to get predictions

## Model Performance

The project evaluates multiple regression models:
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

The best performing model is automatically selected based on R² score during training.

## Development

### Adding New Features

1. Create new components in `src/components/`
2. Update the pipeline in `src/pipeline/`
3. Modify `app.py` to expose new features via the web interface

### Testing

Currently implementing comprehensive testing. Contributions welcome!

## Contributing

I welcome contributions to this repository! If you have ideas for improvement, bug fixes, or want to explore different aspects of the model, feel free to create a pull request.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is available under the MIT License.

## Contact

- Author: Aman Gupta
- Email: amangupta.main@gmail.com

## Acknowledgments

- Dataset source: <a href="https://www.kaggle.com/datasets/impapan/student-performance-data-set" >Students Performance in Exams (Kaggle)</a>.
- Special thanks to contributors and maintainers