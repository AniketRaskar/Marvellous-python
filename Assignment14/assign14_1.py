
class Employee:
    def __init__(self,Nam,indenty,sal):
        self.Name =Nam
        self.ID = indenty
        self.Salary = sal

    def Display(self):
        print("Name of the employee is :"+self.Name +", ID :",self.ID ," Salary : ",self.Salary)
        

def main():
    obj = Employee("Aniket",44,50000)
    obj2 = Employee("Ishawar",14,70000)

    obj.Display()
    obj2.Display()
if __name__ == "__main__":
    main()