from sklearn import tree
from sklearn.datasets import load_iris

def main():
    print("-----Iris Flower Classification Case Study-----")

    _iris = load_iris()
    
    #print(type(_iris))

    Features = _iris.data
    Labels = _iris.target

    print("Features are : ")
    print(Features)

    print("Labels are : ")
    print(Labels)
    
if __name__ == "__main__":
    main()