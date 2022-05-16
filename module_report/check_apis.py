import os
import subprocess
import sys
from pathlib import Path

import qtpy


def check_apis(report_name):
    for api in sorted(qtpy.API_NAMES):
        subprocess.run(
            [sys.executable, Path(__file__).parent / 'check_api.py', report_name],
            check=False, # check_api.py apparently returns a non-zero exit status despite not failing
            env={**os.environ, 'QT_API': api},
        )
