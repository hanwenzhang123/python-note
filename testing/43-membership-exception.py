#Membership and Other Assertions
assertIn(x, y) - Make sure x is a member of y (this is like the in keyword)
assertIsInstance(x, y) - Make sure x is an instance of the y class
assertGreaterEqual(x, y) - Make sure x is greater than or equal to y
assertLessEqual(x, y) - Make sure x is less than or equal to y


#assertIn exercise

#The get_anagrams() function takes one or more words and returns anagrams for each of them as a list. 
#Finish the test_in_anagrams() test to check that the anagrams for the string "treehouse" contains the word "house".

#Conversely, we shouldn't see the word "code" in the list of anagrams for "treehouse". 
#Add a new test named test_not_in_anagrams and use self.assertNotIn() to make sure "code" isn't in the anagrams for "treehouse".

import unittest

from string_fun import get_anagrams

class AnagramTests(unittest.TestCase):
    def test_in_anagrams(self):
        self.assertIn("house", get_anagrams("treehouse"))
        
class test_not_in_anagrams(unittest.TestCase):
    def test_in_anagrams(self):
        self.assertNotIn("code", get_anagrams("treehouse"))

     

#test.py

import unittest
import dice

class DieTests(unittest.TestCase):
    def setUp(self):
        self.d6 = dice.Die(6)
        self.d8 = dice.Die(8)
        
    def test_creation(self):
        self.assertEqual(self.d6.sides, 6)
        self.assertIn(self.d6.value, range(1, 6))
        
    def test_add(self):
        self.assertIsInstance(self.d6+self.d8, int)
        


class RollTests(unittest.TestCase):
    def setUp(self):
        self.hand1 = dice.Roll('1d2')
        self.hand3 = dice.Roll('3d6')

    def test_lower(self):
        self.assertGreaterEqual(int(self.hand3), 3)
        
    def test_upper(self):
        self.assertLessEqual(int(self.hand3), 18)
        
    def test_membership(self):
        test_die = dice.Die(2)
        test_die.value = self.hand1.results[0].value
        self.assertIn(test_die, self.hand1.results)
        
            
if __name__ == '__main__':
    unittest.main()
    
    
    
    

#dice.py
import random
import re

die_pattern = re.compile(r'^(?P<num>\d+)d(?P<sides>\d+)$', re.I)


class Die:
    value = None

    def __init__(self, sides=6):
        try:
            assert sides >= 2
        except AssertionError:
            raise ValueError("Die needs at least 2 sides")
        else:
            self.sides = sides
        self.value = self.roll()

    def roll(self):
        return random.randint(1, self.sides)

    def __int__(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __eq__(self, other):
        return all([
            self.sides == other.sides,
            self.value == other.value
        ])
