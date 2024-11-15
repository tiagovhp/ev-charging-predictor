import streamlit as st
import pandas as pd

# Custom header with colored background
st.markdown(
    """
    <style>
    .header {
        font-size: 2em;
        font-weight: bold;
        color: white;
        background-color: #adcced; /* Change color as needed */
        padding: 10px;
        text-align: center;
        border-radius: 5px;
    }
    </style>
    <div class="header">EV Charging Station Setup</div>
    """,
    unsafe_allow_html=True
)

# Create columns for location input and display
col1, col2 = st.columns(2)

with col1:
    st.subheader("Enter Location Coordinates")
    latitude = st.text_input("Latitude")
    longitude = st.text_input("Longitude")
    st.markdown("**Location:** :earth_americas: **DELFT, United Kingdom**")

with col2:
    if latitude and longitude:
        try:
            # Convert inputs to floats
            lat = float(latitude)
            lon = float(longitude)
            
            # Create a DataFrame with the location for the map
            map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
            st.map(map_data)  # Display map with a pin on the location
        except ValueError:
            st.error("Please enter valid numeric values for latitude and longitude.")
    else:
        st.write("Waiting for valid latitude and longitude values...")

# Add a divider between sections
st.divider()

# Create columns for charger specs and image
spec_col, image_col = st.columns(2)

with spec_col:
    st.subheader("Enter Charger Specs")
    max_power = st.slider("Max Power (kW)", min_value=0, max_value=150, step=1)
    min_power = st.slider("Min Power (kW)", min_value=0, max_value=150, step=1)
    charging_capacity = st.text_input("Charging Capacity (kWh)")

with image_col:
    st.image("/Users/tiagovhp/Ironhack/Final_Project/Presentation/Image_EV_Station.webp", 
             caption="Charger Image", use_container_width=True)

# Add a divider
st.divider()

# Display predicted utilization rate only after clicking the submit button and validating inputs
if st.button("Calculate Utilization Rate"):
    # Check if all inputs are provided
    if latitude and longitude and max_power and min_power and charging_capacity:
        try:
            # Ensure latitude and longitude can be converted to floats
            float(latitude)
            float(longitude)
            
            # Display utilization rate
            st.metric(label="Predicted Charger Utilization Rate", value="70.3%", delta="± 2%")
        except ValueError:
            st.error("Please ensure all inputs are correctly formatted.")
    else:
        st.error("Please fill in all fields to calculate the utilization rate.")
