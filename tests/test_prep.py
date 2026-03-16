import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    def test_strange_function1(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
        )

    # TODO: Can you write more test cases below to increase the test coverage of `strange_function`?
    def test_strange_function2(self):
        # a == b and c < d
        self.assertEqual(
            first=strange_function(1, 1, 3, 4),
            second="behaviour 1"
    )
        
    def test_strange_function3(self):
        # a == b and c >= d
        self.assertEqual(
            first=strange_function(1, 1, 4, 3),
            second="behaviour 2"
    )
    
    def test_strange_function4(self):
        # a < c
        self.assertEqual(
            first=strange_function(1, 5, 3, 4),
            second="behaviour 3"
    )
        
    def test_strange_function5(self):
        # a != b and a >= c and d < b
        self.assertEqual(
            first=strange_function(5, 7, 3, 4),
            second="behaviour 4"
    )
        
    def test_strange_function6(self):
        # a != b and a >= c and d >= b and c < a
        self.assertEqual(
            first=strange_function(5, 7, 3, 10),
            second="behaviour 5"
    )
        
    def test_strange_function7(self):
        # a != b and a >= c and d >= b and c >= a
        self.assertEqual(
            first=strange_function(5, 7, 5, 10),
            second="behaviour 6"
    )
        
    
        
    