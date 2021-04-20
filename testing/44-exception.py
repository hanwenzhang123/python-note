#exception
assertRaises(x) - Make sure the following code raises the x exception
You can use @unittest.expectedFailure on tests that you know will fail
with self.assertRaises(ValueError):    #with - a context managser, use with we are able to control the context, change the variable here


#exercise

#Our get_anagrams() function raises a ValueError when you pass it an empty string. 
#Finish the test to make sure this happens. You'll want to use assertRaises.
#Now add a new test, test_no_args that should also assertRaises(ValueError). 
#This time, call get_anagrams() with no arguments.

import unittest

from string_fun import get_anagrams


class AnagramTestCase(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            get_anagrams('')
            
    def test_no_args(self):
        with self.assertRaises(ValueError):
            get_anagrams()
        
        
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
        
    def test_bad_sides(self):
        with self.assertRaises(ValueError):
            dice.Die(1)


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
        
    def test_bad_description(self):     #exception get raised
        with self.assertRaises(ValueError):    #with - a context managser, use with we are able to control the context, change the variable here
            dice.Roll('2b6')        #this is a wrong dice but passes here because it is exception here
            
    def test_small_die(self):
        with self.assertRaises(ValueError):
            dice.Roll('1b2')        #it failed, because this dice works
            
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
        return random.randint(1, self.sides)    #randrange(start, stop+1) - returns an integer number selected element from the specified range.

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
