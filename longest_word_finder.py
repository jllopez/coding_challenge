import os.path


class LongestWordFinder:
    """A class to keep track of the longest word in a file"""

    def __init__(self):
        """Initializes the class. 

        By default the longest word values
        are initialized to an empty string 
        """
        self.longest_word = ''
        self.longest_word_transposed = ''

    def find_longest_word(self, str_of_words):
        """Finds the longest word in a string"""
        if str_of_words:
            words = str_of_words.split()
            max_word_len = len(max(words, key=len))
            for word in words:
                if len(word) == max_word_len:
                    self.longest_word = word
                    self.longest_word_transposed = self.longest_word[::-1]
