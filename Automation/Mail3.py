import psutil
import urllib2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os

def is_connected():
    try:
        urllib2.urlopen('http://www.youtube.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def MailSender(FileName,time):
    try:
        fromaddr = ""
        toaddr = ""

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        body = """
        Hello %s,
        Please find attached document which contains Log of running process.
        Log file is created at : %s

        This is an auto generated mail
        
        Thanks & Regards
        Harsh Munjaji Korde
        """%(toaddr,time)

        Subject = """
        Process log generated at : %s
        """%(time)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body,'plain'))



    except Exception as E:
        print("Unable to send mail : ",E)

def CreateLog(foldername = "LogFolder"):
    if not os.path.isdir(foldername):
        try:
            os.mkdir(foldername)
        except:
            pass

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(":","_")

    log_path = os.path.join(foldername,"Log_%s.log"%timestamp)

    fd = open(log_path,"a")

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

    return log_path,time.time()

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
    log_path,log_time = CreateLog()
    
    connected = is_connected()
    
    if connected:
        starttime = time.time()
        MailSender(log_path,log_time)
        endtime = time.time()
        print("Took %s seconds to send mail"%endtime-starttime)
    else:
        print("There is no internet connection")
    


if __name__ == "__main__":
    main()