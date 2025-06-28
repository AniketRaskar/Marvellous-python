#accept the number from user and display below pattern
#no 5
#1
#1  2
#1  2   3
#1  2   3   4
#1  2   3   4   5

def display(no):
    for i in range (1,no+1):
        for j in range(1,i+1):
            print(j,"   ",end=" ")
        print()
def main():
    no = int(input("Enter the number :"))
    display(no)
if __name__ =="__main__":
    main()