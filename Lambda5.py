
#Name = lambda Parameters : Logic
#Name(___,___,....)

def ChkEven(A):
    if A%2 == 0:
        return true
    else:
        return false

def main():
    ret = ChkEven(2)
    if ret == 0:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()