#accept the list of numbers from users and use reduce function to find product of all numbers
def reduceX(list):
    ans =1
    for i in range(len(list)):
        no = list[i]
        ans = ans *no
    return ans

def main():
    list = []
    no = int(input("Enter the number of elements that u want to add to list : "))
    for i in range(1,no+1):
        ele  = int(input("Enter the element that to added to list :"))
        list.append(ele)
    print(list)
    listR = reduceX(list)
    print(listR)
if __name__ == "__main__":
    main()