import os
import subprocess


def check_apis(report_name):
    apis = [
        'pyqt5',
        'pyqt6',
        'pyside2',
        'pyside6',
    ]

    for api in apis:
        os.environ['QT_API'] = api
        subprocess.call(f"python module_report/check_api.py {report_name}", shell=True)
