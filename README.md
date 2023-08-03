

# Predictive Rent Pricing Model for Kuala Lumpur and Selangor Apartments

![Python](https://img.shields.io/badge/python-3.8-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

This repository contains a machine learning model for predicting the monthly rent of apartments in Kuala Lumpur and Selangor.

## Dataset

The dataset contains information about various properties listed for rent. The features include property name, completion year, location, property type, number of rooms, parking spaces, bathrooms, size of the property, level of furnishing, facilities, additional facilities, and region. The target variable is the monthly rent of the property.

## Model

The predictive model is a Decision Tree Regressor trained using Scikit-Learn. The model was evaluated based on the root mean squared error (RMSE) metric.

## App

The repository also includes a Streamlit app that allows users to input property features and uses the trained model to predict the rent.

## Usage

To run the Streamlit app:

1. Install the required libraries (Pandas, Streamlit, Scikit-Learn, and Pickle).

2. Download the trained model and preprocessor from the links provided in the repository.

3. Update the paths to the pickled model and preprocessor in the Streamlit app code.

4. Run the Streamlit app using the command: `streamlit run Rent_Pricing_Streamlit_App.py`

## License

This project is licensed under the terms of the MIT license.

