class Vehicle:
    def Start(self):
        print("this car is automatic for starting...")

class car(Vehicle):
    def __init__(self):
        super().__init__()
    
    def Start(self):
        print("Start the BMW car this time...")


def main():
    obj = car()
    obj.Start()
if __name__ == "__main__":
    main()