import multiprocessing
import os

def EvenDisplay(No):
    print("PID of even process : ",os.getpid())

    print("List of even numbers : ")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2
        

def OddDisplay(No):
    print("PID of odd process : ",os.getpid())

    print("List of odd numbers : ")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2
        

def main():
    print("PID of main process : ",os.getpid())

    print("Enter number : ")
    No = int(input())

    p1 = multiprocessing.Process(target = EvenDisplay, args = (No,))
    p2 = multiprocessing.Process(target = OddDisplay, args = (No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")

if __name__ == "__main__":
    main()