class Employee:
    no_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        # following line will update the variable for the object, not for the class
        # self.no_of_employees += 1
        Employee.no_of_employees += 1

        # regular method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

        # regular method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    # can't use class for first argument since class is a keyword
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        #super().__init__(first, last, pay) -OR-
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        #super().__init__(first, last, pay) -OR-
        Employee.__init__(self, first, last, pay)
        if employees == None:
            self.employees = []
        self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee  in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print("-->", employee.fullname())

emp_1 = Employee("Ajay", "Videkar", 50000)
emp_2 = Employee("Sameer", "Videkar", 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(Employee.fullname(emp_2))

print(emp_1.pay)
emp_1.raise_amount = 1.10
emp_1.apply_raise()
print(emp_1.pay)

# following will udpate raise_amount for all the objects
# Employee.raise_amount = 1.20
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

print(emp_1.__dict__)
print(emp_2.__dict__)

print("No. of employess : " + str(Employee.no_of_employees))

Employee.set_raise_amount(1.08)
# -OR-
# Employee.raise_amount = 1.08
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.pay)
print(new_emp_2.pay)
print(new_emp_3.pay)

print("No. of employess : " + str(Employee.no_of_employees))

import datetime
my_date = datetime.date(2016, 7, 10) # Sunday
print(Employee.is_workday(my_date))
my_date = datetime.date(2016, 7, 11) # Monday
print(Employee.is_workday(my_date))

dev_1 = Developer("Kaushik", "Srivatsan", 10000, 'Python')
dev_2 = Developer("Sourabh", "Dravid", 20000, 'Java')
print(help(Developer))
print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.email)
print(dev_2.prog_lang)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager("Bala", "Srivatsan", "111000", [dev_2])
print(mgr_1.email)
mgr_1.add_employee(dev_1)
mgr_1.print_employees()
mgr_1.remove_employee(dev_2)
mgr_1.print_employees()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Manager))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))