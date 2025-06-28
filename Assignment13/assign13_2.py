
class BankAccount:
    ROI = 10.5
    def __init__(self,nam,paise):
        self.Name = nam
        self.Amount = paise

    def Deposit(self,paise):
        print("Amount before deposit is :",self.Amount)
        self.Amount = self.Amount + paise
        print("Amount after deposit is : ",self.Amount)

    def Widhdraw(self,paise):
        print("Amount before withdrawal is :",self.Amount)
        self.Amount = self.Amount - paise
        print("Amount after withdrawal is : ",self.Amount)

    def CalInterset(self):
        interest = (self.Amount //100) * BankAccount.ROI
        print("Calcultaed interest on your amount is : ",interest)

    def Display(self):
        print("Name of account holder is :"+self.Name +"and account balance is :",self.Amount)
        




def main():
    obj = BankAccount("Aniket",10000)
    obj.Display()
    obj.Deposit(5000)
    obj.Display()
    obj.Widhdraw(2000)
    obj.Display()
    obj.CalInterset()
if __name__ =="__main__":
    main()