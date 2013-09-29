#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import pyepisoder.episoder as episoder
import ui
import model
import sys
import os

class MainWindow(QtGui.QWidget):

  def _update(self):
    shows = self.store.getEnabledShows()
    for show in shows:
      show.update(self.store, "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)")
    self.store.update()

  def _add(self):
    self.model.insertRow(0)

  def _remove(self):
    self.model.removeRow(self.ui.view.currentIndex().row())

  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    self.ui = ui.Ui_Episoder()
    self.ui.setupUi(self)
    
    self.store = episoder.DataStore(os.path.join(os.environ["HOME"], '.episodes'))
    self.store.update()
    self.model = model.Model(self.store)
    self.ui.view.setModel(self.model)

    self.ui.bUpdate.clicked.connect(self._update)
    self.ui.bAdd.clicked.connect(self._add)
    self.ui.bRemove.clicked.connect(self._remove)


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  mainWindow = MainWindow()
  mainWindow.show()
  sys.exit(app.exec_())
