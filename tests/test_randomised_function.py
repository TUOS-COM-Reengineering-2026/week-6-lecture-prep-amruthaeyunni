import unittest
from lecture import randomised_function
from unittest.mock import patch

class MyTestCase(unittest.TestCase):

    """
    def test_randomised_function(self):
        self.assertEqual('software', randomised_function())  # This will pass or fail randomly
        # TODO: Can we make this test deterministic? (HINT: Mock testing)
    """

    @patch('lecture.is_small')
    def test_randomised_function_with_mock1(self, mock_is_small):
        mock_is_small.return_value = True
        self.assertEqual('software', randomised_function())
    
    @patch('lecture.is_small')
    def test_randomised_function_with_mock2(self, mock_is_small):
        mock_is_small.return_value = False
        self.assertEqual('engineering', randomised_function())