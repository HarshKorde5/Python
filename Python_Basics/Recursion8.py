
def DisplayR(no):
    if(no != 0):
        print(no)
        DisplayR(no-1)

def main():
    print("Enter number : ")
    no = int(input())

    DisplayR(no)

if __name__ == "__main__":
    main()