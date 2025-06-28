#design python application which will design two threads even and odd, even will display first 10 even numbers and odd will display first 10 odd numbers

import threading
import time

def displayEven(no):
    print("inside displayeven ")
    for i in range(no+1):
        if(i%2==0):
            print(i,end=" ")
    print()
        
def displayOdd(no):
    print("Inside displayodd")
    for i in range(no+1):
        if (i %2 != 0):
            print(i,end=" ")
def main():
    no = int(input("Enter the number upto which u want to diaplay :"))
    curr_time = time.time()

    T1 = threading.Thread(target=displayEven(no))
    T2 = threading.Thread(target=displayOdd(no))
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    print("End main")

    end_time = time.time()
    print("Required time is :",end_time-curr_time)
    

if __name__ == "__main__":
    main()