import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def LoanApproval():

    #Load Data
    data = pd.read_csv(r'C:\Users\91779\Desktop\Python2\CSV\Loan_Data.csv')
    #print(type(data))  dataframe
    #print("Data before cleaning : \n",data)
    print("Shape of data before cleaning : ",data.shape)

    data.drop(['Loan_ID','Gender','Married','Education'], axis=1,inplace = True)

    data.fillna({'Dependents' : 0},inplace = True)
    data.fillna({'Self_Employed' : "Yes"},inplace = True)
    data.fillna({'Loan_Amount_Term' : 360},inplace = True)
    x = int(data['LoanAmount'].mean(axis = 0))
    data.fillna({'LoanAmount' : x},inplace = True)

    #if credit history null and loan_status N then set 0 else 1
    for x in data.index:
        y = data.loc[x,'Credit_History']
        if np.isnan(y) and data.loc[x,'Loan_Status'] == 'Y':
            data.loc[x,'Credit_History'] = 1
        else:
            data.loc[x,'Credit_History'] = 0

    #data.drop_duplicates(inplace = True)   drops duplicates here none
    data.dropna(inplace = True)

    #print("Data after cleaning : \n",data)
    print("Shape of data after cleaning: ",data.shape)
    


    #Data Encoding
    le = LabelEncoder()

    Labels = data['Loan_Status'].values
    Labels = le.fit_transform(Labels)

    data.drop(['Loan_Status'],inplace = True,axis = 1)
    data["Property_Area"] = le.fit_transform(data["Property_Area"])
    data["Self_Employed"] = le.fit_transform(data["Self_Employed"])
    data["Dependents"] = le.fit_transform(int(data["Dependents"].values))

    print(data.corr())

    Features = data.values

    print("Features after encoding : ")
    print(Features)
    print("Labels after encoding : ")
    print(Labels)


    #Split the dataset into training and testing sets
    data_train,data_test,target_train,target_test = train_test_split(Features,Labels,test_size = 0.3)

    KNN = KNeighborsClassifier(n_neighbors = 7)

    #Train/Fit model
    KNN.fit(data_train,target_train)

    #test model
    Y_pred = KNN.predict(data_test)

    #Accuracy of model
    print("Accuracy : ",accuracy_score(Y_pred,target_test)*100,"%")


def main():
    separator = "-"*50
    print(separator)
    print("Supervised Machine Learning")
    print(separator)
    print("Loan Approval using KNN Algorithm")
    print(separator)

    LoanApproval()

if __name__ == "__main__":
    main()