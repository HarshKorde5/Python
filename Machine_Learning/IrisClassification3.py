from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def main():
    print("-----Iris Flower Classification Case Study-----")

    _iris = load_iris()
    
    #print(type(_iris))

    Features = _iris.data
    Labels = _iris.target

    data_train,data_test,target_train,target_test = train_test_split(Features,Labels,test_size = 0.5)

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(data_train,target_train)
    
    output = obj.predict(data_test)

    print(output)
    
if __name__ == "__main__":
    main()