import time
import os
import sys

def DirectoryWatcher(DirName):

    flag = os.path.isabs(DirName)

    if (flag == False):
        print("Path is not absolute path")
        DirName = os.path.abspath(DirName)
        print("Converted absolute path is : ",DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername,subfoldername,filename in os.walk(DirName):  
            for name in filename:
                    print("File name is : ",os.path.join(foldername,name))
                    #foldername+"/"+name                note:this "/" is os specific i.e for windows its "\" and for linux based its "/" so we use os.path.join which is os specific
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