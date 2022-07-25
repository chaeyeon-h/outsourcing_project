from PyQt5 import QtCore, QtGui, QtWidgets
import DataBase

class PlayListPage:
    def __init__(self,ui,id):
        self.db=DataBase.DataBase()
        self.ui=ui
        self.id=id