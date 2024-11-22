import os
import csv
from concurrent.futures import ThreadPoolExecutor
from random import randint
OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'
# Function to calculate Fibonacci number by its ordinal position
def fib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    f0, f1 = 0, 1
    for _ in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1
# Helper function to write Fibonacci value to a file
def write_fib_to_file(n: int):
    filename = f'{OUTPUT_DIR}/{n}.txt'
    fib_value = fib(n)
    with open(filename, 'w') as f:
        f.write(str(fib_value))
    return n, fib_value  # returning for logging purposes
# Function to calculate Fibonacci numbers and write them to files
def func1(array: list):
    with ThreadPoolExecutor() as executor:
        results = executor.map(write_fib_to_file, array)
    for result in results:
        print(f'Written Fibonacci number for {result[0]} to file')
# Function to read Fibonacci values from files and write them to a CSV file
def func2(array: list, result_file: str):
    with open(result_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for n in array:  # Iterate over the original array to maintain order
            filename = f'{OUTPUT_DIR}/{n}.txt'
            with open(filename, 'r') as f:
                fib_value = f.read().strip()
                csv_writer.writerow([n, fib_value])
    print(f'CSV file written to {result_file}')
if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    input_array = [5, 1, 8, 10]  
    func1(input_array) 
    func2(input_array, result_file=RESULT_FILE)  