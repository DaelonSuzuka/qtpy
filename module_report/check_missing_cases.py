from pathlib import Path

import qtpy


def check_missing_cases():
    imports = [f'{api_name.upper()}:' for api_name in qtpy.API_NAMES]

    files = Path('qtpy').glob('*.py')

    lines = []

    for file_name in files:
        if file_name.name.startswith('Qt'):
            text = file_name.read_text(encoding='UTF-8')
            _imports = [_import for _import in imports if _import in text]
            lines.append(f'{file_name.as_posix().ljust(30)} {_imports}')

    with open('module_report/missing_cases.txt', 'w', encoding='UTF-8') as f:
        f.write('\n'.join(lines))
