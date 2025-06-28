
class Rectangle:

    def __init__(self,len,brd):
        self.length = len
        self.breadth = brd

    def Area(self):
        ara = self.length * self.breadth
        return ara
    
    def perimeter(self):
        peri = 2* (self.length + self.breadth)
        return peri
    
def main():
    obj = Rectangle(5,10)
    A = obj.Area()
    print("Area of the reactangel is :",A)

    P = obj.perimeter()
    print("Perimeter of the reactangel is : ",P)

if __name__ == "__main__":
    main()