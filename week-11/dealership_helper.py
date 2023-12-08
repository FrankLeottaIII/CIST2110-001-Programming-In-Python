# Python Object Oriented Programming

# Creating a class
# class ClassName:


class Car:
    """This is a Car class. A car has a make, model, year, and price. The price is private. The odometer reading is public.

    Returns:
        Car: A Car object
    """

    # This creates a car class
    # Class Constructor - this is the function that is called when you create a new object
    # Class Attributes - these are the attributes that all cars will have
    def __init__(self, make, model, year, price):
        # above is the constructor. It is taking in arguments
        self.make = make  # This is an attribute
        self.model = model  # This is an attribute
        self.year = year  # This is an attribute
        self.__price = price  # This is an attribute
        self.odometer_reading = 0  # This is an attribute

    # this is commonly referred to as a "getter" or a to_string() method
    def __str__(self):
        return f"{self.make} {self.model} {self.year} ${self.price}"

    @property
    # Getter
    def price(self) -> int:
        """returns the price of the car

        Returns:
            int: the price of the car
        """
        return self.__price

    @price.setter
    # Setter
    def price(self, new_price):
        self.__price = new_price

    # Class Methods - these are the methods that all cars will have
    def update_odometer(self, mileage: int):
        """update the odometer reading to the new mileage

        Args:
            mileage (int): the new mileage
        """
        if mileage >= self.odometer_reading and mileage >= 0:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer")

    def increment_odometer(self, miles: int):
        """add miles to the odometer reading

        Args:
            miles (int): the miles to add to the odometer reading
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You cannot roll back an odometer")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year, price, battery_cycle_count):
        """Initialize attributes of the parent class"""
        super().__init__(
            make, model, year, price
        )  # This is calling the constructor of the parent class
        # super() is a reference to the parent class
        self.battery_cycle_count = battery_cycle_count

    def __str__(self):
        return f"{self.make} {self.model} {self.year} ${self.price} {self.battery_cycle_count}"

    def describe_battery(self):
        """Print a statement describing the battery cycle count"""
        return f"This {self.make} {self.model} has a cycle count of {self.battery_cycle_count}"
