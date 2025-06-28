#write a python program to compare execution time of summing numbers from 1 to 10 million,using normal function,threading, multiprocessing
import multiprocessing.pool
import multiprocessing.process
import threading
import _thread
import os
import time


def sumX(no):
    #print("Process id of process is :",os.getpid())
    return sum(no)

def summation(listx,results,i):
    results[i] = sum(listx)


def sumXX(no):
    x=0
    for i in range(no+1):
        x=x+i
    return x
def main():
    
    startp = time.time()
    start =1
    result = []
    end = 100000000
    chunks = os.cpu_count()
    #print(chunks)
    chunkSize = int((end)/chunks)
    chunkList = []
    for i in range(chunks):
        chunk_start = start + i * chunks
        chunk_end = chunk_start + chunks - 1
        if i==chunks-1:
            chunk_end = end

        chunkList.append(range(chunk_start,chunk_end+1))
       
    p = multiprocessing.Pool(processes=chunks)
    result = p.map(sumX,chunkList)
    p.close()
    p.join()
    print("sum using mulitprocessing is :",sum(result))
    endp = time.time()
    print("Time using multiprocessing is :",endp-startp)

    startt = time.time()
    sumcal =0
    results = [None] * chunks
    tList =[]
    for i in range(len(chunkList)):
        t= threading.Thread(target=summation,args=(chunkList[i],results,i))
        tList.append(t)
        t.start()
    for t in tList:
        t.join()

    sumcal = sum(results)
    endt = time.time()
    print("Summation using multithreading :",sumcal)
    print("Time using multithreading :",endt-startt)

    #normal functiion
    Nstart = time.time()
    sumn = 0
    sumn = sumXX(end)
    print("Normal sum using normal func is :",sumn)
    nend = time.time()
    print("TIme for normal function is :",nend-Nstart)


    

if __name__ == "__main__":
    main()