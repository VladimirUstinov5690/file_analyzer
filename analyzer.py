from abc import abstractmethod

from utils import pretty_print


class BaseReader:
    """Base class for reading file"""
    
    @abstractmethod
    def avg_time_response(self):
        pass


class JsonAnalyser(BaseReader):
    """Class for analyzing data from json file"""
    
    def __init__(self, data_iter):
        self.data_iter = data_iter
    
    def avg_time_response(self):
        """Displays the average response time for each request for JSON"""
        res_dict = {}
        
        for dict_el in self.data_iter:
            api = dict_el['url']
            response_time = float(dict_el['response_time'])
            if api not in res_dict:
                res_dict[api] = {'total': 1, 'avg': dict_el['response_time']}
            else:
                res_dict[api]['total'] += 1
                res_dict[api]['avg'] += float(response_time)
        
        for api, value in res_dict.items():
            value['avg'] = round(value['avg'] / value['total'], 3)
        
        data_list = [(api, value['total'], value['avg']) for api, value in
                     res_dict.items()]
        
        sorted_data = sorted(data_list, key=lambda x: x[1], reverse=True)
        
        res_data = [(i, *row) for i, row in enumerate(sorted_data)]
        
        # column names
        headers = ['handler', 'total', 'avg_response_time']
        
        if res_data:
            return pretty_print(res_data, headers=headers)
        return 'File is empty'
    
    def get_report(self):
        """something what you want to get"""
        pass
    
    def get_good_worker(self):
        return f'You can get a good worker: https://hh.ru/resume/a8abea4bff0df5fd360039ed1f4f6237655234'


class CsvAnalyzer(BaseReader):
    """Class for analyzing data from csv file"""
    
    def __init__(self, data_iter):
        self.data_iter = data_iter
    
    def avg_time_response(self):
        """Displays the average response time for each request for CSV"""
        pass


class XmlAnalyzer(BaseReader):
    """Class for analyzing data from xml file"""
    
    def __init__(self, data_iter):
        self.data_iter = data_iter
    
    def avg_time_response(self):
        """Displays the average response time for each request for XML"""
        pass
