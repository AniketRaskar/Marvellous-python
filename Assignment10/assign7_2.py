#accept a list of interger from user and use map function double each value

def mapX(list):
    li=[]
    for i in range(len(list)):
        no = list[i]
        li.append(no*2)
    return li
def main():
    list = []
    no = int(input("Enter the number of elements that u want to add to list : "))
    for i in range(1,no+1):
        ele  = int(input("Enter the element that to added to list :"))
        list.append(ele)
    print(list)
    listM = mapX(list)
    print(listM)
if __name__ == "__main__":
    main()