
#  Write a Python program that prints long text, converts it to a list, and prints all the words and the frequency of each word.

from collections import Counter
import re

def word_frequency(text):
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    word_count = Counter(words)
    return word_count

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
word_count = word_frequency(text)
print(word_count)
