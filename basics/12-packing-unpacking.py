# packing - (*args) as parameter 
# Packing positional arguments into a tuple is denoted by *args.

def packer(arg1, arg2, arg3, arg4):
  print(arg1)
  print(arg2)
  print(arg3)
  print(arg4)

parker("hi", "i", "love", "python")

# #console
# hi
# i
# love
# python


def packer(*args):
  for val in args:
  print(val)  

parker("hi", "i", "love", "python")

# #console
# hi
# i
# love
# python


def packer(*args):
  print(args)  

parker("hi", "i", "love", "python")

# #console
# ("hi", "i", "love", "python")



def calculate_total(*args):   #unlimited item numbers
  total = sum(args)
  print(total)
  
  calculate_total(25, 25, 20, 30) # $100
  # you can send whatever numerial data in the function
  
  
  
  
  
  
  

  # unpacking

def unpacker():
  return(1, 2, 3)

var1, var2, var3 = unpacker()

print(var1) #1
print(var2) #2
print(var3) #3



def unpacker():
  return 'hey'

var1, var2, var3 = unpacker()

print(var1) #h
print(var2) #e
print(var3) #y



full_name = input('Enter your full name: \n').split(' ')
# \n - need a new line, keep things neat here
# the input will be saved as string value, then we use split() to split the string

print(full_name)

#['Hanwen', 'Zhang']



first, last = input('Enter your full name: \n').split(' ')

print(first)
print(last)

# Hanwen
# Zhang
