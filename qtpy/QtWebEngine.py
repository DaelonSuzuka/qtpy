# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""
Provides QtWebEngine classes and functions.
"""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    try:
        from PyQt5.QtWebEngine import *
    except ImportError as error:
        raise PythonQtError(
            'The QtWebEngine module was not found. '
            'It needs to be installed separately for PyQt5.'
            ) from error
elif PYQT6:
    raise PythonQtError('QtWebEngine does not exist in Qt6')
elif PYSIDE2:
    from PySide2.QtWebEngine import *
elif PYSIDE6:
    raise PythonQtError('QtWebEngine does not exist in Qt6')
else:
    raise PythonQtError('No Qt bindings could be found')
