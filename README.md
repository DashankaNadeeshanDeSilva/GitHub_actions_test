# GitHub_actions_test


This preoject has conducted to learn how Github actions are working to build CI/CD pipelines.

# Python ML Model Deployment with GitHub Actions

This repository is a demonstration project to learn and showcase the implementation of Continuous Integration and Continuous Delivery (CI/CD) pipelines using GitHub Actions. It includes a simple Python application that trains a machine learning model, makes predictions, and serves the model through a Streamlit app.

## Project Structure

- `app.py`: Streamlit application that serves the trained model.
- `predict.py`: Python script for making predictions using the trained model.
- `requirements.txt`: List of packages required to run the application.
- `train_model.py`: Script for training the machine learning model.
- `model.pkl`: Serialized version of the trained machine learning model.
- `.github/workflows/ci.yml`: CI/CD pipeline configuration using GitHub Actions.

## Features

- **Model Training**: Automate the training of a machine learning model using GitHub Actions.
- **CI/CD Pipeline**: Utilize `ci.yml` for continuous integration and delivery to test, build, and deploy the application.
- **Streamlit Application**: Interactive web app to demonstrate the usage of the trained model.

## Getting Started

To clone and run this application, you'll need Git and Python installed on your computer. From your command line:

```bash
# Clone this repository
git clone https://github.com/yourusername/your-repository-name
# Go into the repository
cd your-repository-name
# Install dependencies
pip install -r requirements.txt
# Run the application
streamlit run app.py
