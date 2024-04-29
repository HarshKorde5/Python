
#Factorial of 5 = 5 * 4 * 3 * 2 * 1 i.e 120

i = 1
Fact = 1

def Factorial(No):
    global i
    global Fact
    
    if(No >= 1):
        Fact = Fact * No
        No = No - 1
        Factorial(No)

    return Fact

def main():
    print("Enter number : ")
    no = int(input())

    Ret = Factorial(no)
    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()