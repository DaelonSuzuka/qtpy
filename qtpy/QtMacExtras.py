# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides classes and functions specific to macOS and iOS operating systems"""

import sys
from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError, QtBindingsNotFoundError

if sys.platform == 'darwin':
    if PYQT5:
        from PyQt5.QtMacExtras import *
    elif PYQT6:
        raise PythonQtError('QtMacExtras does not exist in Qt6')
    elif PYSIDE2:
        from PySide2.QtMacExtras import *
    elif PYSIDE6:
        raise PythonQtError('QtMacExtras does not exist in Qt6')
    else:
        raise QtBindingsNotFoundError()
else:
    raise PythonQtError('QtMacExtras does not exist on this operating system')
