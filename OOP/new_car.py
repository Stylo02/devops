from OOP.car import Car

car_1 = Car("Toyota", "Corolla", 2015, "Red")
car_2 = Car("Toyota", "Camry", 2018, "Blue")

print(car_1.color)
print(car_2.model)

car_1.drive()
car_2.stop()