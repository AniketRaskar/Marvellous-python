#write a recursive function to calculate sum of digits of number  



def SumOfDigit(no):
    if no ==0:
        return 0
    digit = no %10
    return digit + SumOfDigit(int(no/10))
    
def main():

    no = int(input("Enter the number : "))
    ans =SumOfDigit(no)
    print("Sum of the digits of entered number is : ",ans)

if __name__ == "__main__":
    main()