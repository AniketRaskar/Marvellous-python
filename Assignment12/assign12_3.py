
class Arithmetic:
    value1 =0
    value2 =0
    def __init__(self,no1,no2):
        print("Inside arithmatic constructor")
        self.value1 =no1
        self.value2 =no2

    def Addition(self):
        return self.value1 + self.value2
    def Substraction(self):
        return self.value1 - self.value2
    def multiplication(self):
        return self.value1 * self.value2
    def division(self):
        return int(self.value1 // self.value2)
    
    def __del__(self):
        print("Inside arithmatic destructor.")
def main():
    no1 = int(input("Enter the first number :"))
    no2 = int(input("Enter the second number :"))

    obj = Arithmetic(no1,no2)

    print("Addtion of numbers is :",obj.Addition())
    print("Substraction of numbers is :",obj.Substraction())
    print("Multiplication of numbers is :",obj.multiplication())
    print("Division of numbers is :",obj.division())

if __name__ == "__main__":
    main()