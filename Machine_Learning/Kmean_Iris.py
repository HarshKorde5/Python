import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def KMeans_Iris():

    #Load data
    iris_data = load_iris()

    X = np.array(iris_data.data)

    #print(X)

    kmeans = KMeans(n_clusters = 3)

    #train model
    kmeans.fit(X)
    
    print(kmeans.labels_)
    print(iris_data.target)

    fig, ax = plt.subplots(1, 2, figsize=(7, 3))
    ax[0].scatter(X_pca['PC1'], X_pca['PC2'], c=changedPredictions)
    ax[1].scatter(X_pca['PC1'], X_pca['PC2'], c=labels)
    ax[0].set_title('Prediction')
    ax[1].set_title('Truth')


def main():
    border = "-"*50
    print(border)
    print("Unspervised Machine Learning")
    print(border)
    print("Clustering using KMean Algorithm on Iris dataset")
    print(border)
    KMeans_Iris()

if __name__ == "__main__":
    main()