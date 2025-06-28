#accept the number from and chk wheather it is prime or not

def ChkPrime(no):
    for i in range(2,int((no+1)/2)):
        if(no %i==0):
            return False
    return True
def main():
    no = int(input("Enter the number :"))
    result = ChkPrime(no)
    if(result == True):
        print("Given number is prime")
    else:
        print("Given number is not prime")
if __name__ == "__main__":
    main()