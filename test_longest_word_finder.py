import os.path
import unittest
import xmlrunner
from ddt import ddt, file_data
from longest_word_finder import LongestWordFinder


@ddt
class TestLongestWordFinder(unittest.TestCase):
    """Test Class to verify the correct behaviour of LongestWordFinder class"""

    def test_initialize_class_with_args(self):
        """Test init class with args"""
        with self.assertRaises(TypeError):
            LongestWordFinder('random', 'args')

    def test_initialize_class_no_args(self):
        """Test init class with no args"""
        lwf = LongestWordFinder()
        self.assertEqual(lwf.longest_word, '')
        self.assertEqual(lwf.longest_word_transposed, '')

    def test_input_file_exist(self):
        """Test if file exist"""
        self.assertTrue(os.path.exists('input_file.json'))

    @file_data('input_file.json')
    def test_find_longest_and_transposed_word(self, given_input,
                                              expected_output,
                                              expected_output_transposed):
        """Test to find the longest word in a string"""
        lwf = LongestWordFinder()
        lwf.find_longest_word(given_input)
        self.assertEqual(lwf.longest_word, expected_output)
        self.assertEqual(lwf.longest_word_transposed,
                         expected_output_transposed)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./test_results'))
