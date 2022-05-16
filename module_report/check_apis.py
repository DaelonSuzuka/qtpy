import os
import subprocess
import sys
from pathlib import Path

import qtpy


def check_apis(report_name):
    for api in sorted(qtpy.API_NAMES):
        # this doesn't actually change the QT_API
        # I would prefer using this if it actually worked
        # child_env = dict(os.environ).update({'QT_API': api})

        # still required to actually change the selected API
        os.environ['QT_API'] = api

        subprocess.run(
            [sys.executable, Path(__file__).parent / 'check_api.py', report_name],
            check=False, # check_api.py apparently returns a non-zero exit status despite not failing
            # env=child_env
        )
