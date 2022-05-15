import importlib
from pathlib import Path


lib_path = Path('.venv/lib/python3.8/site-packages/')
libs = ['PyQt5', 'PyQt6', 'PySide2', 'PySide6']
qtpy_files = [f.name[:-len('.py')] for f in Path('qtpy').glob('*.py') if f.name.startswith('Qt')]


modules = {}


for lib in libs:
    path = lib_path / lib
    files = path.glob('*.pyi')
    for f in files:
        if f.name.startswith('Qt'):
            name = f.name[:-len('.pyi')]
            if name not in modules:
                modules[name] = {'libs':[], 'missing': name not in qtpy_files}
            modules[name]['libs'].append(lib)

module_names = sorted(modules.keys())

false_positives = [
    'QtChart',
    'QtOpenGLFunctions',
    'QtScript',
    'QtScriptTools',
]

for name in false_positives:
    if name in module_names:
        module_names.remove(name)
    if name in modules:
        modules.pop(name)

new = []

report = []
for m in module_names:
    name = m
    if modules[m]['missing']:
        name += '*'
        new.append(m)
    report.append(f"{name.ljust(20)}{modules[m]['libs']}")

with open('modules.txt', 'w') as f:
    f.write('\n'.join(report))

report = []
for m in new:
    report.append(f"{m.ljust(20)}{modules[m]['libs']}")

    
with open('modules_new.txt', 'w') as f:
    f.write('\n'.join(report))

libs = [
    'qtpy',
]

import os
# os.environ['QT_API'] = 'pyqt6'
# os.environ['QT_API'] = 'pyside2'
# os.environ['QT_API'] = 'pyside6'

import qtpy


failed = []


print(qtpy.API_NAME)
print('------------------------------------------')


for l in libs:
    try:
        mod = importlib.import_module(l)
        for m in module_names:
            name = f'{l}.{m}'

            try:
                mod = importlib.import_module(name)
            except Exception as e:
                print(e)
                failed.append(name)
    except:
        failed.append(l)


print('------------------------------------------')
# print(failed)


imports = [
    'PYQT5:',
    'PYQT6:',
    'PYSIDE2:',
    'PYSIDE6:',
]

# files = Path('qtpy').glob('*.py')

# for file_name in files:
#     if file_name.name.startswith('Qt'):
#         with open(file_name) as f:
#             text = f.read()
#             _imports = []
#             for i in imports:
#                 if i in text:
#                     _imports.append(i)
#             print(_imports, file_name)