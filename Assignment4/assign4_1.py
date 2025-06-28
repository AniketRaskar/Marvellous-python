#write a program which accepts one parameter and return the power of 2

'''def PowerX(no):
    ans = 1
    for i in range (1,no+1):
        ans= ans*2
    return ans '''

ans = lambda no : 2 ** no

def main():
    no = int(input("Enter the number :"))
    pow = ans(no)
    print("Power of two is : ",pow )
if __name__ == "__main__":
    main()