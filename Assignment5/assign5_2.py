#accept a character from user and chk wheather it is vovel or consonant
def chk(char):
    if((char =='a' or (char == 'e') or (char=='i') or(char == 'o') or (char == 'u'))):
        return True
    else:
        return False

def main():
    char = input("Enter the character: ")
    result = chk(char)
    if(result == True): 
        print("character is vovel")
    else:
        print("Chracter is consonent")
if __name__ == "__main__":
    main()