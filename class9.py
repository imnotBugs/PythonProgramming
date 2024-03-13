#Write and exaplain each concept of OOps with example
class car:
    def __init__(self, company ,model,year):
        self.company = company
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started!")
    def stop_engine(self):
        print("Engine stopped!")

#Creating an object of the car class
my_car = car("Toyota" , "Camry", 2022)

#Accessing object attributes
print(f"Company: {my_car.company}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")

#Calling object methods
my_car.start_engine()
my_car.stop_engine()
