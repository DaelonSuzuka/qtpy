# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtOpenGLWidgets classes and functions."""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, QtBindingsNotFoundError, QtBindingMissingModuleError

if PYQT5:
    raise QtBindingMissingModuleError(name='QtTextToSpeech')
elif PYQT6:
    from PyQt6.QtOpenGLWidgets import *
elif PYSIDE2:
    raise QtBindingMissingModuleError(name='QtTextToSpeech')
elif PYSIDE6:
    from PySide6.QtOpenGLWidgets import *
else:
    raise QtBindingsNotFoundError()
