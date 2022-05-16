import importlib
import sys

import qtpy

from check_modules import QT_MODULE_NAMES


report_name = 'import_report.txt'
if len(sys.argv) == 2:
    report_name = sys.argv[1]


lines = ['', '']
lines.append(qtpy.API_NAME)
lines.append('-' * 50)
for module_name in QT_MODULE_NAMES:
    try:
        mod = importlib.import_module(f'qtpy.{module_name}')
    except Exception as e:
        lines.append(f'{type(e).__name__}: {e}')

lines.append('-' * 50)

with open(f'module_report/{report_name}', 'a', encoding='UTF-8') as f:
    f.write('\n'.join(lines))
