class BankAccount:
    def __init__(self,no,naw,paise):
        self.Num = no
        self.Name = naw
        self.Balance = paise

    def deposit(self,amt):
        self.Balance = self.Balance + amt
    
    def withdraw(self,amt):
        self.Balance = self.Balance - amt

    def Display(self):
        print("Balance of :"+self.Name +" is :",self.Balance)

def main():
    obj = BankAccount (9821,"Aniket",15000)
    obj.Display()
    obj.deposit(3000)
    obj.Display()
    obj.withdraw(1500)
    obj.Display()
    
if __name__ == "__main__":
    main()