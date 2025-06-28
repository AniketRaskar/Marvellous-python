#print triangle pattern using nested loop
'''
*
*   *
*   *   *
*   *   *   *
'''

def main():
    for i in range(1,5):
        for j in range(1,i+1):
            print("*","\t",end=" ")
        print("\n")
if __name__ == "__main__":
    main()