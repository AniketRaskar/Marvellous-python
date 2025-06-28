def addition(input1,input2):
        ans = input1 + input2
        return ans

def substraction(input1,input2):
     ans = input1-input2
     return ans

def multiplication(input1,input2):
     ans = input1 * input2
     return ans

def division(input1,input2):
     ans = input1 / input2
     return ans
    

def main():
    input1 = int(input("Enter first number : "))
    input2 = int(input("Enter second number :"))

    add = addition(input1,input2)
    sub = substraction(input1,input2)
    multi = multiplication(input1,input2)
    div = division(input1,input2)

    print("Result of addition is :",add)
    print("Result of substraction is :",sub)
    print("Result of multiplication is :",multi)
    print("Result of division is :",div)

if __name__ == "__main__":
    main()