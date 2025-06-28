#accept N numbers from user and find addition of prime numbers from that list.

def chkPrime(no):
    for i in range(2,int(no/2+1)):
        if((no %i)==0):
            return False
    return True

def main():
    print("Inmian")
    size = int(input(("Enter the how many numbers u want to insert to the list :")))
    list = []
    for i in range(size):
        no = int(input("Enter the element  :"))
        list.append(no)

    print(list)

    sum =0
    for i in range(0,size):
        ans = chkPrime(list[i])
        if(ans == True):
            sum = sum +list[i]
    print("summation of all prime numbers from list is :",sum)


if __name__ == "__main__":
    main()