#design python application which will design two threads evenfactor and oddfactor, even will display addition of even factors and oddfactors will display addition of odd factors

import threading
import time

def EvenFactor(no,return_val):
    print("inside Even factor ")
    sum_even =0
    for i in range(1,int(no/2)+1):
        if((no % i == 0) and (i%2==0)):
            sum_even = sum_even +i
    return_val[0] = sum_even
    
        
def OddFactor(no,return_val):
    print("Inside odd factor")
    sum_odd =0
    for i in range(2,int(no/2)+1):
        if ((no %i==0) and (i%2==1)):
            sum_odd = sum_odd +i
    return_val[0] = sum_odd
    

def main():
    no = int(input("Enter the number whos factors u want calculate :"))
    curr_time = time.time()

    return_val_fromEven = [None] * 1
    return_val_fromOdd = [None] * 1


    T1 = threading.Thread(target= EvenFactor,args=(no,return_val_fromEven))
    T2 = threading.Thread(target= OddFactor,args=(no,return_val_fromOdd))

    T1.start()
    T2.start()
    T1.join()
    T2.join()
    
    print("Sum of even factor is: ", return_val_fromEven)
    print("Sum of odd factor is :", return_val_fromOdd)
    print("End main")

    end_time = time.time()
    print("Required time is :",end_time-curr_time)
    print("Exit from main ")
    

if __name__ == "__main__":
    main()