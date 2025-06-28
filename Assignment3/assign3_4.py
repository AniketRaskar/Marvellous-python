# frequency_counter.py

def main():
    print("Entet the number of elements :")
    size  =int(input())

    data = list()

    print("enter the values:")
    for i in range(size):
        data.append(int(input()))
    print("Enter the number :")
    value1 = int(input())
    count =0
    for i in data:
        if value1 == i:
            count = count +1
    print("Frequency of number is :",count)

if __name__ == "__main__":
    main()
