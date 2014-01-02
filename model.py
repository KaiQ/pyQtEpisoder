# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
import pyepisoder.episoder as episoder

class Model(QtCore.QAbstractTableModel):
  def __init__(self, store, parent=None, *args):
    super(Model, self).__init__(parent, *args)
    self.store = store
    self.colors = [QtCore.Qt.gray, QtCore.Qt.green, QtCore.Qt.yellow, QtCore.Qt.red]

  def headerData(self, row, orientation, status):
    if orientation == QtCore.Qt.Vertical:
      return ""
    if status == QtCore.Qt.DisplayRole:
      if row == 0:
        return "Enabled"
      if row == 1:
        return "Name"
      if row == 2:
        return "URL"
      if row == 3:
        return "Last Update"

  def rowCount(self, parent):
    return self.store.getShowsCount()

  def columnCount(self, parent):
    return 4

  def data(self, index, role = QtCore.Qt.DisplayRole):
    if not index.isValid():
      return QtCore.QVariant()
    
    row = index.row()
    column = index.column()

    if role == QtCore.Qt.CheckStateRole:
      if column == 0:
        return QtCore.Qt.CheckState(self.store.isEnabled(row))

    if role == QtCore.Qt.BackgroundRole:
      if not self.store.getName(row):
        return QtGui.QBrush(self.colors[0])
      return QtGui.QBrush(self.colors[self.store[row].status])

    if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
      if column == 1:
        return QtCore.QVariant(self.store.getName(row))
      if column == 2:
        return QtCore.QVariant(self.store.getURL(row))
      if column == 3:
        return QtCore.QVariant("%s" % (self.store[row].updated))
      if column == 4:
        return self.store.getID(row)

    return QtCore.QVariant()


  def setData(self, index, value, role):
    if not index.isValid():
      return False
    
    row = index.row()
    column = index.column()

    if role == QtCore.Qt.CheckStateRole:
      if column == 0:
        if self.store.isEnabled(row):
          self.store.setEnabled(row, False)
        else:
          self.store.setEnabled(row, True)
        self.dataChanged.emit(index, index)
        return True
    if role == QtCore.Qt.EditRole:
      if column == 2:
        self.store.setURL(row, str(value.toPyObject()))
        self.dataChanged.emit(index, index)
    return False

  def insertRow(self, position, parent = QtCore.QModelIndex()):
    if self.store.urlExists("http://URL"):
      return False
    self.beginInsertRows(parent, self.rowCount(None), self.rowCount(None))
    show = episoder.Show("", url="http://URL")
    self.store.addShow(show)
    self.endInsertRows()
    return True


  def removeRow(self, position, parent = QtCore.QModelIndex()):
    self.beginRemoveRows(parent, position, position)
    self.store.removeShow(self.store[position].show_id)
    self.endRemoveRows()
    return True

  def flags(self, index):
    column = index.column()

    if column == 0:
      return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable  
    if column == 2:
      return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
    
    return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

