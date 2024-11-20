
class Car:
    def __init__(self, make, model, year, color): # Constructor
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The car is moving.")

    def stop(self):
        print("The car" +self.model + " has stopped.")
