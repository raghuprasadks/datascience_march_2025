#class
#class is a blueprint for creating objects
"""
class Student:
    pass

#object
#object is an instance of a class

#contructor is a special method in Python classes
#it is called a constructor
#it is called when an object is created

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


obj1=student("John", 23)
obj1.display()

obj2=student("Jane", 22)
obj2.display()


#class without constructor

class Hello:
    def display(self):
        print("Hello")

obj3=Hello()
obj3.display()
"""

# calculater with out constructor using oops

class Calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        print("substraction :",a-b)
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b
calc1=Calculator()
result=calc1.add(10, 20)
print("Addition: ", result)
calc1.sub(10, 20)







