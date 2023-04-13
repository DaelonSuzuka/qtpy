# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtTextToSpeech classes and functions."""

from packaging.version import parse
from qtpy import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
    PYSIDE_VERSION,
    QtBindingMissingModuleError,
)

if PYQT5:
    from PyQt5.QtTextToSpeech import *
elif PYQT6:
    raise QtBindingMissingModuleError(name='QtTextToSpeech')
elif PYSIDE2:
    from PySide2.QtTextToSpeech import *
elif PYSIDE6:
    if parse(PYSIDE_VERSION) >= parse('6.5'):
        from PySide6.QtTextToSpeech import *
    else:
        raise QtBindingMissingModuleError(name='QtTextToSpeech')
