#accept the list of numbers from users and use filter to return list prime numbers
def filterX(list):
    li=[]
    for i in range(len(list)):
        no = list[i]
        for j in range(2,int(list[i]/2)):
            if(list[i]%j==0):
                break
        else:
            li.append(list[i])
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