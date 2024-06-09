import os

def main():
    print("Enter the name of file that you want to write : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname,"a")
        print("File is successfully opened in appened mode")
        
        print("Enter data that you want to append in the file : ")
        Data = input()

        fobj.write(Data)

        fobj.close()
        
    else:
        print("Unable to open file as file is not present in current directory")

if __name__ == "__main__":
    main()
