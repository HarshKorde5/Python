
CheckEven = lambda No : (No%2 == 0)
Increase = lambda No : No+1
Add = lambda A,B : A+B

# Task : Name of function
#Elements : List of data elements
def filterX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        if(Ret == True):
            Result.append(no)

    return Result

# Task : Name of function
#Elements : List of data elements
def mapX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

# Task : Name of function
#Elements : List of data elements
def reduceX(Task,Elements):
    Result = 0

    for no in Elements:
        Result = Task(Result,no)
    
    return Result

def main():
    Data = [11,14,20,23,18,16,15,20]
    print("Data from input list is : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after filter activity : ",FData)

    MData = list(mapX(Increase,FData))
    print("Data after map activity : ",MData)

    RData = reduceX(Add,MData)
    print("Data after reduce activity : ",RData)

if __name__ == "__main__":
    main()