#
# The goal of this series is to describe internals and general concepts behind the class object
# in Python 3.6. In this part, I will explain how Python stores and lookups attributes. I
# assume that you already have a basic understanding of object-oriented concepts in Python.
#
# Let's start with a simple class:

class Vehicle:
    kind = 'car'

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model_name = model

    @property
    def name(self):
        return "%s %s" % (self.manufacturer, self.model_name)

    # __repr__ is a built-in function used to compute the "official" string reputation of an object,
    # while __str__ is a built-in function that computes the "informal" string representations of
    # an object.
    def __repr__(self):
        return "<%s>" % self.name

def from_dict(dict):
    instance = Vehicle.__new__(Vehicle)
    instance.__dict__.update(dict)
    return instance

car = Vehicle('Toyota', 'Corolla')
car2 = Vehicle('Honda', 'Civic')
print(car) # <Toyota Corolla>
print(car2) # <Honda Civic>
print(car.kind, car2.kind) # car car
# Vehicle.kind = 'scrap'
# print(car.kind, car2.kind) #scrap scrap

car.kind = 'scrap'
print(car.kind, car2.kind) # scrap car
# In Python, all instance variables are stored as a regular dictionary. When working with
# attributes, you just changing a dictionary.

print(car.__dict__) # {'manufacturer': 'Toyota', 'model_name': 'Corolla', 'kind': 'scrap'}
print(car2.__dict__) # {'manufacturer': 'Honda', 'model_name': 'Civic'}

class_state = car.__dict__.copy()
del car
new_car_obj = from_dict(class_state)
print(new_car_obj) # <Toyota Corolla>

print("==========================================================================================")

# MUTABLE CLASS OBJECTS
class List:
    lst = [1,]

t1 = List()
t2 = List()

print(t1.lst, t2.lst) # [1] [1]
t1.lst.append(2)
print(t1.lst, t2.lst) # [1, 2] [1, 2]

print("==========================================================================================")

# SETTER and GETTER functions

class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature()) # 37

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit()) # 98.60000000000001

# # new constraint implementation
# human.set_temperature(-300) # ValueError: Temperature below -273.15 is not possible.
#
# # Get the to_fahreheit method
# print(human.to_fahrenheit())

