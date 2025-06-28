#design a python application which contains three threads small,capital,digit and application accepts string, small thread finds number small characters,capital finds number of capital letters,and digit find number of digits, display id and name of each theread

import threading
from threading import Thread

def small(str,return_val):
    print("Inside small ")
    #print(threading.current_thread().getName())
    print("Thread id of samll is :",threading.get_ident())

    scnt =0
    for i in range(len(str)):
        if(ord(str[i])>= 97 and ord(str[i])<= 122):
            scnt = scnt +1
    return_val[0] = scnt

def capital(str,return_val):
    print("Inside capital ")
    #print(threading.current_thread().getName())

    print("Thread id of capital is :",threading.get_ident())

    ccnt =0
    for i in range(len(str)):
        if(ord(str[i])>= 65 and ord(str[i])<= 90):
            ccnt = ccnt +1
    return_val[0] = ccnt


def digits(str,return_val):
    print("Inside digits ")
    #print(threading.current_thread().getName())

    print("Thread id of digits is :",threading.get_ident())

    dcnt =0
    for i in range(len(str)):
        if(str[i].isdigit()):
            dcnt = dcnt +1
    return_val[0] = dcnt



def main():
    print("Inside main")
    print("Thread id of main is :",threading.get_ident())
    str = input("Enter the string :")

    return_digit = [None]*1
    return_small = [None]*1
    return_capital = [None]*1

    T1 = threading.Thread(target=small,args=(str,return_small))
    T2 = threading.Thread(target=capital,args=(str,return_capital))
    T3 = threading.Thread(target=digits,args=(str,return_digit))

    T1.start()
    T2.start()
    T3.start()

    print("Number of small leterrs :", return_small)
    print("Number of capital leterrs :", return_capital)
    print("Number of digits :", return_digit)

    print("Exit from main ")

if __name__ =="__main__":
    main()