from pathlib import Path


def check_missing_cases():
    imports = [
        'PYQT5:',
        'PYQT6:',
        'PYSIDE2:',
        'PYSIDE6:',
    ]


    files = Path('qtpy').glob('*.py')

    lines = []

    for file_name in files:
        if file_name.name.startswith('Qt'):
            with open(file_name) as f:
                text = f.read()
                _imports = []
                for i in imports:
                    if i in text:
                        _imports.append(i)
                lines.append(f'{file_name.as_posix().ljust(30)} {_imports}')

    with open('module_report/missing_cases.txt', 'w') as f:
        f.write('\n'.join(lines))