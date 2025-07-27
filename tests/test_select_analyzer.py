import pytest
from select_analyzer import get_analyzer
from analyzer import JsonAnalyser
from load_file import FileReader


def test_get_analyzer_returns_json_analyzer(monkeypatch):
    # Подменим метод read_json, чтобы не читать настоящий файл
    def fake_read_json(self):
        return iter([{'url': '/api', 'response_time': 0.2}])
    
    monkeypatch.setattr(FileReader, 'read_json', fake_read_json)
    
    analyzer = get_analyzer("f_data.json")
    assert isinstance(analyzer, JsonAnalyser)
    
    analyzer = get_analyzer("f_data.log")
    assert isinstance(analyzer, JsonAnalyser)


def test_get_analyzer_invalid_extension():
    with pytest.raises(ValueError) as excinfo:
        get_analyzer("data.unsupported")
    
    assert "unknown format" in str(excinfo.value)