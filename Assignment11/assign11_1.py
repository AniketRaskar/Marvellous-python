#print the numbers form 1 to n by using recursion

def Display(no):
    if(no==0):
        return
    Display(no-1)
    print(no)
    
def main():

    no = int(input("Enter the number : "))
    Display(no)

if __name__ == "__main__":
    main()