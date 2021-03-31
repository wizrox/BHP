# '''#######################
#
# Courtesy : codebasic (youtube channel)
#
# Tutorial (youtube) : https://www.youtube.com/watch?v=rdfbcdP75KI&list=PLeo1K3hjS3uu7clOTtwsp94PcHbzqpAdg&index=1
#
# git : https://github.com/codebasics/py/tree/master/DataScience/BangloreHomePrices
#
# Disclaimer: I don't own the rights of this project/code, The code was all written as followed
#             by tutorial.
#             P.S. Some of the file/variable names has been changed for personal refrences.
#
#     #######################
# '''


import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("./artifacts/banglore_home_orices_model.pickle", 'rb') as f:  # 'rb' for read Binary file
        __model = pickle.load(f)
    print("loading saved artifacts done....")


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


if __name__ == '__main__':
    load_saved_artifacts()  # if this function won't run before other functions : no data will load in variables
    # __location , __data_columns and would casue errors in other functions
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
