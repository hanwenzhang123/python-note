# For an int and an int, + returns an int
2 + 4 == 6
 
# For a float and a float, + returns a float
3.1 + 2.1 == 5.2
 
# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"
 
# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]



Polymorphism is the term used to describe the same syntax (like the + operator here, but it could be a method name) doing different actions depending on the type of data.

Polymorphism is an abstract concept that covers a lot of ground, but defining class hierarchies that all implement the same interface is a way of introducing polymorphism to our code.



a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

len(a_list)
len(a_dict)
len(a_string)
