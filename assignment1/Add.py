
def add(no1,no2):
    ans = no1 +no2
    return ans

def main():
    no1 =int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    ans =add(no1,no2)
    print("Addition of given two numbers is : ",ans)
    

if __name__ == "__main__":
    main()