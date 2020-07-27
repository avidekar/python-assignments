# A decorator is a special kind of function that either takes a function and returns a function,
# or takes a class and returns a class. The @ symbol is just syntactic sugar that allows you to
# decorate something in a way that's easy to read.

# The decorator pattern is an object orientated design pattern that allows behaviour to be added
# to an existing object dynamically. When you decorate an object then you extend its functionality
# in a way that is independent of other instances of the same class. Python decorators are not an
# implementation of the decorator pattern. Python decorators add functionality to functions and
# methods at definition time, they are not used to add functionality at run time. The decorator
# pattern itself can be implemented in Python, but it'a a pretty trivial thing because of the
# fact that Python is duck-typed.

# Basic Decorator

def time_this(original_function):
    print("inside time_this")
    def new_function(*args, **kwargs):
        print("inside new_function")
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time : {0}".format(after - before))
        print("end new_function")
        return x
    print("outside time_this")

    return new_function

@time_this
def func_a(stuff):
    print("inside func_a")
    import time
    print("before time.sleep")
    time.sleep(3)
    print("after time.sleep")

func_a(1)

print("============================================================================================")

# This decorator exists so you can create class methods that are passed the actual class object
# within the function call, much like self is passed to any other ordinary instance method in
# a class.
#
# In those instance methods, the self argument is the class instance object itself, which can
# then be used to act on instance data. @classmethod methods also have a mandatory first argument,
# but this argument isn't a class instance, it's actually the uninstantiated class itself.
# So, while a typical class method might look like this:
# BENEFIT - No need to instantiate class object
# A class method is a method which is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter that points to the
# class and not the object instance.
# It can modify a class state that would apply across all the instances of the class. For example,
# it can modify a class variable that would be applicable to all the instances.

class Employee(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(" "))
        student = cls(first_name, last_name)
        return student

    @classmethod
    def from_json(cls, json_obj):
        # parse json and create Student object
        return True

    @classmethod
    def from_pickle(cls, pickle_file):
        # load pickle file
        return False

scott = Student('Scott', 'Robinson')
#print(scott)
scott_1 = Student.from_string('Scott Robinson')
print(scott_1)
# employee = Employee.from_string('Ajay Videkar') # will throw error -
# AttributeError: type object 'Employee' has no attribute 'from_string'

print("============================================================================================")

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18

person_1 = Person('Ajay', 29)
person_2 = Person.from_birth_year('Ajay', 1990)
person_3 = Person.from_birth_year('Ananya', 2016)
print(person_1.age)
print(person_2.age)

print(person_2.is_adult(person_2.age))
print(person_3.is_adult(person_3.age))
print(Person.is_adult(25))
# print(emp1.is_adult(emp1.age))

print("============================================================================================")

# The @staticmethod Decorator
# The @staticmethod decorator is similar to @classmethod in that it can be called from an
# uninstantiated class object, although in this case there is no cls parameter passed to its
# method. Since no self object is passed either, that means we also don't have access to any
# instance data, and thus this method can not be called on an instantiated object either.
#
# These types of methods aren't typically meant to create/instantiate objects, but they may
# contain some type of logic pertaining to the class itself, like a helper or utility method.

# @classmethod vs @staticmethod
# The most obvious thing between these decorators is their ability to create static methods
# within a class. These types of methods can be called on uninstantiated class objects, much
# like classes using the static keyword in Java.
#
# There is really only one difference between these two method decorators, but it's a major one.
# You probably noticed in the sections above that @classmethod methods have a cls parameter
# sent to their methods, while @staticmethod methods do not.
#
# This cls parameter is the class object we talked about, which allows @classmethod methods
# to easily instantiate the class, regardless of any inheritance going on. The lack of this
# cls parameter in @staticmethod methods make them true static methods in the traditional sense.
# They're main purpose is to contain logic pertaining to the class, but that logic should not
# have any need for specific class instance data.