# EV Charging Station Usage Prediction

This project predicts the usage of EV charging stations using machine learning models. The goal is to help companies better understand and anticipate EV charger occupancy rates, enabling efficient resource allocation and planning.

## Table of Contents
- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Project Files](#project-files)
- [Model Performance](#model-performance)
- [Acknowledgments](#acknowledgments)

---

## Project Overview
Electric vehicle (EV) charging station usage prediction helps address the growing demand for EV charging infrastructure. This project leverages demographic and traffic data to develop a predictive model for EV charging station occupancy rates, enabling more informed decisions regarding charger deployment and utilization.

## Directory Structure

Final_Project/
├── app.py                   # Main application script
├── data/                    # Data files
│   ├── raw/                 # Raw data files
│   ├── processed/           # Processed data files
├── models/                  # Model artifacts
│   ├── scaler.pkl           # Scaler for data normalization
│   ├── trained_model.pkl    # Trained machine learning model
├── notebooks/               # Jupyter notebooks for analysis and modeling
│   ├── data_enrichment.ipynb
│   ├── data_preprocess.ipynb
│   ├── model.ipynb
├── Presentation/            # Presentations and reports
│   ├── EV-Charging-Usage-Prediction.pdf
│   ├── EV-Charging-Usage-Prediction.pptx
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Git ignore file







## Installation

### Prerequisites
- Python 3.7 or higher
- Virtual environment (recommended)

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ev-charging-predictor.git
    cd ev-charging-predictor
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate       # On macOS/Linux
    .\env\Scripts\activate        # On Windows
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Project
- To run the main application:
    ```bash
    python main.py
    ```

- To explore the data processing and model training steps, open the Jupyter notebooks in the `notebooks/` directory.

### Main Scripts
- **`app.py`**: Contains the main application logic for running predictions.
- **`main.py`**: Serves as the entry point for data processing, model training, and evaluation.

### Notebook Analysis
- **`data_enrichment.ipynb`**: Enriches data by merging demographic and traffic data.
- **`data_preprocess.ipynb`**: Prepares data by cleaning and preprocessing.
- **`model.ipynb`**: Builds and evaluates the machine learning model.

## Project Files

- **`data/`**: Contains the dataset used in this project. Raw data is stored in `data/raw/`, while processed data is in `data/processed/`.
- **`models/`**: Holds the saved model (`trained_model.pkl`) and scaler (`scaler.pkl`).
- **`notebooks/`**: Jupyter notebooks for data enrichment, preprocessing, and model training.
- **`Presentation/`**: Contains presentation files in `.pdf` and `.pptx` formats.

## Model Performance

The final model, a Random Forest Regressor, achieved an R² score of 0.91 on cross-validation. This result indicates the model's strong performance in predicting EV charging station occupancy rates. Further improvements may include tuning hyperparameters and testing additional features.

## Acknowledgments

Special thanks to the Ironhack Data Science & Machine Learning Bootcamp for providing foundational knowledge and support throughout this project.

---

For questions or contributions, please feel free to reach out or create a pull request!


