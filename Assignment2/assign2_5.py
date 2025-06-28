#write  a program to accept number from user and chk wheather it is prime or not

def ChkPrime(no):
    
    for i in range(2,int(no/2)+1):
        if(no %i==0): 
            return False
    return True
        
def main():
    no = int(input("Enter the number :"))
    ans = ChkPrime(no)

    if(ans == True): print("It is prime")
    else: print("It is not prime...")

if __name__ =="__main__":
    main()