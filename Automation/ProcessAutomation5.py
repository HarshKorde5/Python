import psutil
import time 

def CreateLog(FileName = "Output.log"):
    fd = open(FileName,"w")
    separator = "-"*70

    fd.write(separator+"\n")
    fd.write("My Process Log"+"\n")
    fd.write("Log file created at : "+time.ctime()+"\n")
    fd.write(separator+"\n")

    fd.write("CONTENTS OF LOG FILE"+"\n")

    fd.write(separator+"\n")

    Arr = GetProcessInfo()

    for data in Arr:
        fd.write("%s \n"%data)
    
    fd.write(separator+"\n")

    fd.close()

def GetProcessInfo():
    ListProcess = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        ListProcess.append(proc.info)

    return ListProcess

def main():
    CreateLog()

if __name__ == "__main__":
    main()