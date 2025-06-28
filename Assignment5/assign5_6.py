#accept the temperatur in celcius and convert it to farenheight
def ConvertF(temp):
    F = float((temp *(9/5))) + 32
    return F
def main():
    temp = int(input("Enter the temperature in celcius :"))
    faren = ConvertF(temp)
    print("Temprature in farenheight is :",faren, " F")
if __name__ == "__main__":
    main()