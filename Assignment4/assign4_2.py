#write a function which accepts two paramters and returns its multiplication

multi = lambda no1,no2 : no1 *no2

def main():
    no1 = int(input("Enter the first number "))
    no2 = int(input("Enter the second number :"))

    ans = multi(no1,no2)
    print("Multiplication of given numbers is : ", ans)
if __name__ =="__main__":
    main()