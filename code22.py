class Employee:
    public=12
    _protect=23
    __private=34
class Student(Employee):
    pass   
emp=Employee()
print(emp.public)    
print(emp._protect)
print(emp._Employee__private)
#this happens due to python mangling