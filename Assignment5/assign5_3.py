#accept the age from user and chk wheather user is eligible to vote

def chkVoter(age):
    if((age)>=18):
        return True
    else :
        return False
def main():
    age = int(input("Enter the age of the user :"))
    result = chkVoter(age)
    if(result == True):
        print("User is voter ")
    else:
        print("User is not voter")
if __name__ =="__main__":
    main()