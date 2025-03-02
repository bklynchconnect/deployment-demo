# this file demonstrates the same functionality we saw in used_cars_inference.ipynb but
# within a python script file (.py) instead of a Jupyter notebook

# import modules
import pickle
import numpy as np
import pandas as pd

# unction to load the model
def loadModel(model_file):
    '''
        This function loads a model from a pickle file.

        inputs:
            model_file:     string indicating the file location
        outputs:
            model:          the trained model
    '''
    with open(model_file,'rb') as f:
        model = pickle.load(f)
    return model

# function to generate new data as a dataframe object
def createNewData(year,km,owners,kmpl,engine_cc,power_bhp,seats):
    '''
        This function accepts each feature value as a separate argument and packages them into
        a dataframe.
        inputs:
            year:           car model year
            km:             km's driven (odometry)
            owners:         number of previous owners
            kmpl:           fuel efficiency (km/L)
            engine_cc:      engine volume (cubic centimetres)
            power_bhp:      engine brake horsepower (HP)
            seats:          number of seats in the car

        outputs:
            df_new:         data point packaged as a dataframe object
    '''

    # set up feature columns
    columns = ['year', 'km_driven', 'owners', 'kmpl', 'engine_cc', 'power_bhp', 'seats']

    # construct array from inputs
    X_new = np.array([
            year,
            km,
            owners,
            kmpl,
            engine_cc,
            power_bhp,
            seats
        ])
    
    # package data into a dataframe
    df_new = pd.DataFrame(data=X_new.reshape(1,-1),columns=columns)

    return df_new

# function to run the model and make a prediction
def runPrediction(model,X):
    '''
        This function runs the model to make a prediction.

        inputs:
            model:          trained model
            X:              dataframe or numpy array of input data

        outputs:
            y:              predicted selling price
    '''

    # make prediction
    y = model.predict(X)

    return y

# main function (runs when the file is run through a terminal) -- run in a terminal with "python used_cars_inference.py"
if __name__ == "__main__":

    # load the model from a pickle file
    model = loadModel('models/model.pkl')

    # package new data
    X = createNewData(2019,40000,1,8,1500,300,4)

    # run the model to predict
    y = runPrediction(model,X)

    # print the results
    print(f"Predicted selling price: {y[0]}")