#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import pyepisoder.episoder as episoder
import time


class Store(QtCore.QObject):

  UpdateFinished = QtCore.pyqtSignal(int)

  def __init__(self, store_adress, parent=None):
    super(Store, self).__init__(parent)
    self.store = episoder.DataStore(store_adress)
    self.update()
    self.loop = QtCore.QEventLoop()

  def __getitem__(self, index):
    return self.showsByID[index]

  def isEnabled(self, index):
    return self.showsByID[index].enabled

  def setEnabled(self, index, value):
    self.showsByID[index].enabled = value
    self.commit()

  def setURL(self, index, value):
    self.showsByID[index].url = value
    self.commit()

  def getName(self, index):
    return self.shows[index].show_name

  def getID(self, index):
    return self.store.getShowById(self.shows[index].show_id)

  def getURL(self, index):
    return self.showsByID[index].url

  def getShowsCount(self):
    return self.showsCount

  def update(self):
    self.store.update()
    self.shows = self.store.getShows()
    self.showsByID = [self.getID(i) for i in xrange(len(self.shows))] 
    self.showsCount = len(self.showsByID)

  def commit(self):
    self.store.commit()

  def addShow(self, show):
    self.store.addShow(show)
    self.commit()
    self.update()

  def removeShow(self, show):
    self.store.removeShow(show)
    self.commit()
    self.update()

  def _update(self, number):
    if number >= 0:
      if number < self.showsCount:
        self.showsByID[number].update(self.store, "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)")
    self.UpdateFinished.emit(number+1)

  def update_all(self):
    self.prog = QtGui.QProgressDialog("Processing", "Cancel", 0, self.showsCount , None)
    self.prog.forceShow()
    for num in xrange(0, self.showsCount+1) :
      self._update(num)
      self.prog.setValue(num)

  def update_single(self, number):
    self.prog = QtGui.QProgressDialog("Processing", "Cancel", number, max(1,number), None)
    self.prog.forceShow()
    for num in xrange(number, max(1,number)+1) :
      self._update(num)
      self.prog.setValue(num)
    self.commit()
    self.update()
