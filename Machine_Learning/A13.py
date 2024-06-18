import numpy
import pandas
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pandas.read_csv(r"C:\Users\91779\Downloads\PlayPredictor.csv")
Features = data[['Whether','Temperature']].values.tolist()
Labels = data['Play'].values.tolist()

le = LabelEncoder()
Labels = le.fit_transform(Labels)

enc = OneHotEncoder()
Features = enc.fit_transform(Features)

data_train,data_test,target_train,target_test = train_test_split(Features,Labels,test_size = 0.5)


neigh = KNeighborsClassifier(n_neighbors = 5)
neigh.fit(data_train,target_train)

predicitions = neigh.predict(data_test)

Accuracy = accuracy_score(target_test,predicitions)
print("Accuracy : ",Accuracy*100,"%")

#Sunny  2
#Overcast  0
#Rainy  1

#Hot  4
#Mild  5
#Cool  3
