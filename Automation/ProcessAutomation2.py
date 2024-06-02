import psutil

def DisplayProcess():

    print("List of running processes are : ")

    print("_____________________________________________________________")

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)

    print("_____________________________________________________________")

def main():
    DisplayProcess()

if __name__ == "__main__":
    main()