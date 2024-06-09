import threading
import os

def EvenDisplay(No):

    print("PID of even process : ",os.getpid())
    print("PID of even thread : ",threading.get_ident())

    print("List of even numbers : ")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2
        

def OddDisplay(No):
    print("PID of odd process : ",os.getpid())
    print("PID of odd thread : ",threading.get_ident())

    print("List of odd numbers : ")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2
        

def main():
    print("PID of main process : ",os.getpid())
    print("PID of main thread : ",threading.get_ident())

    print("Enter number : ")
    No = int(input())

    t1 = threading.Thread(target = EvenDisplay, args = (No,))
    t2 = threading.Thread(target = OddDisplay, args = (No,))

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

    print("End of main process")

if __name__ == "__main__":
    main()