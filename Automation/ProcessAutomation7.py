import psutil
import time 
import schedule
import os

def CreateLog(FolderName = "LogFolder"):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    FileName = os.path.join(FolderName,"Mylog.log")
    

    fd = open(FileName,"a")
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
    schedule.every(1).minutes.do(CreateLog)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()