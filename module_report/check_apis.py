import os
import sys
import subprocess

import qtpy


for api in qtpy.API_NAMES:
        child_env = dict(os.environ).update({'QT_API': api})
        subprocess.run(
            [sys.executable, Path(__file__).parent / 'check_api.py', report_name],
            check=True, env=child_env)
