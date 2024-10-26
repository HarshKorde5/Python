import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Predictor():

    #Load Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variables X : ",X)
    print("Values of Depenedent variables Y : ",Y)

    #Least Square Method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean of Indepenedent variable X : ",mean_x)
    print("Mean of Depenedent variable Y : ",mean_y)
    n = len(X)

    numerator = 0
    denomenator = 0

    for i in range(1,n):
        numerator = numerator + (X[i] - mean_x) * (Y[i] - mean_y)
        denomenator = denomenator + (X[i] - mean_x)**2

    m = numerator/denomenator

    #c = y' - mx'

    c = mean_y - (m * mean_x)

    print("Slope of Regression line is : ",m)       #0.4
    print("Y intercept of Regression line is : ",c)     #2.4

    #Display plotting of above points
    x = np.linspace(1,6,n)

    y = m*x + c

    plt.plot(x,y,color='#58b970',label = 'Regression Line')

    plt.scatter(X,Y,color='#ef5423',label='scatter plot')

    plt.xlabel('X-Indepenedent Variable')
    plt.ylabel('Y-Depenedent Variable')

    plt.legend()
    plt.show()

    #Find goodness of fit i.e. R Square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m *X[i]
        ss_t += (Y[i] - mean_y)**2
        ss_r += (y[i] - y_pred)**2

    r2 = 1 - (ss_r/ss_t)

    print("Goodness of fit using R2 method is : ",r2)


def main():
    border = "-"*50
    print(border)
    print("Supervised Machine Learning")
    print(border)
    print("User defined implementation of Linear Regression")
    print(border)

    Predictor()

if __name__ == "__main__":
    main()