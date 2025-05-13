#accept name from user and display its length

def main():
    name = input("enter the name :")
    cnt =0
    #sizeX = len(name)
    #print(sizeX)
    for char in name:
        cnt = cnt+1
    print(cnt)


     
if __name__ =="__main__":
    main()