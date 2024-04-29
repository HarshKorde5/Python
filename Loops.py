
def DisplayF():
    print("Inside Display of for loop")
    i = 0
    for i in range(1,6):
        print(i)

def DisplayW():
    print("Inside Display of while loop")
    i = 1
    while(i <= 5):
        print(i)
        i = i + 1

def main():
    DisplayF()
    DisplayW()

if __name__ == "__main__":
    main()