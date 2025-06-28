#accept the number from user and print its multiplication table

def main():
    no = int(input("Enter the number :"))
    for i in range(1,11):
        print(no *i)
if __name__ == "__main__":
    main()