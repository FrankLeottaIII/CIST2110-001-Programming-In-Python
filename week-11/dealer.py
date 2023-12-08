from dealership_helper import Car, ElectricCar


# from the Car class, we are inheriting all of the attributes and methods

# from the Car class, create a car Object

car1 = Car("Toyota", "Camry", 2019, 25000)

car2 = Car("Honda", "Accord", 2019, 30000)


car1.price = 15000

print(car1)

car1.update_odometer(60)

car1.increment_odometer(100)

print(car1.odometer_reading)


# Create a ElectricCar Object

electric_car1 = ElectricCar(
    make="Tesla", model="Model 3", year=2020, price=40000, battery_cycle_count=75
)

print(electric_car1.describe_battery())
