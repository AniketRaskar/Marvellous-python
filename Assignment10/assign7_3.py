#accept the list of numbers from users and use filter to keep only even numbers
def filterX(list):
    li=[]
    for i in range(len(list)):
        no = list[i]
        if(no %2==0):
            li.append(no)
    return li

def main():
    list = []
    no = int(input("Enter the number of elements that u want to add to list : "))
    for i in range(1,no+1):
        ele  = int(input("Enter the element that to added to list :"))
        list.append(ele)
    print(list)
    listM = filterX(list)
    print(listM)
if __name__ == "__main__":
    main()