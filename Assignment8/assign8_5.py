#design a python application which contains two threads, thread1 diplays 1 to50 and thread 2 dipalys 50 to1 in reverse, after competion of 1 second gets started.
import threading
def Display1(no):
    for i in range(50):
        print(i,end="  ")
    print()

def Display2(no):
    for i in range(50,0,-1):
        print(i,end="  ")
    print()

def main():
    print("Inside main :")
    T1 = threading.Thread(target=Display1,args = (50,))
    T2 = threading.Thread(target=Display2,args = (50,))

    T1.start()
    T1.join()
    T2.start()
    print("exit from main")

if __name__ == "__main__":
    main()