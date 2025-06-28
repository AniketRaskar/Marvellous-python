#design python application which will design two threads evenadd and oddadd, evenadd will add all the even numbers from the list,and oddadd will add all the odd numbers from the list,and print both

import threading
import time

def Evenadd(list,return_val):
    print("inside Even factor ")
    sum_even =0
    for i in range(len(list)):
        if(list[i]%2==0):
            sum_even = sum_even +list[i]
    return_val[0] = sum_even
    
        
def Oddadd(list,return_val):
    print("Inside odd factor")
    sum_odd =0
    for i in range(len(list)):
        if(list[i]%2==1):
            sum_odd = sum_odd+list[i]
    return_val[0] = sum_odd
    

def main():
    no = int(input("Enter the number of elements u want to add to list :"))
    list = []
    for i in range(no):
        num = int(input("enter the number that u want to add to list :"))
        list.append(num)
    print("list is :",list)
    curr_time = time.time()

    return_val_fromEven = [None] * 1
    return_val_fromOdd = [None] * 1


    T1 = threading.Thread(target= Evenadd,args=(list,return_val_fromEven))
    T2 = threading.Thread(target= Oddadd,args=(list,return_val_fromOdd))

    T1.start()
    T2.start()
    T1.join()
    T2.join()
    
    print("Sum of even numbers from list is: ", return_val_fromEven)
    print("Sum of odd numbers from list is :", return_val_fromOdd)
    print("End main")

    end_time = time.time()
    print("Required time is :",end_time-curr_time)
    print("Exit from main ")
    

if __name__ == "__main__":
    main()