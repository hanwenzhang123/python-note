# Define a class using the class keyword.
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)

print(facade_1_type); #<class '__main__.Facade'>


#Class Variables
#1
class Musician:
  title = "Rockstar"
 
drummer = Musician()
print(drummer.title);   # prints "Rockstar"

#2
class Grade:
  minimum_passing = 65
 
