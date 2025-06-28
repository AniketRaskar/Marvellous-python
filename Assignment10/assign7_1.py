#write two lamda functions to find square and cube of number
squareX = lambda no :no*no
cubeX = lambda no : no *no *no
def main():
    no = int(input("Enter the number :"))
    sq = squareX(no)
    cu = cubeX(no)
    print("Square of the given number is :",sq)
    print("Cube of the given number is :",cu)

if __name__ == "__main__":
    main()