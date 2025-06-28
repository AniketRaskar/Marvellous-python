#print the patter using recursion
'''
*
*   *
*   *   *
*   *   *   *
'''

def PrintPat(no):
    if no==0:
        return
    PrintPat(no-1)
    for i in range(no):
        print("*",end=" ")
    print() 
    

def main():

    no = int(input("Enter the number : "))
    ans =PrintPat(no)

if __name__ == "__main__":
    main()