import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def Advertising(data_path):
    data = pd.read_csv(data_path,index_col=0)

    print("Shape of data : ",data.shape)

    Y = data.sales.values
    X = data[["TV","radio","newspaper"]].values
    
    reg = LinearRegression()

    reg.fit(X,Y)
    
    print(reg.score(X,Y))


def main():
    border = "-"*50
    print(border)
    print("Supervised machine learning")
    print(border)
    print("Play Prediction using KNN algorithm")
    print(border)
    
    Advertising(r"C:\Users\91779\Desktop\Python2\CSV\Advertising.csv")

if __name__ == "__main__":
    main()