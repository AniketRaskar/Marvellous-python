'''write a python application which contain one class name as demo
Demo class contains two instace variable no1,no2
that class contain one class variable as value
'''
class Demo:
    value =11

    def __init__(self,X,Y):
        print("Inside demo constructor..")
        self.no1 = X
        self.no2 = Y

    def gun(self):
        print("Inside method demo gun")
        print(self.no1)
        print(self.no2)

    def fun(self):
        print("Inside demo fun ")
        print(self.no1)
        print(self.no2)

    def __del__(self):
        print("Inside demo destructor")
def main():
    val1 = int(input("Enter the first value :"))
    val2 = int(input("Enter the second value :"))

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.fun()
    obj1.gun()
    obj2.fun()
    obj2.gun()

if __name__ == "__main__":
    main()