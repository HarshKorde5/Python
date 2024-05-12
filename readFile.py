import os

def main():
    print("Enter the name of file that you want to read : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname,"r")
        print("File is successfully opened in appened mode")

        Data = fobj.read()

        print(Data)
        
        fobj.close()
        
    else:
        print("Unable to open file as file is not present in current directory")

if __name__ == "__main__":
    main()
