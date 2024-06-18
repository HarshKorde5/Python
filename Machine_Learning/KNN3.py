from sklearn.neighbors import KNeighborsClassifier

def main():
    Features = [[4,3],[6,7],[7,8],[5,5],[8,8]]
    Labels = [0,1,1,0,1]

    neigh = KNeighborsClassifier(n_neighbors = 3)
    neigh.fit(Features,Labels)

    print(neigh.predict([[6,8]]))

if __name__ == "__main__":
    main()