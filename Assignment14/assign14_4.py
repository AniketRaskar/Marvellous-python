class student:
    name = "Aniket "
    Roll_no = 44
    School_Name= "PVG COET Pune "

    def changeSchName(self):
        student.School_Name = "SNDV"

    def Display(self):
        print("Name of the student is :"+self.name)
        print("ROll no of the student is :",self.Roll_no)
        print("School name of the student is :"+self.School_Name)

def main():
    obj = student()
    obj.Display()
    obj.changeSchName()
    obj.Display()

if __name__ =="__main__":
    main()
