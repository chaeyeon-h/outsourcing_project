from PyQt5 import QtCore, QtGui, QtWidgets
import DataBase

class PlayListPage:
    def __init__(self,ui,id):
        self.db=DataBase.DataBase()
        self.ui=ui
        self.id=id
    
        self.ui.playListPageAddBtn.clicked.connect(self.AddList)

    def AddList(self):
        text="추가하실 재생목록의 이름을 작성해주세요"
        # db에서 있는 제목인지 불러오기 == result
        # 없으면 추가하기
