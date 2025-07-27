import json
from typing import Iterator


class FileReader:
    """Class for reading data from different formats"""
    
    def __init__(self, file: str):
        self.file = file
    
    def read_json(self) -> Iterator[dict]:
        """Read json objects from file and return iterable object"""
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                for line in f:
                    data_dict = json.loads(line)
                    yield data_dict
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.file} is not found')
    
    def read_csv(self):
        """scaling example"""
        pass
    
    def read_xml(self):
        """scaling example"""
        pass
