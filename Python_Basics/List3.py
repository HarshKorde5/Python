
def main():
    print("Enter number of elements you want to insert in the list : ")
    Size = int(input())
    
    Arr = list()

    print("Enter the elements : ")
    for i in range(Size):
        No = int(input())
        Arr.append(No)

    print("Entered elements are : ",Arr)


if __name__ == "__main__":
    main()