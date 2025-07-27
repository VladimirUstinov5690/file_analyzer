import pytest
import json
import tempfile
import os
from load_file import FileReader


def test_read_json_yields_dicts():
    data = [
        {"url": "/api/1", "response_time": 0.1},
        {"url": "/api/2", "response_time": 0.2}
    ]
    
    # временный файл
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.json',
                                     delete=False) as tmp:
        for item in data:
            tmp.write(json.dumps(item) + '\n')
        tmp_path = tmp.name
    
    reader = FileReader(tmp_path)
    result = list(reader.read_json())
    
    assert result == data
    
    os.remove(tmp_path)


def test_read_json_file_not_found():
    reader = FileReader('nonexistent_file.json')
    
    with pytest.raises(FileNotFoundError) as excinfo:
        list(reader.read_json())
    
    assert 'is not found' in str(excinfo.value)
