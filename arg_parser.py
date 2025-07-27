import argparse

parser = argparse.ArgumentParser(description='''This script parses logs and
outputs reports for a given file.
Example of launch:
python main.py --file "path_to_file" --report "average"

Report types:
"something" - Your custom report (explanation of what it does)
"average" - Average API response time
"good_worker" - Useful link for finding a good worker''')

parser.add_argument('--file', type=str, help="file's name", default=None)
parser.add_argument('--report', type=str, help="type of report",
                    default=None)

args = parser.parse_args()
