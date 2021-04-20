how to check if you have test everything in your code
`coverage.py` is an amazing library for determining how much of your code is covered by your tests and how much still needs to be tested.
-m - What flag makes coverage report show the lines that aren't yet covered by tests?


#Installing coverage.py
pip install coverage

#Using coverage.py
#Make sure you test file can be run from the command line without the -m unittest argument.

coverage run tests.py

#Generate a report
#coverage report or coverage report -m if you want the missed lines.

coverage report
coverage report -m    # m means missing


#html report
#coverage html will generate the HTML report. By default, it'll live in the htmlcov/ directory.
#To serve HTML files (and CSS, JS, etc) directly from Python, we used the http.server module through python -m http.server.
   

>>> coverage html
>>> python -m http.server
#Serving HTTP on 0.0.0.0 port 8000 ... then go to preview port 8000
#then go to htmlcov
#click the module like dice, then you can see the lines that are not covered



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
            dice.Roll('1b2')        #it will fail, because this dice works
    
    def test_adding(self):
        self.assertEqual(self.hand1+self.hand3,
                         sum(self.hand1.results)+sum((self.hand3.results))
    
    
if __name__ == '__main__':
    unittest.main()
    
