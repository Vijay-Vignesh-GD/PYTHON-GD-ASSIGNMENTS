import os
import pytest
import json
from main import create_data_entry, save_to_file

data_schema = {
    "date": "timestamp",
    "name": "str:rand",
    "type": "['client', 'partner', 'government']",
    "age": "int:rand(1, 90)"
}

def test_data_generation():
    expected_lines = 10
    data = create_data_entry(data_schema, expected_lines)
    
    assert len(data) == expected_lines
    for entry in data:
        for key in ["date", "name", "type", "age"]:
            assert key in entry
        assert isinstance(entry['age'], int)
        assert entry['type'] in ['client', 'partner', 'government']

def test_data_persistence(tmp_path):
    sample = [
        {"date": "2024-09-24T10:00:00", "name": "John Doe", "type": "client", "age": 30},
        {"date": "2024-09-24T11:00:00", "name": "Jane Smith", "type": "partner", "age": 25}
    ]
    
    file_location = tmp_path / "saved_data.json"
    save_to_file(file_location, sample)
    
    assert file_location.exists()
    with open(file_location) as f:
        lines = f.readlines()
        assert len(lines) == len(sample)
        for line in lines:
            record = json.loads(line)
            assert "date" in record
            assert "name" in record
            assert "type" in record
            assert "age" in record

@pytest.mark.parametrize("schema, line_count", [
    (data_schema, 10),
    (data_schema, 100),
])
def test_data_file_creation(tmp_path, schema, line_count):
    filename_prefix = "generated"
    output_filepath = tmp_path / f"{filename_prefix}_data_0.json"
    
    random_data = create_data_entry(schema, line_count)
    save_to_file(output_filepath, random_data)

    assert output_filepath.exists()
    with open(output_filepath) as f:
        lines = f.readlines()
        assert len(lines) == len(random_data)
