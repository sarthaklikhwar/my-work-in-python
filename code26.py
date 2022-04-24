class Employee:

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):  # always write self in ()
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def __add__(self, other):
        return self.salary+other.salary  # we have created an addtion  method

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"EMPLOYEE ({self.name},{self.salary},{self.role})"

    def __str__(self): # gets prefered over __repr__ method.
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 800, "Instructor")
rohan = Employee("Rohan", 200, "Student")
#karan = Employee.from_dash("Karan-480-Student")

# Employee.printgood("Sarthak")
print(harry.printdetails())
# print(harry.name+rohan.name)
print(harry+rohan)
print(harry/rohan)
print(harry)
print(repr(rohan))
print(str(rohan))
