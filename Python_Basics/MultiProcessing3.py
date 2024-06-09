def Display_Even(No):
    print("List of even numbers : ")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2
        

def Display_Odd(No):
    print("List of odd numbers : ")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2
        

def main():
    print("Enter number : ")
    No = int(input())

    Display_Even(No)
    Display_Odd(No)

if __name__ == "__main__":
    main()