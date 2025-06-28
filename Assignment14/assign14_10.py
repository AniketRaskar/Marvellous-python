class Employee:
    def __init__(self,naw,Dept,sal):
        self.Name = naw
        self._Deparment = Dept
        self.__Salary = sal

    def Display(self):
        print("Name of the employee is : "+self.Name)
        print("Department of the employee is :"+self._Deparment)
        print("Salary of the employee is :",self.__Salary)

def main():
    obj = Employee("Raj","SDE",50000)
    obj.Display()

if __name__ =="__main__":
    main()