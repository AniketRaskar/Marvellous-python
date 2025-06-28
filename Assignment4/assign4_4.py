#accept a list from user, design a application which contains filter map reduce, filter will take only even numbers from the list, map will find the square of those and reduce will add all those numbers

def filter(list):
    fil =[]
    for i in range(len(list)):
        if(list[i]%2==0):
            fil.append(list[i])
    return fil

def mapX(list):
    mp =[]
    for i in range(len(list)):
        sq = list[i]*list[i]
        mp.append(sq)
    return mp

def reduceX(list):
    ans =0
    for i in range(len(list)):
        ans = ans + list[i]
    return ans
def main():
    size = int(input("enter the number of elements that u want to insert to list:"))
    list =[]
    for i in range(size):
        no = int(input("enter the element at index :"))
        list.append(no)
    print(list)

    listF = filter(list)
    #print(listF)
    listM = mapX(listF)
    #print(listM)
    listR = reduceX(listM)
    print("result after filter map reduce on list is : ",listR)
if __name__== "__main__":
    main()