# for string
seq_string = 'Python'
print(list(reversed(seq_string)))

# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))

# for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))

# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))
Output

['n', 'o', 'h', 't', 'y', 'P']
['n', 'o', 'h', 't', 'y', 'P']
[8, 7, 6, 5]
[5, 3, 4, 2, 1]
In our example, we have converted the iterators returned by reversed() to list using the list() function.



#Reverse
#The function should return word in reverse.
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

print(reverse_string("Codecademy")) # should print ymedacedoC
print(reverse_string("Hello world!")) # should print !dlrow olleH
print(reverse_string(""))# 
