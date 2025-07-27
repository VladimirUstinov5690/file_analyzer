from arg_parser import args
from select_analyzer import get_analyzer


def main():
    # variables from console
    file = args.file
    report = args.report
    
    analyzer = get_analyzer(file)
    
    type_report_operation = {
        'something': lambda: analyzer.get_report(),
        'average': lambda: analyzer.avg_time_response(),
        'good_worker': lambda: analyzer.get_good_worker(),
    }

    if report not in type_report_operation:
        print('Try to use: --report "something"')
        print('Try to use: --report "average"')
        print('Try to use: --report "good_worker"')
        return  # или exit(1)

    result = type_report_operation[report]()
    print(result)


if __name__ == '__main__':
    main()
