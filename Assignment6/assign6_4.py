#accept a number and print its factorial

def main():
    no = int(input("Enter the number :"))
    fact =1
    for i in range(no,0,-1):
        fact = fact *i
    print("Factorila of the given number is :",fact)

if __name__ == "__main__":
    main()