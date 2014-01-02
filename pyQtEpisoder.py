#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import ui
import model
import store
import sys
import os

class MainWindow(QtGui.QWidget):
  
  Update = QtCore.pyqtSignal(int);

  def _update_all(self):
    self.Update.connect(self.store.update_all)
    self.Update.emit(0)
    self.Update.disconnect(self.store.update_all)

  def _update_selected(self):
    self.Update.connect(self.store.update_single)
    self.Update.emit(self.ui.view.currentIndex().row())
    self.Update.disconnect(self.store.update_single)

  def _add(self):
    self.model.insertRow(0)

  def _remove(self):
    self.model.removeRow(self.ui.view.currentIndex().row())

  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    self.ui = ui.Ui_Episoder()
    self.ui.setupUi(self)
    
    self.store = store.Store(os.path.join(os.environ["HOME"], '.episodes'), self)
    self.model = model.Model(self.store)
    self.ui.view.setModel(self.model)

    self.ui.bUpdateAll.clicked.connect(self._update_all)
    self.ui.bUpdateSelected.clicked.connect(self._update_selected)
    self.ui.bAdd.clicked.connect(self._add)
    self.ui.bRemove.clicked.connect(self._remove)


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  mainWindow = MainWindow()
  mainWindow.show()
  sys.exit(app.exec_())
