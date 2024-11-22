"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""

import string
import random

def generate_words(n=10):
    """Generate a list of random words of length between 3 to 10 characters."""
    words = []
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)
    return words

def write_files(file1_path: str, file2_path: str, words=None):
    """Write words to two files with specified encodings and separators."""
    if words is None:
        words = generate_words()

    with open(file1_path, 'w', encoding='utf-8') as file1:
        file1.write('\n'.join(words))

    with open(file2_path, 'w', encoding='cp1252') as file2:
        file2.write('|'.join(reversed(words)))

    print("Files written successfully.")

if __name__ == "__main__":
    write_files('file1.txt', 'file2.txt')