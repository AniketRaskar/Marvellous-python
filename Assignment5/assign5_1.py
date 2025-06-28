#write a program two accept two numbers from the user and dipalay their sum differnece product and division

addition = lambda no1,no2:no1+no2
substraction = lambda no1,no2:no1-no2
multiplication = lambda no1,no2:no1*no2
division = lambda no1,no2:no1/no2


def main():
    input1 = int(input("enter the first number :"))
    input2 = int(input("Entert the second number :"))

    add = addition(input1,input2)
    sub = substraction(input1,input2)
    mul = multiplication(input1,input2)
    div = division(input1,input2)

    print("Addition of two numbers is :",add)
    print("Subtraction of two numbers is :",sub)
    print("multiplication of two numbers is :",mul)
    print("division of two numbers is :",div)
if __name__ =="__main__":
    main()