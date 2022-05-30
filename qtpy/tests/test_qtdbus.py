import pytest
import sys
from qtpy import PYSIDE2, PYSIDE6, PYQT5, PYQT6

def test_qtdbus():
    """Test the qtpy.QtDBus namespace"""
    QtDBus = pytest.importorskip("qtpy.QtDBus")

    assert QtDBus.QDBusAbstractAdaptor is not None
    assert QtDBus.QDBusAbstractInterface is not None
    assert QtDBus.QDBusArgument is not None
    assert QtDBus.QDBusConnection is not None
