
def ChkEvenOdd( no):
    if(no %2==0): print("Given number is even...")
    else : print("Given number is odd...")
    
def main():
    no = int(input("Enter the number: "))
    ChkEvenOdd(no)

if __name__ == "__main__":
    main()