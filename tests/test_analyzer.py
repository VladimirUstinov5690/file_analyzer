import pytest
from analyzer import JsonAnalyser


def test_avg_time_response():
    data = [
        {'url': '/api/1', 'response_time': 0.1},
        {'url': '/api/1', 'response_time': 0.3},
        {'url': '/api/2', 'response_time': 0.2}
    ]
    analyzer = JsonAnalyser(iter(data))
    result = analyzer.avg_time_response()
    
    assert isinstance(result, str)
    
    # Проверяем наличие заголовков
    assert 'handler' in result
    assert 'total' in result
    assert 'avg_response_time' in result
    
    # Проверяем наличие URL
    assert '/api/1' in result
    assert '/api/2' in result
    
    # Проверяем, что средние значения присутствуют
    assert '0.2' in result
    assert '0.2' in result
