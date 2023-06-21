#parent class
class Vehicle:

    # __init__ is a python constructor
    # is used to assign value to the attributes of the object
    #default all the vehicle is available
    def __init__(self, brand, model, year, mileage, rental_price, plate_number,availability=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.rental_price = rental_price
        self.plate_number = plate_number
        self.availability = availability
    
    def set_availability(self, availability):
        self.availability = availability

    def get_availability(self):
        return self.availability

#1st child class, inherits from Vehicle (parent class)
class Car(Vehicle):

    #use super().__init__ is a python constructor 
    #It allows the child class to inherit and initialize the attributes and behavior defined in the parent classto initialize the attributes and behavior defined in the parent class
    def __init__(self, brand, model, year, mileage, rental_price, plate_number, doors, seats,availability=True):
        super().__init__(brand, model, year, mileage, rental_price, plate_number, availability)
        self.doors = doors
        self.seats = seats

    def get_seat_capacity(self):
        return self.seats
    
    def print_info(self):
        print("-------------------")
        print("Vehicle Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Mileage:", self.mileage)
        print("Rental Price:", self.rental_price)
        print("Door:", self.doors)
        print("Seat:", self.seats)

    def print_with_id(self, id):
        self.print_info()
        print("Unique ID:", id)
        print("--------------------\n")

    
#2nd child class, inherits from Vehicle (parent class)
class Bike(Vehicle):
    
    def __init__(self, brand, model, year, mileage, rental_price, plate_number,wheel_size,availability=True):
        super().__init__(brand, model, year, mileage, rental_price, plate_number, availability)
        self.wheel_size = wheel_size

    def print_info(self):
        print("-------------------")
        print("Vehicle Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Mileage:", self.mileage)
        print("Rental Price:", self.rental_price)
        print("Wheel Size:", self.wheel_size)
    
    def print_with_id(self, id):
        self.print_info()
        print("Unique ID:", id)
        print("--------------------\n")

    











    