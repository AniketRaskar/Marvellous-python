class Person:
    def __init__(self,naw,way):
        self.Name = naw
        self.Age= way


class Teacher(Person):
    def __init__(self,naw,way,sub,sal):
        self.Subject = sub
        self.Salary = sal
        super().__init__(naw,way)

    def Display(self):
        print("Name of the teacher is :"+self.Name)
        print("Age of the teacher is : ",self.Age)
        print("Subject of the teacher is :",self.Subject)
        print("Salary of the teacher is :",self.Salary)

def main():
    obj = Teacher("kale sir",55,"Physics",50000)
    obj.Display()

if __name__ == "__main__":
    main()