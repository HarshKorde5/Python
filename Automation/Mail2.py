import psutil
import time
import os

def is_connected():
    try:
        urllib2.urlopen('http://www.youtube.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False


def CreateLog(foldername = "LogFolder"):
    if not os.path.isdir(foldername):
        try:
            os.mkdir(foldername)
        except:
            pass

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(":","_")

    FileName = os.path.join(foldername,"Log_%s.log"%timestamp)

    fd = open(FileName,"a")

    separator = "-"*100
    fd.write(separator+'\n')
    fd.write("Log file for current processes"+"\n")
    fd.write(separator+'\n')
    fd.write("CONTENTS OF LOG FILE : "+"\n")
    fd.write(separator+'\n')

    starttime = time.time()
    Arr = GetProcessInfo()
    endtime = time.time()
    
    for data in Arr:
        fd.write("%s \n"%data)

    fd.write(separator+'\n')

    fd.close()
    print("Time required for log creation : ",endtime-starttime)

def GetProcessInfo():
    ListProcess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms/(1024*1024)
            ListProcess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    return ListProcess


def main():
    CreateLog()
    
    connected = is_connected()
    


if __name__ == "__main__":
    main()