#Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques


print(unique_english_letters("mississippi")) #4

print(unique_english_letters("Apple")) #4



#Count X
def count_char_x(word, x):
  occurrences = 0
  for letter in word:
    if letter == x:
      occurrences += 1
  return occurrences


print(count_char_x("mississippi", "s")) #4

print(count_char_x("mississippi", "m")) #1



#Count Multi X
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

print(count_multi_char_x("mississippi", "iss")) #2

print(count_multi_char_x("apple", "pp")) #1



#Substring Between
#This function should return the substring between the first occurrence of start and end in word. 
#If start or end are not in word, the function should return word.
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
  	return(word[start_ind+1:end_ind])
  return word

print(substring_between_letters("apple", "p", "e")) #pl

print(substring_between_letters("apple", "p", "c")) #apple

# slicing is [inclusive:exclusive]



# X Length
#This function should return True if every word in sentence has a length greater than or equal to x
def x_length_words(sentence, x):
  words = sentence.split(" ")
  for word in words:
    if len(word) < x:
      return False
  return True

print(x_length_words("i like apples", 2)) #False
print(x_length_words("he likes apples", 2)) #True



#Check Name

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie")) # True
print(check_for_name("My name is jamie", "Jamie")) # True
print(check_for_name("My name is Samantha", "Jamie")) # False



#Every Other Letter
#The function should return a string containing every other letter in word.
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

print(every_other_letter("Codecademy")) # should print Cdcdm
print(every_other_letter("Hello world!")) # should print Hlowrd
print(every_other_letter("")) # 


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



#Make Spoonerism
#Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”.
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

print(make_spoonerism("Codecademy", "Learn")) # should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!")) # should print wello Horld!
print(make_spoonerism("a", "b")) # should print b a
