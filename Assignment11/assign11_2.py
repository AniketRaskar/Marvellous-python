#write a recursive function to calculate factorial of number 



def Fact(no):
    if(no==1):
        return 1
    return no * Fact(no-1)
    
def main():

    no = int(input("Enter the number : "))
    ans =Fact(no)
    print("Factorial of the emtered number is : ",ans)

if __name__ == "__main__":
    main()