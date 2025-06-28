class Numbers:

    def __init__(self,num):
        self.Value = num

    def ChkPrime(self):
        for i in range(2,int((self.Value/2)+1)):
            if(self.Value%i==0):
                return False
        return True
    
    def SumFactor(self):
        sum=0
        for i in range(1,int(self.Value/2)+1):
            if(self.Value%i==0):
                sum = sum+i
        print("Sum of factors of the number is :",sum)
        return sum
    def ChkPerfect(self):
        sum = Numbers.SumFactor(self)
        if(sum == self.Value):
            return True
        else:
            return False
        
    def Factors(self):
        print("Facotrs of :",self.Value, " are : ")
        for i in range(1,int(self.Value/2)+1):
            if(self.Value%i==0):
                print(i,end="   ")
        print()

def main():
    no = int(input("Enter the number : "))
    obj = Numbers(no)
    ret =obj.ChkPerfect()
    if(ret == True):
        print("Entered number is perfect number")
    else:
        print("Entered number is not perfect number ")

    obj.Factors()

    ret =obj.ChkPrime()
    if(ret == True):
        print("Entered number is prime number")
    else:
        print("Entered number is not prime number ")
    
    FacSum = obj.SumFactor()

if __name__ == "__main__":
    main()