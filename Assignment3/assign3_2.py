#accept n numers from user store it into list return the max of that list

def Max(list1,no):
    max =0
    for i in range(no):
        if(max < list1[i]):max = list1[i]
    return max
def main():
    no = int(input("Enter the number of elements that u want to insert to list :"))
    list1 = []
    for i in range (no):
        num = int(input("Enter the element to list :"))
        list1.append(num)

    print(list1)
    ret = Max(list1,no)
    print("maximum of all the elements of list is :",ret)
if __name__ == "__main__":
    main()