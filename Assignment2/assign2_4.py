#write a program to accept from user and find addition of its factors

def fac_sum(no):
    sum =0
    for i in range (1,int(no/2)+1):
        if(no %i==0):
            sum = sum +i
    return sum
def main():
    no = int(input("Enter the number :"))
    ans = fac_sum(no)
    print("Summation of factors of number: ",no ,"is :",ans)
if __name__ == "__main__":
    main()