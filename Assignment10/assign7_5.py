#write a function that accepts a string and chk wheather it is pallindrome or not

def chkPall(str):
    
    i=0
    j=len(str)-1
    while (i<j):
        if (str[i]==str[j]):
            i = i+1
            j=j-1
        else:
            return False
    return True
def main():
    str = input("enter the string: ")
    result = chkPall(str)
    if(result == True):
        print("entered string is pallindrome")
    else:
        print("Entered string is not pallindrome")
if __name__ =="__main__":
    main()