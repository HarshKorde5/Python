from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def main():
    print("-----Iris Flower Classification Case Study-----")

    _iris = load_iris()
    
    #print(t_iris)

    Features = _iris.data
    Labels = _iris.target

    data_train,data_test,target_train,target_test = train_test_split(Features,Labels,test_size = 0.5)

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(data_train,target_train)
    
    output = obj.predict(data_test)

    Accuracy = accuracy_score(target_test,output)       #accuracy changes everytime we run this program due to shuffling of data and formation of different trees in DecisionTreeClassifier due to shuffling of data

    print("Accuracy of the model is : ",Accuracy*100,"%")
    
    
if __name__ == "__main__":
    main()