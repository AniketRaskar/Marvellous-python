
def pattern(no):
    for i in range(0,no):
        for j in range (0,no):
            print("*  ",end=' ')
        print()

def main():
    no = int(input("Enter the number : "))
    pattern(no)

if __name__ == "__main__":
    main()