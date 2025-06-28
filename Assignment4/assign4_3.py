#write a prgoram which contains filter map reduce, which accept a list of numbers and filtet will take numbers which are greatert than 70 and less than 90,map will increase them by 10, and reduce will make product of them

def FilterX(list):
    fil = []
    for i in list:
        print(i)
        if(i in range(70,90)):
            fil.append(i)
        
    #print("List after filer is :",fil)
    return fil

def mapX(list):
    for i in range(len(list)):
        list[i]= list[i]+10
    #print(list)
    return list

def reduceX(list):
    ans = 1
    for i in range(len(list)):
        ans = ans * list[i]
    return ans

def main():
    list =[]
    size = int(input("Enter the number of elements that u want to insert into the list :"))
    for i in range(1,size+1):
        in1 = int(input("Enter the element at index : "))
        list.append(in1)
    print("list is as below :",list)

    listFX = FilterX(list)
    #print("List after filter is :",listX)
    listMX = mapX(listFX)

    listRX = reduceX(listMX)
    print("Result after filter map reduce on list is : ",listRX)
if __name__ == "__main__":
    main()