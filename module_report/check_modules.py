from pathlib import Path
import pkgutil

import qtpy


QTPY_MODULES = [module.name for module in pkgutil.iter_modules(qtpy.__path__)
                if module.name.startswith('Qt')]


QT_MODULES = {}

FALSE_POSITIVES = [
    'Qt',
    'QtChart',
    'QtOpenGLFunctions',
    'QtScript',
    'QtScriptTools',
]


for api_name in sorted(qtpy.API_NAMES.values()):
    try:
        api_path = pkgutil.resolve_name(api_name).__path__
    except ImportError:
        continue
    api_modules = [mod.name for mod in pkgutil.iter_modules(api_path) if mod.name.startswith('Qt')]

    for module in api_modules:
        if module in FALSE_POSITIVES:
            continue
        if module not in QT_MODULES:
            QT_MODULES[module] = {'apis':[], 'missing': module not in QTPY_MODULES}
        QT_MODULES[module]['apis'].append(api_name)


QT_MODULE_NAMES = sorted(QT_MODULES.keys())


def write_module_report():
    report_lines = []
    for module in QT_MODULE_NAMES:
        name = module
        if QT_MODULES[module]['missing']:
            name += '*'
        report_lines.append(f'{name.ljust(20)}{QT_MODULES[module]["apis"]}')

    with open('module_report/module_report.txt', 'w', encoding='UTF-8') as f:
        f.write('\n'.join(report_lines))
