import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def TitanicLogisticReg():
    #Step 1 : Load data
    titanic_data = pd.read_csv(r"C:\Users\91779\Desktop\Python2\CSV\MarvellousTitanicDataset.csv",index_col = 0)

    print("First 5 entries from the loaded dataset : ")
    print(titanic_data.head(5))

    print("Number of passengers are : "+str(len(titanic_data)))

    print("Shape of data : ",titanic_data.shape)

    #Step 2 : Analyze data
    print("Visualisation : Survived and non survived passengers")
    figure()
    target = "Survived"
    countplot(data = titanic_data, x = target).set_title("Survived and Non-Survived passengers")
    show()

    print("Visualisation : Survived and non survived passengers based on gender")
    figure()
    target = "Survived"
    countplot(data = titanic_data, x = target,hue = "Sex").set_title("Survived and Non-Survived passengers based on Gender")
    show()

    print("Visualisation : Survived and non survived passengers based on Passenger class")
    figure()
    target = "Survived"
    countplot(data = titanic_data, x = target,hue = "Pclass").set_title("Survived and Non-Survived passengers based on Passenger class")
    show()

    print("Visualisation : Survived and non survived passengers based on Age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Survived and Non-Survived passengers based on Passenger Age")
    show()

    print("Visualisation : Survived and non survived passengers based on Fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Survived and Non-Survived passengers based on Passenger Fare")
    show()

    #Step 3 : Data cleaning 
    titanic_data.drop("zero",axis = 1,inplace = True)

    print("First 5 entries from the loaded dataset : ")
    print(titanic_data.head(5))


    print("Values of data set after removing irrelavant columns : ")
    titanic_data.drop(["sibsp","Parch","Embarked"],axis = 1,inplace = True)
    print(titanic_data.head(5))
    
    x = titanic_data.drop("Survived",axis = 1)
    y = titanic_data["Survived"]

    #Step 4 : Data Training
    data_train,data_test,target_train,target_test = train_test_split(x,y,test_size = 0.3)

    logmodel = LogisticRegression()

    logmodel.fit(data_train,target_train)

    #Step 5 : Data Testing
    prediction = logmodel.predict(data_test)

    #Step 5 : Calculate accuracy
    print("Classification report of Logistic Regression is : ")
    print(classification_report(target_test,prediction))

    print("Confusion matrix of Logistic Regression is : ")
    print(confusion_matrix(target_test,prediction))

    print("Accuracy of Logistic Regression is : ")
    print(accuracy_score(target_test,prediction)*100)


def main():
    border = "-"*100
    print(border)
    print("Supervised Machine Learning")
    print(border)
    print("Logistic Regression on Titanic data set")
    print(border)

    TitanicLogisticReg()
    print(border)


if __name__ == "__main__":
    main()