#write a recursive function to calculate sum of first N natural no  


def CalSum(no):
    if no==0:
        return 0
    return no + CalSum((no-1))

def main():

    no = int(input("Enter the number : "))
    ans =CalSum(no)
    print("sum of natural number upto : ",no," :is :",ans)

if __name__ == "__main__":
    main()