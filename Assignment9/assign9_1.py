#create the python application with three threads,each prints 1 to 5, with time gap 1 second
import threading
import time


def fun1():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def fun2():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def fun3():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def main():

    curr_time = time.time()
    T1 = threading.Thread(target=fun1)
    T2 = threading.Thread(target=fun2)
    T3 = threading.Thread(target=fun2)
    
    T1.start()
    T2.start()
    T3.start()
    
    T1.join()
    T2.join()
    T3.join()
    final_time = time.time()
    print("Total time taken for execution is: ", final_time - curr_time)


if __name__ == "__main__":
    main()