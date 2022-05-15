import importlib
from check_modules import *
import qtpy
import sys


report_name = 'import_report.txt'
if len(sys.argv) == 2:
    report_name = sys.argv[1]


lines = ['', '']
lines.append(qtpy.API_NAME)
lines.append('------------------------------------------')
for m in module_names:
    try:
        mod = importlib.import_module(f'qtpy.{m}')
    except Exception as e:
        lines.append(f'{e.__class__.__name__}: {e}')

lines.append('------------------------------------------')

with open(f'module_report/{report_name}', 'a') as f:
    f.write('\n'.join(lines))