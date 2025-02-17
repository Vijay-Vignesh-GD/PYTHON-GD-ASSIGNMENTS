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


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

def reversed_words(words):
    return list(reversed(words))

def writewords(words):
    with open('file1.txt', 'w', encoding='UTF8') as f1:
        f1.write('\n'.join(words))

    with open('file2.txt', 'w', encoding='CP1252') as f2:
        f2.write(','.join(reversed_words))

if __name__ == "__main__":

    words = generate_words(80) 

    writewords(words)
