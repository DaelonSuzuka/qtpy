from pathlib import Path
import pkgutil

import qtpy


QTPY_MODULES = [module.name for module in pkgutil.iter_modules(qtpy.__path__)
                if module.name.startswith(Qt)]


QT_MODULES = {}

FALSE_POSITIVES = [
    'QtChart',
    'QtOpenGLFunctions',
    'QtScript',
    'QtScriptTools',
]


for api_name in qtpy.API_NAMES.values():
    try:
        api_path = pkgutil.resolve_name(api_name).__path__
    except ImportError:
        continue
    api_modules = [mod.name for mod in pkgutil.iter_modules(api_path)]
    api_modules =  [mod for mod in api_modules if mod.name.startswith('Qt')]
    for module in api_modules:
        if module not in QT_MODULES and module not in FALSE_POSITIVES:
            modules[module] = {'apis':[], 'missing': name not in QTPY_MODULES}
        modules[api_module]['apis'].append(module)


QT_MODULE_NAMES = sorted(modules.keys())


def write_module_report():
    report_lines = []
    for module in module_names:
        name = module
        if modules[module]['missing']:
            name += '*'
        report.append(f'{name.ljust(20)}{modules[module]["apis"]}')`

    with open('module_report/module_report.txt', 'w', encoding='UTF-8') as f:
        f.write('\n'.join(report_lines))
