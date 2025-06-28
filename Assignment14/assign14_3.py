#create a class book with private attribue __price.add a method to get and set the price. Show encapsulation.

class Book:
    def __init__(self,nam,kimmat,lekhak):
        self.Name = nam #public
        self.__Price =kimmat  #private
        self._Author = lekhak   #protected

    #get method
    def Get_Price(self):
        return self.__Price
    
    #set method
    def Set_price(self,New_Price):
        self.__Price = New_Price

    #display
    def Display(self):
        print("Name of the book : "+self.Name)
        print("Price of the book : ",self.__Price)
        print("Author of the book : "+self._Author)


def main():
    obj = Book("Yayati",450,"Pu L Deshapande")
    obj.Display()
    obj.Set_price(500)
    obj.Display()
    pri = obj.Get_Price()
    print("Price of the book by getter method is :",pri)

if __name__ == "__main__":
    main()