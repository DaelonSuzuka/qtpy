# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""
Provides QtNetworkAuth classes and functions.
"""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    try:
        from PyQt5.QtNetworkAuth import *
    except ImportError as error:
        raise PythonQtError(
            'The QtNetworkAuth module was not found. '
            'It needs to be installed separately for PyQt5.'
            ) from error
elif PYQT6:
    try:
        from PyQt6.QtNetworkAuth import *
    except ImportError as error:
        raise PythonQtError(
            'The QtNetworkAuth module was not found. '
            'It needs to be installed separately for PyQt6.'
            ) from error
elif PYSIDE2:
    raise PythonQtError('QtNetworkAuth not implemented in PySide2')
elif PYSIDE6:
    from PySide6.QtNetworkAuth import *
else:
    raise PythonQtError('No Qt bindings could be found')
