# this is a Streamlit demo showing off just how easy it is to set up and run a Streamlit app to use our model in a
# more user-friendly way

# import modules
import streamlit as st
from used_cars_inference import loadModel, createNewData, runPrediction

# define page title configuration (sets the name of the page as well as gives it a logo, note the wide layout)
st.set_page_config(
    page_title='Streamlit Demo for LHL',
    page_icon=':smile:',
    layout='wide'
)

# write some introductory message
st.write('''
            # Used Car Selling Price Prediction
         
            Input the requested parameters to predict the selling price of the car :crystal_ball:
         ''')

# example date input
date = st.date_input('Choose a date')

# set up inputs for each of our features for our model
# we'll do this with each input from left-to-right as a separate column (otherwise each one will be above/below each
# other and take up the whole width of the page)

# create a set of columns (7 in this case)
cols = st.columns(7)

# for each columns...

# access the column (note cols is a list that we can index)
with cols[0]:
    # create a user input (number type) that has a label ('Year') and a default value (2025), store whatever the
    # user enters in the output variable (year)
    year = st.number_input('Year',value=2025)

# ...similar code for each input
with cols[1]:
    km_driven = st.number_input('Total kilometres on the car', value=0)
with cols[2]:
    owners = st.number_input('Number of previous owners', value=1)
with cols[3]:
    kmpl = st.number_input('Mileage (km/L)',value=8)
with cols[4]:
    engine_cc = st.number_input('Engine Volume (cc)',value=1000)
with cols[5]:
    power_bhp = st.number_input('Brake horsepower (HP)',value=300)
with cols[6]:
    seats = st.number_input('Number of seats',value=4)

# load the model from the pickle file
model = loadModel('models/model.pkl')

# package the inputs into the appropriate structure
X = createNewData(year,km_driven,owners,kmpl,engine_cc,power_bhp,seats)

# get our predicted selling price
y = runPrediction(model,X)

# display the prediction on our page
st.write(
        f":car: predicted selling price: ${y[0]:.2f}"
)