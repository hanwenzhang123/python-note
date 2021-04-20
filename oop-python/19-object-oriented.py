OOP = Object-Oriented Programming
eveything in python is an object, class allows us grow our own custom object, repeatable and organied
Object-Oriented Programming = a way of structuring your code into groups of properties and behaviors

# classes are like a factory, they hold all the information about an object like a blueprint
# when you use your class to create an object is called instantiation
# the object you created itself is called an instance
# you create a blueprint for your object using the class keyword, the name of your class and the colon.

# class is a blue print for individual objects with exact behaviour.


class PlayerCharacter:
  membership = True # class object attribute, it doesn't change across the instance, it is not dynamic here
  
  def __init__(self, name, age):  #constructor method, init method, always first self, init gives you control
    if(self.membership): # self here refers to the class, or we can use PlayerCharacter.membership because it is class attribute
      self.name = name    #self refers to the playercharacter, change when we give the value to it, self.name = parameter
      self.age = age    #name and age here are attribute, they are data that is dynamic and unique, need self keyword
    
  def shout(self):  #create method here and use self
    print(f'my name is {self.name}') #without the self, name is not defined. 
    
  def run(self, hello):  #use self as parameter first before the second one
    print(f'my name is {self.name}')  # have to use self to get the data from the attribute
    
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50
    
print(player1.run('hello'))   # we have to pass an argument because we have a second parameter hello
print(player2.shout())





# car.py

class Car:    #with or without the () and Car() is an instance of class Car.
pass     #pass keep moving without error
#you can use print(), type(), isinstance() to see if you correctly made an object

class Car: 
wheels = 4
doors = 2
engine = True
# the initializer is a funtion or method that is called in a Python class, when an object is created from the class and it allow the class to initialize the attributes of a class.
def __init__(self, model, year, make='ford'):  #dunder method structures each instance
  self.make = make        # this argument called self, self is a reference to the instance, we can access attribute and methods
  self.model = model
  self.year = year

car_one = Car('model t', 1908) #ford is a default value for make
car_two = Car('phantom', 2020, 'rolls royce')

print(car_one.make) 
print(car_two.make) 
# only be able to access with an instance, not class



#exercise
class Panda:  #Inside class, create two class attributes
    species = 'Ailuropoda melanoleuca'
    food = 'bamboo' 

    def __init__(self):  #take the self argument
        self.is_hungry = True   #create an instance attribute called is_hungry and set it equal to True

        
