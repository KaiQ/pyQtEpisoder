#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import pyepisoder.episoder as episoder
import ui
import model
import sys
import os

class MainWindow(QtGui.QWidget):

  def _update_all(self):
    shows = self.store.getEnabledShows()
    prog = QtGui.QProgressDialog("Text1", "text2", 0, len(shows), self)
    prog.setWindowModality(QtCore.Qt.WindowModal)
    prog.setValue(0)
    num = 1
    for show in shows:
      prog.setValue(num)
      num+=1
      show.update(self.store, "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)")
    self.store.update()

  def _update_selected(self):
    shows = self.store.getEnabledShows()
    for show in xrange(len(shows)):
      if self.model.data(self.model.index(self.ui.view.currentIndex().row(),2)).toPyObject() == shows[show].url:
        shows[show].update(self.store, "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)")
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

    self.ui.bUpdateAll.clicked.connect(self._update_all)
    self.ui.bUpdateSelected.clicked.connect(self._update_selected)
    self.ui.bAdd.clicked.connect(self._add)
    self.ui.bRemove.clicked.connect(self._remove)


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  mainWindow = MainWindow()
  mainWindow.show()
  sys.exit(app.exec_())
