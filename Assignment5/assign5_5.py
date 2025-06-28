#write the program to chk wheather the gieven number is even or odd

def chkEven(no):
    if(no%2==0):
        return True
    else:
        return False
def main():
    no1 = int(input("Enter the number :"))
    result = chkEven(no1)
    if(result== True):
        print("Given number is even")
    else:
        print("Given number is odd")
if __name__ =="__main__":
    main()