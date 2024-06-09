import os

def main():
    print("Enter the name of file that you want to create : ")
    Fname = input()

    if os.path.exists(Fname):
        print("Unable to create file as file is already existing")

    else:
        open(Fname,"x")
        print("File gets successfully created")

if __name__ == "__main__":
    main()


#Absolute path : "C:\Users\91779\Desktop\Python2Myfile.txt"
#Relative path : "Python2\Myfile.txt"