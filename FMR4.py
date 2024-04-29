from functools import reduce

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

    FData = list(filter(CheckEven,Data))
    print("Data after filter activity : ",FData)

    MData = list(map(Increase,FData))
    print("Data after map activity : ",MData)

    RData = reduce(Add,MData)
    print("Data after reduce activity : ",RData)

if __name__ == "__main__":
    main()