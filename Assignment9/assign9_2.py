#write a python program to find squre of numbers in list using various process by using multiprocessing
import multiprocessing.pool
import multiprocessing.process
import os

def fun(no):
    print("Process id of process is :",os.getpid())
    return no *no



def main():
    data = [2,4,6,10,12,14,15,16,18,20,22,54,48,56,58,60,72]

    result = []
    
    p = multiprocessing.Pool()
    result = p.map(fun,data)

    p.close()
    p.join()

    print(result)

if __name__ == "__main__":
    main()