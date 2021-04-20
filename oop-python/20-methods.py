# in object oriented python, a function inside of a class is called a method
# here we add methods to a class, pass in arguments and call a method
# all methods inside of a class will need to take self as argument, otherwise it will throw an error
# A method needs self, like def leaderboard(self)

class Car: 
  wheels = 4    # it is class attribute here
  doors = 2
  engine = True

def __init__(self, model, year, make='ford'):  #dunder init takes self
  self.make = make      # make and model are both instance attributes
  self.model = model
  self.year = year
  self.gas = 100
  self.is_moving = False # it does not need to pass in a value always

def stop(self): #take the self as an argument, stop is a method here
  if self.is_moving:
     print('the car has stopped')
     self.is_moving = False
  else:
    print('the car has already stopped')
  
def go(self, speed):
  if self.use_gas():
    if not self.is_moving:
      print('The car starts moving')
      self.is_moving = True
    print(f'The car is going {speed}')
  else:
    print('you have run out of gas')
    self.stop()
  
def use_gas(self):
  self.gas -= 50
  if self.gas <= 0: 
    return False
  else:
    return True
  
car_one = car('model T', 1908)
car_one.stop() # do not need to pass anything although we have self as argument
car_one.go('slow') # here we need argument for speed
car_one.go('fast')
car_one.stop()
car_one.stop()
#car_one is an instance of our Car class

#exercise
class Panda:
    species = 'Ailuropoda melanoleuca'
    food = 'bamboo'

    def __init__(self, name, age):
        self.is_hungry = True #default value
        self.name = name
        self.age = age

    def eat(self):
        self.is_hungry = False
        return f'{self.name} eats {self.food}.'
    
    def check_if_hungry(self):
        if self.is_hungry:
            self.eat()

panda_one = Panda('Bao Bao', 10)
panda_one.eat()


#in order to call the stop method inside of another method, you'd need to write 
self.stop() # to run it in another method within the class
car_one.stop() # to run it on/for/with the car_one instance
