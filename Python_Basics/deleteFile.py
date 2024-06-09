import os

def main():
    print("Enter the name of file that you want to delete : ")
    Fname = input()

    if os.path.exists(Fname):
        os.remove(Fname)
        print("File is successfully deleted")
        
    else:
        print("Unable to delete file as file is not present in current directory")

if __name__ == "__main__":
    main()
