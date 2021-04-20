# sequences - an ordered group of things
# iterate - looping over sequences
# all python sequences are iterable, they can all be loop over

# For In Loop - for each element in a sequence do this action

# letter is variable and my_name is sequence, we can access each sequence individually
# for letter in my_name
# my_name = 'Hanwen'


groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']
for item in groceries:
  print(item)
#in the console, each element in the grocery list printed on its own line


# f-string helps us print variables inside of strings
groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']
index = 1
for item in groceries:
  print(f'{index}. {item}')
  index += 1


# enumerate()
groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

for index, item in enumerate(groceries, 1): # enumerate to start counting 1 but 0
  print(f'{index}. {item}')
  
  
# exercise
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for index, color in enumerate(rainbow, 0):
  print(f'{index}. {color}')
  
  
  
# range [ start, stop, step ]
# start default value is 0
# stop is the ending index
# step represents the index increase, default is 1
# i represents the index of the current element in the loop

for i in range(0, 10, 1):   #range(10) is good here because the default value
  print(i) 

# print 0 to 9 but not 10, still run 10 times including 10
  
  
  #exercise
my_list = []
for val in range(10):
    my_list.append(val)
    
    
  
  #len(length)/min(smallest)/max(biggest)

my_string = 'treehouse2019'
len(my_string) #13 - number of the letters
max(my_string) #u - closest to the end of the alphabet
min(my_string) #0 - if you have number here, number is smaller

  

    
    
#slice - won't change the initial value
#slice[ start, stop, step ]
#seq[<start>:<stop>:<step>]
#seq[1:4] - begin at the second element and end by the fifth one. (1 2 3 index)

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
rainbow[1] 
'organge'
rainbow[1:4] # 1 is start 4 is ending
['orange', 'yellow', 'green']
rainbow[3:] # leave the stop value empty after the colon
['green', 'blue', 'indigo', 'violet']
rainbow[:3] # stop up to the third value, not including the fourth
['red', 'orange', 'yellow']
rainbow[::2] # step value, skip every other value here
['red', 'yellow', 'blue', 'violet']
rainbow[::-1] # reverse value



#slicing

letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[1:6]
print(sliced_list)  #["b", "c", "d", "e", "f"]



fruits = ["apple", "cherry", "pineapple", "orange", "mango"]

fruits[:n]. - If we want to select the first n elements of a list, we could use the following code
print(fruits[:3])   #['apple', 'cherry', 'pineapple']
fruits[-n:] - we want to slice the last n elements in a list
print(fruits[-2:]) # ['orange', 'mango']

fruits[:-n] - Negative indices can also accomplish taking all but n last elements of a list.
print(fruits[:-1])  #['apple', 'cherry', 'pineapple', 'orange']



suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Checkpoint 1
last_two_elements = suitcase[-2:]
print(last_two_elements)

# Checkpoint 2
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

