#write a recursive function to calculate power of x  



def PowerX(no,pow):
    if(pow == 0):
        return 1
    return no * PowerX(no,(pow-1))
    
def main():

    no = int(input("Enter the number : "))
    pow = int(input("Enter number which power u want to find: "))
    ans =PowerX(no,pow)
    print(pow," : power of num :",no," is :",ans)

if __name__ == "__main__":
    main()