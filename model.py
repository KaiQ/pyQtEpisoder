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
    return len(self.store.getShows())

  def columnCount(self, parent):
    return 4

  def data(self, index, role = QtCore.Qt.DisplayRole):
    if not index.isValid():
      return QtCore.QVariant()
    
    row = index.row()
    column = index.column()
    data = self.store.getShows()[row]

    if role == QtCore.Qt.CheckStateRole:
      if column == 0:
        return QtCore.Qt.CheckState(data.enabled)

    if role == QtCore.Qt.BackgroundRole:
      if not data.show_name:
        return QtGui.QBrush(self.colors[0])
      return QtGui.QBrush(self.colors[data.status])

    if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
      if column == 1:
        return QtCore.QVariant(data.show_name)
      if column == 2:
        return QtCore.QVariant(data.url)
      if column == 3:
        return QtCore.QVariant("%s" % (data.updated))
      if column == 4:
        return data.show_id

    return QtCore.QVariant()


  def setData(self, index, value, role):
    if not index.isValid():
      return False
    
    row = index.row()
    column = index.column()
    data = self.store.getShowById(self.store.getShows()[row].show_id)

    if role == QtCore.Qt.CheckStateRole:
      if column == 0:
        if data.enabled:
          data.enabled = False
        else:
          data.enabled = True
        self.store.commit()
        self.data = self.store.getShows()
        self.dataChanged.emit(index, index)
        return True
    if role == QtCore.Qt.EditRole:
      if column == 2:
        data.url = str(value.toPyObject())
        self.store.commit()
        self.dataChanged.emit(index, index)
    return False

  def insertRow(self, position, parent = QtCore.QModelIndex()):
    if self.store.getShowByUrl("http://URL"):
      return False
    self.beginInsertRows(parent, self.rowCount(None), self.rowCount(None))
    show = episoder.Show("", url="http://URL")
    self.store.addShow(show)
    self.store.commit()
    self.endInsertRows()
    return True


  def removeRow(self, position, parent = QtCore.QModelIndex()):
    data = self.store.getShows()[position]
    self.beginRemoveRows(parent, position, position)
    self.store.removeShow(data.show_id)
    self.store.commit()
    self.endRemoveRows()
    return True
    


  def flags(self, index):
    column = index.column()

    if column == 0:
      return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable  
    if column == 2:
      return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
    
    return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

