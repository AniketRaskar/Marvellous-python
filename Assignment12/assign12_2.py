#write a program which implements the class cirle,

class Circle:
    PI = 3.14

    def __init__(self,rad):
        self.Radius =rad
        self.Area =0.0
        self.Circum =0.0

    
    def Cal_area(self):
        areaX = self.PI * self.Radius * self.Radius
        return areaX
    def Cal_circum(self):
        circumX = 2 * self.PI * self.Radius
        return circumX


def main():
    rad = int(input("Enter the value of radius : "))
    obj1 = Circle(rad)

    print("Area of the circle is :",obj1.Cal_area())
    print("Circumferance of the circle is :",obj1.Cal_circum())

if __name__ == "__main__":
    main()