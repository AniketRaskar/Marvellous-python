#accept 3 numbers from user and find largeest using nested loop condition

def findM(no1,no2,no3):
    if((no1>no2) and (no1>no3)):
        return no1
    elif((no2>no1) and (no2>no3)):
        return no2
    elif((no3>no1) and (no3 > no2)):
        return no3
    
def main():
    no1 = int(input("Enter the first number :"))
    no2 = int(input("Enter the second number :"))
    no3 = int(input("Enter the third number :"))
    max = findM(no1,no2,no3)
    print("Maximum of the given numbers is : ",max)
if __name__ == "__main__":
    main()