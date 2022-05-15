import importlib
from pathlib import Path
import platform
import subprocess


lib_path = Path([*Path('.venv').rglob('site-packages')][0])
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


def write_module_report():
    report = []
    for m in module_names:
        name = m
        if modules[m]['missing']:
            name += '*'
        report.append(f"{name.ljust(20)}{modules[m]['libs']}")

    with open('module_report/module_report.txt', 'w') as f:
        f.write('\n'.join(report))
