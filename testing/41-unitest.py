# unittest - Python's library for writing tests
# TestCase - A collection of tests

# Running tests In Command line
python -m unittest tests.py

# Running tests In a script
 unittest.main()

# Remember, all tests in a TestCase have to start with the word test_ to be run. 
# You can have methods that don't start with test_ for other purposes if you need them.


#exercise 
#Import the unittest module
import unittest

#Create a TestCase named SimpleTestCase with a simple test that asserts that 10 - 10 is 0. 
#Remember, unittest test names have to start with test_.
class SimpleTestCase(unittest.TestCase):    #extend unittest.TestCase
    def test_simple(self):
        assert 10 - 10 == 0

#tests.py
import unittest
import moves

class Movetests(unittest.TestCase):
    def test_five_plus_five(self):
        assert 5 + 5 == 10
        
    def test_one_plus_one(self):
        assert not 1 + 1 == 3
        
if __name__ == '__main__':
    unitest.main()
        
        
#moves.py
        
class Move:
    better_than = None
    worse_than = None

    def __gt__(self, other):
        """Is this instance being compared to an instance from a worse class"""
        return other.__class__.__name__ in self.better_than

    def __lt__(self, other):
        """Is this instance being compared to an instance from a better class"""
        return other.__class__.__name__ in self.worse_than

    def __eq__(self, other):
        """Is this instance being compared to an instance from the same class"""
        return type(other) == type(self)

    def __ne__(self, other):
        """Is this instance being compared to an instance from another class"""
        return other.__class__ != self.__class__


class Rock(Move):
    better_than = ['Scissors']
    worse_than = ['Paper']


class Paper(Move):
    better_than = ['Rock']
    worse_than = ['Scissors']


class Scissors(Move):
    better_than = ['Paper']
    worse_than = ['Rock']
