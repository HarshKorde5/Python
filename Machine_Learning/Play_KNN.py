import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def PlayPredictor(data_path):

    #Step 1 : Load data
    data = pd.read_csv(data_path,index_col = 0)

    print("Size of actual dataset : ",len(data))

    #Step 2 : Clean,Prepare and manipulate data
    feature_names = ['Whether','Temperature']

    print("Names of Features : ",feature_names)

    Whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    #creating Label encoder
    le = preprocessing.LabelEncoder()
    
    #encode label
    label = le.fit_transform(play)

    #converting string labels into numbers
    weather_encoded = le.fit_transform(Whether)
    print(weather_encoded)

    #converting string labels into numbers
    temperature_encoded = le.fit_transform(Temperature)
    print(temperature_encoded)

    #combining weather and temp into single listof tuples
    features = list(zip(weather_encoded,temperature_encoded))

    #Step 3 : Train data
    model = KNeighborsClassifier(n_neighbors = 3)

    #Train the model using the training sets
    model.fit(features,label)

    #Step 4 : Test data
    predicted = model.predict([[0,2]])      #0:Overcast,2:Mild
    print(predicted)

def main():
    border = "-"*50
    print(border)
    print("Supervised machine learning")
    print(border)
    print("Play Prediction using KNN algorithm")
    print(border)
    
    PlayPredictor(r"C:\Users\91779\Desktop\Python2\CSV\PlayPredictor.csv")

if __name__ == "__main__":
    main()