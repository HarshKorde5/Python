import psutil

def CreateLog(FileName = "Output.log"):
    fd = open(FileName,"w")
    separator = "-"*70

    fd.write(separator+"\n")
    fd.write("My Process Log"+"\n")
    fd.write(separator+"\n")

    fd.write("CONTENTS OF LOG FILE"+"\n")

    fd.write(separator+"\n")

    fd.close()

def main():
    CreateLog()

if __name__ == "__main__":
    main()