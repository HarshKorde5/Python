def Display(Cnt):

    if(Cnt <= 0):
        print("Invalid Input")
        return

    for i in range(Cnt):
        print("Jai Ganesh...",end = " ")

def main():
    Cnt = int(input("Please enter frequency : "))
    Display(Cnt)

if __name__ == "__main__":
    main()