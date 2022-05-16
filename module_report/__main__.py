import sys
from pathlib import Path

from .check_apis import check_apis
from .check_missing_cases import check_missing_cases
# from .check_modules import write_module_report


if __name__ == '__main__':
    report_name = 'import_report.txt'
    if len(sys.argv) == 2:
        report_name = sys.argv[1]

    # write_module_report()
    check_missing_cases()

    # reset the import_report file
    Path('module_report', report_name).unlink(missing_ok=True)

    check_apis(report_name)
