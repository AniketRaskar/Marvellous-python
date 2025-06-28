
class BookStore:
    NoOfBooks =0
    def __init__(self,naw,lekhak):
        self.Name = naw
        self.Author = lekhak
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print("Number of books are :", self.NoOfBooks)
        print("Name of book is :"+self.Name +" and author of book is : "+self.Author)
        #("Author of book is :"+self.Author)

def main():
    name = input("Enter the name of book :")
    author = input("Enter the name of author: ")

    obj = BookStore(name,author)
    obj.Display()

    obj2 = BookStore("Denis Ritche","C programning")
    obj2.Display()

    obj3 = BookStore("Robert Love","Linux programing system")
    obj3.Display()

if __name__ == "__main__":
    main()