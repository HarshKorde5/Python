from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():
    wine = datasets.load_wine()

    print(wine.feature_names)

    print(wine.target_names)

    print(wine.data[0:5])

    print(wine.target)

    data_train,data_test,target_train,target_test = train_test_split(wine.data,wine.target,test_size = 0.3)

    knn = KNeighborsClassifier(n_neighbors = 3)         #5 gives more accuracy

    knn.fit(data_train,target_train)

    y_pred = knn.predict(data_test)

    print("Accuracy : ",accuracy_score(target_test,y_pred)*100,"%")

def main():
    border = "-"*50
    print(border)
    print("Supervised Machine Learning")
    print(border)
    print("Wine Prediction using KNN algorithm")
    print(border)

    WinePredictor()

if __name__ == "__main__":
    main()