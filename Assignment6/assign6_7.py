#accept 5 numbers from user and find and print largest of them

def main():
    lar =0
    for i  in range(1,6):
        no = int(input("Enter the  number:",i))
        if(no >lar):
            lar = no
    
    print("Largest number of the given number is :",lar)
if __name__ == "__main__":
    main()