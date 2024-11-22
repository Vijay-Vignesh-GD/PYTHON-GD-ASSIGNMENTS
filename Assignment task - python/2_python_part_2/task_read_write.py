"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os

def read_files_and_write_result(directory: str, output_file: str):
    values = []
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if content:
                    values.append(content)
                    

    with open(output_file, 'w', encoding='utf-8') as result_file:
        result_file.write(', '.join(values)) 

if __name__ == "__main__":
    directory = '/Users/vganesan/Documents/PYTHON/PYTHON-BASIC/practice/python_part_2/files'
    output_file = 'result.txt'
    read_files_and_write_result(directory, output_file)
