import multiprocessing
import os
import time

def Cube(No):
    Sum = 0
    print("PID is : ",os.getpid())
    for i in range(No):
        Sum = Sum + (No*No*No)
    return Sum


def main():
    starttime = time.time()
    Arr = [100000,2000003,400000,500000]
    Result = []

    p = multiprocessing.Pool();
    Result = p.map(Cube,Arr)
    p.close()
    p.join()

    print(Result)
    endtime = time.time()
    print("Time required for execution : ",endtime-starttime)

if __name__ == "__main__":
    main()