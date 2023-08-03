import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the pickled model and preprocessor
with open('data/rent_pricing_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('data/rent_pricing_preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

# Define the app
def run():
    st.title("Predictive Rent Pricing Model for Kuala Lumpur and Selangor Apartments")
    
    # Input features
    completion_year = st.number_input('Completion Year', min_value=1900, max_value=2100)
    location = st.selectbox('Location', ['Kuala Lumpur', 'Selangor'])
    property_type = st.selectbox('Property Type', ['Condominium', 'Apartment'])
    rooms = st.slider('Number of Rooms', 1, 10)
    parking = st.slider('Number of Parking Spaces', 0, 5)
    bathroom = st.slider('Number of Bathrooms', 1, 5)
    size = st.number_input('Size (in sqft)', min_value=100)

    # Placeholder for additional fields
    prop_name = st.text_input('Property Name')
    furnished = st.selectbox('Furnished', ['Yes', 'No'])
    facilities = st.text_input('Facilities')
    additional_facilities = st.text_input('Additional Facilities')
    region = st.selectbox('Region', ['Region1', 'Region2'])  # Adjust this according to your data

    # Create a dataframe from the inputs
    input_data = pd.DataFrame({
        'completion_year': [completion_year],
        'location': [location],
        'property_type': [property_type],
        'rooms': [rooms],
        'parking': [parking],
        'bathroom': [bathroom],
        'size': [size],
        'prop_name': [prop_name],
        'furnished': [furnished],
        'facilities': [facilities],
        'additional_facilities': [additional_facilities],
        'region': [region]
    })

    # Preprocess the input data
    input_data_preprocessed = preprocessor.transform(input_data)

    # Make predictions
    if st.button("Predict Rent"):
        prediction = model.predict(input_data_preprocessed)
        st.write("The predicted monthly rent is: ", prediction)

# Run the app
if __name__ == '__main__':
    run()
