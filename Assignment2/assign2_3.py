#accept a number from user and return its factorial

def fact(no):
    ans = 1
    for i in range (1,no+1):
        ans = ans *i
    return ans

def main():
    no = int(input("Enter the number: "))
    ans = int(fact(no))
    print("Factorial of the number :",no, " is :",ans)
if __name__ == "__main__":
    main()