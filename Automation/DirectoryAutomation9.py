import time
import os
import sys

def DirectoryWatcher(DirName):
    Count = 0
    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername,subfoldername,filename in os.walk(DirName):  
            for name in filename:
                if(os.path.getsize(os.path.join(foldername,name)) == 0):
                    os.remove(os.path.join(foldername,name))
                    print("Deleted file : ",os.path.join(foldername,name))
                    Count = Count + 1
        print("Number of deleted files are : ",Count)
    else:
        print("There is no such directory")

def main():
    print("------------------------------Directory Watcher----------------------------------")
    if(len(sys.argv)==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform Directory traversal")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Useage of the script : ")
            print("Name_Of_File Name_Of_Directory")
            exit()

        try:
            starttime = time.time()
            DirectoryWatcher(sys.argv[1])
            endtime = time.time()

            print("Time required to execute the script is : ",endtime-starttime)
        except Exception as obj:
            print("Unable to do the task due to : ",obj) 

    else:
        print("Invalid option")
        print("Use --h option to get help and use --u to get the usage of application")
        exit()

    print("----------------------------ThankYou for using script----------------------------")

if __name__ == "__main__":
    main()