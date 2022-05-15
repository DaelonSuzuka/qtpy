from .check_modules import *
from .check_missing_cases import *
from .check_apis import *
import sys


if __name__ == '__main__':
    report_name = 'import_report.txt'
    if len(sys.argv) == 2:
        report_name = sys.argv[1]

    # write_module_report()
    check_missing_cases()

    # reset the import_report file
    with open(f'module_report/{report_name}', 'w') as f:
        f.write('')

    check_apis(report_name)