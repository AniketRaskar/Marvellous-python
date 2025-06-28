#accept n numers from user store it into list return the summantion of that list

def addition(list1,no):
    sum =0
    for i in range(no):
        sum = sum+list1[i]
    return sum
def main():
    no = int(input("Enter the number of elements that u want to insert to list :"))
    list1 = []
    for i in range (no):
        num = int(input("Enter the element to list :"))
        list1.append(num)

    print(list1)
    ret = addition(list1,no)
    print("Summation of all the elements of list is :",ret)
if __name__ == "__main__":
    main()