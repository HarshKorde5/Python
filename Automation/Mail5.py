import psutil
import urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import time
import os
import schedule

def is_connected():
    try:
        urllib.request.urlopen('http://www.youtube.com',timeout=1)
        return True
    except urllib.request.URLError as err:
        return False

def MailSender(FileName,time):
    try:
        fromaddr = "korde0510@gmail.com"
        toaddr = "maskepranav99@gmail.com"

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

        attachment = open(FileName,"rb")

        p = MIMEBase('application','octet-stream')
        
        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition','attachment',filename = FileName)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.ehlo()

        s.starttls()


        s.login(fromaddr,"rosjvmcxjbdowrbv")

        text = msg.as_string()

        s.sendmail(fromaddr,toaddr,text)
        
        s.quit()

        print("Log file successfully sent through Mail")
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

    connected = is_connected()
    
    if connected:
        MailSender(log_path,time.ctime())
    else:
        print("There is no internet connection")

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

    try:
        schedule.every(2).minutes.do(CreateLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as E:
        print("Error : ",E)

if __name__ == "__main__":
    main()