#write a program to accept a number from user and count digits in it

def countDgt(no):
    cnt =0

    while(no !=0):
        no = int(no/10)
        cnt = cnt+1
        print(no, cnt)
    return cnt

def main():
    no = int(input("enter the number: "))
    ans = countDgt(no)
    print("Number of digits in number :",no, "is :",ans)

if __name__ == "__main__":
    main()