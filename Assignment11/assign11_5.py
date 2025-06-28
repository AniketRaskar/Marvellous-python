#write a recursive function to calculate number of zeroes in the number  


def CalZero(no):
    if no==0:
        return 0
    digit = no %10
    no = int(no/10)
    if digit==0:
        return 1 + CalZero(no)
    else:
        return CalZero(no) 

def main():

    no = int(input("Enter the number : "))
    ans =CalZero(no)
    print("Number of zeroes in the number :",no,": are: ",ans)

if __name__ == "__main__":
    main()