import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    global __locations
    global __data_columns

    with open('C:/Users/venka/OneDrive/Desktop/banglore_hous/server/artifacts/columns.json','r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    with open('C:\\Users\\venka\\OneDrive\\Desktop\\banglore_hous\\server\\artifacts\\Realestate_price_prediction_model.pickle','rb') as f:
        __model = pickle.load(f)
    return __locations
def get_location_names():
    return __locations



if __name__ == '__main__':
    print('loading....')
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('hudi',1200,2,3),"lakhs")