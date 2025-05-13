#chk for divisibility by five

def chkbool(no):
    if(no %5==0): return True
    else : return False
def main():
    no = int(input("Enter the number :"))
    ans = chkbool(no)
    if(ans==True):print("True")
    else : print("False")
if __name__ == "__main__":
    main()