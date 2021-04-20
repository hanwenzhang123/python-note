# while loop (condition-based)
# the while loop will not run unless the expression is True
import sys

MASTER_PASSWORD = 'opensesame'
password = input("please entetr the super secret password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
  if attempt count > 3:
      sys.exit("too many invalid password attempts")
  password = input ('Invalid password, try again: ')
  attempt_count += 1
print('welcome to secret town')


# for loop
# run each set of the left-side for value, the right-side in must be literable

banner = "Happy Birthday!"
for letter in banner:
...    print(letter.upper())
# H
# A
# P
# P
# Y
#
# B
# I
# R
# T
# H
# D
# A
# Y
# !


for letter in "You got this!":
    if letter in "oh":
        print(letter)
# O
# O
# H


#workshop

name = input('what's your name?')
understanding = input('{}, do you understand Python while loops?\n(Enter yes/no)'.format(name))

while understanding.lower() != 'yes':
      print('OK, {}, while loops in python repeat as long as a certain boolean condition met.'.format(name))
      understanding = input('{}, now do you understand Python while loops?\n(Enter yes/no)'.format(name))
             
print('that is great, {}.'.format(name))
