import numpy as np
import pickle
import json
import pandas as pd

def predict_price(location,sqft,bath,bhk, modl):

    with open("columns.json", "r") as file:
        col = json.load(file)

    location_col = col['data_columns']

    if location.lower() in location_col:
        loc_index = location_col.index(location.lower())
    #print(type(loc_index))
    x = np.zeros(len(location_col))
    #print(x)
    x[0] = sqft
    #print(x)
    x[1] = bath
    #print(x)
    x[2] = bhk
    #print(x)
    if loc_index >= 0:
        #print(loc_index)
        x[loc_index] = int(1)
    #x_df = pd.DataFrame([x], columns=location_col)

    #print(x)
    return modl.predict([x])[0]

def call_pred(location,sqft,bath,bhk):

    with open("banglore_home_prices_model.pickle", "rb") as f:
        modl = pickle.load(f)

    price_pred = predict_price(location,sqft,bath,bhk, modl)

    return print(round(price_pred,2))


with open('columns.json', 'r') as f:
    location = json.load(f)
location = location['data_columns'][3:]
print(location)

location_ip = input("Please enter the location from the given list above : ")
sqft = int(input("Input the area in sqft : "))
bath = int(input("Input the no of Bathrooms required : "))
bhk = int(input("Input no of rooms or bhk : "))

call_pred(location_ip,sqft,bath,bhk)
#call_pred("2nd phase judicial layout", 1600, 2, 2)
