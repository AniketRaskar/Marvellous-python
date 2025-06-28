#accept length and width of rectangle and calculate perimter and area of it
def area(len,wid):
    return len * wid
def peri(len,wid):
    return 2*(len + wid)
def main():
    len = int(input("Enter the length of rectangle : "))
    wid = int(input("Enter the width of rectangle : "))
    a = area(len,wid)
    p = peri(len,wid)
    print("area of the rectangle is : ",a)
    print("perimeter of the rectangle is :",p)
if __name__ == "__main__":
    main()