from FMRModule import *

CheckEven = lambda No : (No%2 == 0)
Increase = lambda No : No+1
Add = lambda A,B : A+B

def main():    
    print("Enter size : ")
    size = int(input())

    Data = list()

    print("Enter elements of list : ")
    for i in range(size):
        No = int(input())
        Data.append(No)

    print("Data from input list is : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after filter activity : ",FData)

    MData = list(mapX(Increase,FData))
    print("Data after map activity : ",MData)

    RData = reduceX(Add,MData)
    print("Data after reduce activity : ",RData)

if __name__ == "__main__":
    main()