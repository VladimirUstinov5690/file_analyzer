from pathlib import Path

from load_file import FileReader
from analyzer import JsonAnalyser, CsvAnalyzer, XmlAnalyzer


def get_analyzer(file: str):
    reader = FileReader(file)
    extension = Path(file).suffix.lower()
    
    if extension == '.json' or extension == '.log':
        data_iter = reader.read_json()
        return JsonAnalyser(data_iter)
    elif extension == '.csv':
        data_iter = reader.read_csv()
        return CsvAnalyzer(data_iter)
    elif extension == '.xml':
        data_iter = reader.read_xml()
        return XmlAnalyzer(data_iter)
    else:
        raise ValueError(f'unknown format - {extension}')
