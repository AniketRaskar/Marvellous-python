#write a program which accepts a number from user and displays the pattern
# no = 5
# * * * * *
# * * * *
# * * *
# * *
# *

def display(no):
    temp = no
    for i in range( 1,temp+1):
        for j in range(1,temp-i+2):
            print("* ",end=' ')
        print()
    

def main():
    no = int(input("Enter the number :"))
    display(no)

if __name__ == "__main__":
    main()