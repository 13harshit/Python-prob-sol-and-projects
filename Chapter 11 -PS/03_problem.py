# Defining a class with class variables and a property method
class Employee:
    salary = 50000  # Class variable
    increment = 10  # Class variable
    
    # Using property decorator to define a method as a property
    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * (self.increment / 100)))

    # Setter for the property
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = value

# Creating an instance of Employee and accessing the property
e = Employee()
print(e.salaryAfterIncrement)

# Using setter to change increment
e.salaryAfterIncrement = 20
print(e.salaryAfterIncrement)

