"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    file = open('filename.txt','r')
    minnum = float('inf')
    maxnum = float('-inf')
    for line in file:
        num = int(line.strip())
        minnum = min(minnum,num)
        maxnum = max(maxnum,num)

    

    return (minnum, maxnum)
    
        # print(type(num))
print(get_min_max('filename.txt'))

