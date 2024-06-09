
#Name = lambda Parameters : Logic
#Name(___,___,....)

def ChkEven(A):
    return (A%2 == 0)

ChkEvenX = lambda A : A%2

def main():
    ret = ChkEvenX(2)
    if ret:
        print("Odd")
    else:
        print("Even")

if __name__ == "__main__":
    main()