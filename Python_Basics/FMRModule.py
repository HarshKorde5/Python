
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
