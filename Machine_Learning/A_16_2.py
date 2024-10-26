import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Predictor(data_path):

    #Load Data
    data = pd.read_csv(data_path,index_col=0)
    print("Shape of data : ",data.shape)
    
    Y = data.sales.values
    X1 = data.TV.values
    X2 = data.radio.values
    X3 = data.newspaper.values
    

    print("Values of Independent variables X1 : ",X1)
    print("Values of Independent variables X2 : ",X2)
    print("Values of Independent variables X3 : ",X3)

    print("Values of Depenedent variables Y : ",Y)

    #Least Square Method
    mean_x1 = np.mean(X1)
    mean_x2 = np.mean(X2)
    mean_x3 = np.mean(X3)

    mean_y = np.mean(Y)

    print("Mean of Indepenedent variable X1 : ",mean_x1)
    print("Mean of Indepenedent variable X2 : ",mean_x2)
    print("Mean of Indepenedent variable X3 : ",mean_x3)

    print("Mean of Depenedent variable Y : ",mean_y)
    n1 = len(X1)
    n2 = len(X2)
    n3 = len(X3)

    numerator = 0
    denomenator = 0

    for i in range(1,n1):
        numerator = numerator + (X1[i] - mean_x1) * (Y[i] - mean_y)
        denomenator = denomenator + (X1[i] - mean_x1)**2

    m1 = numerator/denomenator
    
    for i in range(1,n2):
        numerator = numerator + (X2[i] - mean_x2) * (Y[i] - mean_y)
        denomenator = denomenator + (X2[i] - mean_x2)**2

    m2 = numerator/denomenator
    
    for i in range(1,n3):
        numerator = numerator + (X3[i] - mean_x3) * (Y[i] - mean_y)
        denomenator = denomenator + (X3[i] - mean_x3)**2

    m3 = numerator/denomenator

    m = (m1 + m2 + m3)/3
    mean = (mean_x1+mean_x2+mean_x3)/3

    #c = y' - mx'

    c = mean_y - (m * mean)

    print("Slope of Regression line is : ",m)       
    print("Y intercept of Regression line is : ",c)     

    #Display plotting of above points
    x1 = np.linspace(1,6,n1)

    y1 = m1*x1 + c

    plt.plot(x1,y1,color='#58b970',label = 'Regression Line')

    plt.scatter(X1,Y,color='#ef5423',label='scatter plot')

    plt.xlabel('X-Indepenedent Variable')
    plt.ylabel('Y-Depenedent Variable')

    plt.legend()
    plt.show()

    #Find goodness of fit i.e. R Square
    ss_t = 0
    ss_r = 0

    for i in range(n1):
        y_pred = c + m1*X1[i]
        ss_t += (Y[i] - mean_y)**2
        ss_r += (Y[i] - y_pred)**2

    r21 = 1 - (ss_r/ss_t)

    for i in range(n2):
        y_pred = c + m2*X2[i]
        ss_t += (Y[i] - mean_y)**2
        ss_r += (Y[i] - y_pred)**2

    r22 = 1 - (ss_r/ss_t)

    for i in range(n3):
        y_pred = c + m3*X3[i]
        ss_t += (Y[i] - mean_y)**2
        ss_r += (Y[i] - y_pred)**2

    r23 = 1 - (ss_r/ss_t)

    r2 = (r21+r22+r23)/3

    print("Goodness of fit using R2 method is : ",r2)


def main():
    border = "-"*50
    print(border)
    print("Supervised Machine Learning")
    print(border)
    print("User defined implementation of Linear Regression")
    print(border)

    Predictor(r"C:\Users\91779\Desktop\Python2\CSV\Advertising.csv")


if __name__ == "__main__":
    main()