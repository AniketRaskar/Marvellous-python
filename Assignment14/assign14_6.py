class Calculator:
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Addtion(self):
        return self.no1 + self.no2
    
    def Substraction(self):
        return self.no1 - self.no2
    
    def Multiplication(self):
        return self.no1 * self.no2
    
    def Division(self):
        return self.no1 / self.no2
    
def main():
    obj = Calculator(40,10)

    ret= obj.Addtion()
    print("Addtion of given numbers is :",ret)

    ret= obj.Substraction()
    print("Subatraction of given numbers is :",ret)

    ret= obj.Multiplication()
    print("Multiplication of given numbers is :",ret)

    ret= obj.Division()
    print("Division of given numbers is :",ret)

if __name__ =="__main__":
    main()