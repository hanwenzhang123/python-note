#quantitative assertions
setUp() - Method that is run before each test. Use this to set up state for the tests
assertEqual(x, y) - Make sure x and y are equal
assertNotEqual(x, y) - Make sure x and y are not equal
assertGreater(x, y) - Make sure x is greater than y
assertLess(x, y) - Make sure x is less than y

The assert statement exists in almost every programming language. 
assert - What keyword do we use to say a statement has to be true?
It helps detect problems early in your program, where the cause is clear, rather than later when some other operation fails.

#assertTrue and assertFalse
# assertTrue checks that a value is truthy. 
# Complete the first test using assertTrue to test the is_palindrome function. 
# Fill out test_bad_palindrome with the assertFalse assertion, is_palindrome, and a bad palindrome.

import unittest
from string_fun import is_palindrome

class PalindromeTestCase(unittest.TestCase):
    def test_good_palindrome(self):
        # assertTrue will check if the passed parameter returns True
        # In order to make it true, we have to pass a string that is a palindrome
        self.assertTrue(is_palindrome("tacocat"));

    def test_bad_palindrome(self):
        # assertFalse will check if the passed parameter returns False
        # In order to make it true, we have to pass a string that is not a palindrome
        self.assertFalse(is_palindrome("notpalindrome"));
            
            
# self.assertGreater(age, 12) - I want to make sure than age is always higher than 12. What assertion would I use?


#tests.py
import unittest
import moves

class Movetests(unittest.TestCase):
    def setup(self):
        self.rock = moves.Rock()
        self.paper = move.Paper()
        self.scissors = moves.Scissors()
        
    def test_five_plus_five(self):
        assert 5 + 5 == 10
        
    def test_one_plus_one(self):
        assert not 1 + 1 == 3
        
    def test_equal(self):
        self.assertEqual(self.rock, moves.Rock())
        
    def test_not_equal(self):
        rock = moves.Rock()
        paper = moves.Paper()
        self.assertNotEqual(self.rock, self.paper)
        
    def test_rock_better_than_scissors(self):
        self.assertGreater(self.rock, self.scissors)
        
    def test_paper_worse_than_scissors(self):
        self.assertLess(self.paper, self.scissors)
        
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
