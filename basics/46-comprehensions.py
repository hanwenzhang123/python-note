Comprehensions let you skip the for loop and start creating lists, dicts, and sets straight from your iterables. 
Comprehensions also let you emulate functional programming aspects like map() and filter() in a more accessible way. 


number range (5, 101)   # we have numbers 5 to 100 

#loop
halves = []
for num in nums:
  halves.append(num/2)
  
#comprehension
halves = [num/2 for num in nums]  # result returns same as the loop


#examples
print([num for nums in range(1, 101) if num % 3 == 0])

rows = range(4)
cols = range(10)
[(x, y) for y in rows for x in cols]

[(letter, number) for number in range (1, 5) for letter in 'abc']


#zip takes two or more iterables and gives back one item from each iterable at the same index position
#we can loop through that zip to get these two items or three items or four items, however iterables put in to it at a time
{number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))} # {1: 'a',  2: 'b' ~~~~}

{student: point for student, points in zip(['Kenneth', 'Dave', 'Joy'], [123, 456, 789])} # {'Kenneth':  123, ~~~~~}


#fizzbuzz game
total_nums = range(1, 101)
fizzbuzzes = {
  'fizz': [n for n in total nums if n % 3 == 0],
  'buzz': [n for n in total nums if n % 7 == 0]
}
fizzbuzzes = {key: set(values) for key, value in fizzbuzzes.item()}   #we come out sets {}
fizzbuzzes['fizzbuzz'] = {n for n in fizzbuzzes['fizz'].intersection(fizzbuzzes['buzz'])}
fizzbuzzes['fizzbuzz']  #{42, 84, 21, 63}
  
{round(x/y) for y in range (1, 11) for x in range (2, 21)} #set - output is unique  
[ound(x/y) for y in range (1, 11) for x in range (2, 21)] #list - more number/repeat, much more bigger than set


  
