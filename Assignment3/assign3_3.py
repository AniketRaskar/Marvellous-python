#accept n numers from user store it into list return the min of that list
import sys
def Min(list1,no):
    min = sys.maxsize
    print(min)
    for i in range(no):
        if(min> list1[i]):min = list1[i]
    return min
def main():
    no = int(input("Enter the number of elements that u want to insert to list :"))
    list1 = []
    for i in range (no):
        num = int(input("Enter the element to list :"))
        list1.append(num)

    print(list1)
    ret = Min(list1,no)
    print("minimum of all the elements of list is :",ret)
if __name__ == "__main__":
    main()