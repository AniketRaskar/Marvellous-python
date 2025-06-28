#write a program to accept a number from user and find addition of its digits

def countDgt(no):
 
    sum =0
    digit =0
    while(no !=0):
        digit = no %10
        sum = sum +digit
        no = int(no/10)
        
        
    return sum

def main():
    no = int(input("enter the number: "))
    ans = countDgt(no)
    print("summation of digits of number :",no, "is : ",ans)

if __name__ == "__main__":
    main()