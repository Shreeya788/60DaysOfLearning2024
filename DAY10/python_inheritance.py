'''
Inheritance is a mechanism in which one class acquires all the properties and behaviors of another class.
Parent class --> class being inherited from  (base class)
child class --> class that inherits from another class (derived class)
'''

#Creating parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Creating child class
class Student(Person):
  pass

#Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Chan")
x.printname()