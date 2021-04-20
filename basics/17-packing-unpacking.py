# **kwargs will pack variable arguments into a dictionary, not a tuple! 
# Packing positional arguments into a tuple is denoted by *args.

#packing with dictionaries
  def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)
print_teacher(name='Ashley', job='Instructor', topic='Python') # the name here has to match the parameter names
  
  
#kwargs - stands for keywordd arguments, we will replace the individual parameters with a single parameter kwargs
def print_teacher(**kwargs): 
  for key, value in kwargs.items():
    print(f'{key}: {value}') #f-string formatting here
print_teacher(name='Ashley', job='Instructor', topic='Python', second_topic = 'javascript')
    
  # by converting our functions definition to use packing,
    # any amount of variable or keyword arguments can be passes to be function
    # I can send or not send arguments as needed, allows more flexibility
  # differ from when we pack positional arguments into a tuple which is *args
  
  
#   The items() method returns a view object. 
#   The view object contains the key-value pairs of the dictionary, as tuples in a list.
  
  car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964 }
x = car.items()
print(x)

# dict_items([('brand', 'Ford'), ('model', 'Mustang')])
  
  
  
# Unpacking with dictionaries
# Unpacking dictionaries is the opposite of packing them. 
# It can be used if you have an existing dictionary that you would like to send to a function.


teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)
    
# To pass the data from the teacher dictionary to this function, we can use unpacking
  
  print_teacher(**teacher)
  
#   This ** unpacks all the key:value pairs in the teacher dictionary into three keyword arguments, 
#     which are then accepted by the function into the three corresponding parameters.

