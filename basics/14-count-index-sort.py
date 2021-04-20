#Code Samples: Membership Testing, Count, and Index

List & Tuples
Membership Testing

fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']
vegetables = ('asparagus', 'corn', 'broccoli', 'eggplant', 'onion')

'eggplant' in fruits # False
'eggplant' not in fruits # True

'eggplant' in vegetables # True
'eggplant' not in vegetables # False


#Index - where it is, it could be the location in a paragraph, only return the very first time one
my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')

my_pets.index('dog') # 0
my_pets.index('chicken') # 3
my_pets.index('lizard') # ValueError: 'lizard' is not in list


Count - how many times the value exist , case sensitive
my_pets = ['dog', 'cat', 'cat', 'chicken', 'dog']

my_pets.count('cat') # 2
my_pets.count('lizard') # 0


#Index
nums = range(1, 10, 2)

nums.index(5) # 2
nums.index(10) # ValueError: 10 is not in list
nums.index(1) # 0




#Range
Membership Testing
nums = range(10)

0 in nums # True
10 in nums # False
4 in nums # True

0 not in nums # False
15 not in nums # True
10 not in nums # True

nums = range(1, 10, 2)

0 in nums # False
6 in nums # False

4 not in nums # True
8 not in nums # True



my_range = range(10)  #range(0, 10)
print(list(my_range))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 7]


my_list = range(2, 9)
print(list(my_list))

# [2, 3, 4, 5, 6, 7, 8]

my_range2 = range(2, 9, 2)
print(list(my_range2))

# [2, 4, 6, 8]

my_range3 = range(1, 100, 10)
print(list(my_range3))

#[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]


range_five_three = range(5, 15, 3)
print(list(range_five_three))

range_diff_five = range(0,40,5)
print(list(range_diff_five))

# [5, 8, 11, 14]
# [0, 5, 10, 15, 20, 25, 30, 35]




#sort() - We can sort a list using the method .sort() either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names) # ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
names.sort(reverse=True)
print(names) #['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']



# sorted()
# It comes before a list, instead of after as all built-in functions do.
# It generates a new list rather than modifying the one that already exists.

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names)
print(sorted_names) #['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
print(names) #['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
