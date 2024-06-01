import fnmatch
from sys import *
import os
import hashlib

def hashfile(path,blocksize = 65536):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    dups = {}
    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups

    else:
        print("Invalid path")

def PrintDuplicate(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates found : ")

        print("The following files are identical")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print('\t\t%s'%subresult)
            icnt = 0
    else:
        print("No duplicate files found")


def DeleteFiles(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))
    icnt = 0
    
    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0
    else:
        print("No duplicate files found")


def main():
    print("--------------------------------------------")

    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if(argv[1] == "--h") or (argv[1] == "--H"):
        print("This script is used to traverse specific directory and display checksum of files")
        exit()
    
    if(argv[1] == "--u") or (argv[1] == "--U"):
        print("Usage : ApplicationName AbsolutePath_Of_Directory")
        exit()    

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)
        DeleteFiles(arr)
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input ",E)

if __name__ == "__main__":
    main()