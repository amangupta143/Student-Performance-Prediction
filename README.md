# Student Performance Prediction

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-red.svg)](https://flask.palletsprojects.com/)

An end-to-end machine learning project that predicts student mathematics scores based on demographic and academic factors. Features automated model selection, comprehensive data processing, and an intuitive Flask web interface. Live demo available on Render.

## 🚀 Quick Links
- [Live Demo](https://student-performance-cl3b.onrender.com/)
- [Dataset Source](https://www.kaggle.com/datasets/impapan/student-performance-data-set)
- [API Documentation](#-api-documentation)
- [Contributing Guidelines](#-contributing)

## 💻 User Interface

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

## 🌟 Features

### Core Functionality
- Mathematics score prediction (0-100 range) using 7 key features
- Automated model selection from an ensemble of algorithms
- Comprehensive data preprocessing pipeline
- Real-time prediction via web interface

### Technical Highlights
- Flask-based web application with form validation
- Automated hyperparameter tuning
- Extensive error handling and logging
- Privacy policy and terms of service implementation
- Responsive, modern UI design
- Model performance monitoring

## 📊 Dataset Overview

The model uses the [Students Performance in Exams](https://www.kaggle.com/datasets/impapan/student-performance-data-set) dataset:

| Feature | Type | Description | Example Values |
|---------|------|-------------|----------------|
| `gender` | Categorical | Student's gender | male, female |
| `race_ethnicity` | Categorical | Ethnic group identifier | group A - E |
| `parental_level_of_education` | Categorical | Highest parental education | bachelor's degree, master's degree |
| `lunch` | Categorical | School lunch program type | standard, free/reduced |
| `test_preparation_course` | Categorical | Test prep completion status | completed, none |
| `reading_score` | Numerical | Reading exam score | 0-100 |
| `writing_score` | Numerical | Writing exam score | 0-100 |

**Target Variable**: `math_score` (Numerical, 0-100 range)

## 🏗 Project Structure

```
student-performance-prediction/
├── app.py                  # Flask application
├── requirements.txt        # Project dependencies
├── setup.py                # Package configuration
├── artifacts/              # Model artifacts and processed data
│   ├── data.csv            # Processed dataset
│   ├── model.pkl           # Trained model
│   └── preprocessor.pkl    # Data transformation pipeline
├── src/
│   ├── components/         # Core ML pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/           # Prediction and training pipelines
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py        # Custom exception handling
│   ├── logger.py           # Logging configuration
│   └── utils.py            # Utility functions
├── templates/              # HTML templates
│   ├── home.html
│   ├── index.html
│   └── legal.html
├── notebook/               # Jupyter notebooks
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
└── .ebextensions/          # Elastic Beanstalk configuration
    └── python.config
```

## ⚙️ Installation

1. **Clone Repository**
```bash
git clone https://github.com/amangupta143/student-performance-prediction.git
cd student-performance-prediction
```

2. **Setup Environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# OR
venv\Scripts\activate     # Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

## 🔧 Usage

### Training Pipeline

```python
from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.predict_pipeline import PredictPipeline

# Training
train_pipeline = TrainPipeline()
model_metrics = train_pipeline.run_pipeline()

# Prediction
predict_pipeline = PredictPipeline()
prediction = predict_pipeline.predict(input_data)
```

### Web Interface

1. Start the Flask application:
```bash
python app.py
```

2. Open `http://localhost:5000` in your browser
3. Fill the prediction form with student information

## 🤖 Model Architecture

### Data Processing Pipeline
1. **Data Ingestion**:
   - Automated data loading and validation
   - Train-test split (80/20)
   - Data integrity checks

2. **Data Transformation**:
   - Numerical features: Median imputation + Standard scaling
   - Categorical features: One-hot encoding
   - Feature engineering and validation

### Model Selection
The system evaluates multiple regression models:
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- Gradient Boosting Regressor
- Linear Regression
- Decision Tree Regressor
- AdaBoost Regressor

Selection criteria:
- Automated hyperparameter tuning via GridSearchCV
- Model selection based on R² score
- Typical performance: R² 0.85-0.90

## 🔌 API Documentation

### Prediction Endpoint
```http
POST /predict
Content-Type: application/json

{
    "gender": "male",
    "race_ethnicity": "group B",
    "parental_level_of_education": "bachelor's degree",
    "lunch": "standard",
    "test_preparation_course": "completed",
    "reading_score": 75,
    "writing_score": 82
}
```

## 🛠 Development

### Adding Features
1. Create new components in `src/components/`
2. Update pipelines in `src/pipeline/`
3. Modify `app.py` for web interface changes
4. Add appropriate tests and documentation

### Testing
- Unit tests being implemented
- Integration tests planned
- Contributions welcome!

## 👥 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Maintain consistent logging patterns

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 📫 Contact & Support

**Aman Gupta**  
📧 [amangupta.main@gmail.com](mailto:amangupta.main@gmail.com)  
🐛 [Issue Tracker](https://github.com/amangupta143/student-performance-prediction/issues)

## 🙏 Acknowledgments

- Kaggle for providing the dataset
- Render for hosting services
- Open source community for various tools and libraries used
