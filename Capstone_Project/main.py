import os
import json
import random
import argparse
import configparser
from faker import Faker
from datetime import datetime
from multiprocessing import Process

faker_instance = Faker()

def create_data_entry(schema, num_entries):
    entries = []
    for _ in range(num_entries):
        record = {}
        for field, rule in schema.items():
            if rule.startswith("int:rand"):
                start_end = rule[len("int:rand("):-1]  # Correct extraction
                start, end = map(int, start_end.split(","))
                record[field] = random.randint(start, end)
            elif rule == "timestamp":
                record[field] = datetime.now().isoformat()
            elif rule == "str:rand":
                record[field] = faker_instance.name()
            elif rule.startswith("["):
                options = json.loads(rule.replace("'", '"'))
                record[field] = random.choice(options)
        entries.append(record)
    return entries

def save_to_file(filepath, records):
    with open(filepath, 'w') as file:
        file.writelines(json.dumps(record) + "\n" for record in records)

def create_file(output_folder, base_name, prefix, schema_json, num_entries, idx):
    full_path = os.path.join(output_folder, f"{prefix}_{base_name}_{idx}.json")
    print(f"Creating file: {full_path}")
    schema = json.loads(schema_json)
    records = create_data_entry(schema, num_entries)
    save_to_file(full_path, records)

def read_configuration():
    parser = configparser.ConfigParser()
    parser.read('config/default.ini')
    return parser['DEFAULT']

def run_generator():
    config = read_configuration()
    
    arg_parser = argparse.ArgumentParser(description="Random Data File Generator")
    arg_parser.add_argument("--file_count", type=int, default=config.getint('files_count'))
    arg_parser.add_argument("--file_name", type=str, default=config['file_name'])
    arg_parser.add_argument("--prefix", type=str, default=config['file_prefix'])
    arg_parser.add_argument("--path_to_save", type=str, default=config['path_to_save_files'])
    arg_parser.add_argument("--multiprocessing", type=int, default=config.getint('multiprocessing'))
    arg_parser.add_argument("--data_lines", type=int, default=config.getint('data_lines'))
    arg_parser.add_argument("--data_schema", type=str, required=True)
    
    arguments = arg_parser.parse_args()

    os.makedirs(arguments.path_to_save, exist_ok=True)

    processes = [
        Process(target=create_file, args=(
            arguments.path_to_save, arguments.file_name, arguments.prefix,
            arguments.data_schema, arguments.data_lines, i))
        for i in range(arguments.file_count)
    ]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    print("Files generated successfully!")

if __name__ == "__main__":
    run_generator()
