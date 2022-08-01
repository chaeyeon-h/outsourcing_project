from PyQt5 import QtCore, QtGui, QtWidgets
import DataBase
import VideoListPage

class PlayListPage:
    def __init__(self,ui,id):
        self.db=DataBase.DataBase()
        self.ui=ui
        self.id=id
        self.ui.playListPageBackBtn.clicked.connect(self.backMove)
        self.ui.playListPageAddBtn.clicked.connect(self.AddList)
        
        self.PlayListPrint()

    def PlayListBtnEvent(self):
        for i in range(0,self.ui.PlayListNum):
            self.ui.PlayPageMoveToVideoList[i].clicked.connect(lambda event, nowIndex=i : self.MoveToVideoPage(nowIndex))
            self.ui.PlayPageChangeBtnList[i].clicked.connect(lambda event, nowIndex=i : self.ChangeClickEvent(nowIndex))
            self.ui.PlayPageDeleteBtnList[i].clicked.connect(lambda event, nowIndex=i : self.DeleteClickEvent(nowIndex))

    def backMove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    def PlayListPrint(self):
        self.listname=[]
        self.result=self.db.read("playlist",["id"],[self.id])
        self.ui.PlayListNum=len(self.result)
        print(self.result)
        for i in range(0,len(self.result)):
            self.listname.append(self.result[i][2])
        self.ui.PlayListBtn(self.listname)
        self.PlayListBtnEvent()
        
    
    def AddList(self):
        text="추가하실 재생목록의 이름을 작성해주세요"
        self.ui.InputDialog(text)

        if self.ui.ok:
            self.text=self.ui.input 
            self.result=self.db.read("playlist",["id","listname"],[self.id,self.text])
            print(self.result)
            if len(self.text)<20:
                if len(self.result)==0:
                    print(self.ui.PlayListNum)
                    print(self.result)
                    self.db.insert("playlist",["id","listname"],[self.id,self.text])
                    self.ui.PlayListNum+=1
                    self.ui.resultDialog("추가에 성공하셨습니다")
                    self.PlayListPrint()
                else:
                    self.ui.resultDialog("이미 존재하는 이름")  
            else:
                self.ui.resultDialog("재생목록의 길이는 20자 미만입니다.")

    def DeleteClickEvent(self,index):

        self.ui.DeleteDialog("플레이리스트를 삭제하시겠습니까?")
        if self.ui.retval == QtWidgets.QMessageBox.Ok :
            self.ui.PlayListNum-=1
            del self.ui.PlayPageMoveToVideoList[index]
            del self.ui.PlayPageDeleteBtnList[index]
            del self.ui.PlayPageChangeBtnList[index]
            listname=self.result[index][2]
            self.db.delete("playlist",["id","listname"],[self.id,listname])
            self.ui.resultDialog("삭제 성공했습니다.")
            self.PlayListPrint()
        
        elif self.ui.retval == QtWidgets.QMessageBox.Cancel:
            self.ui.resultDialog("삭제하지 않습니다.")
        
    def ChangeClickEvent(self,index):

        text=" 재생목록의 이름을 작성해주세요 "
        self.ui.InputDialog(text)

        if self.ui.ok:
            self.text=self.ui.input
            if len(self.text)<20:
                self.resultListName=self.db.read("playlist",["listname","id"],[self.text,self.id])
                
                if len(self.resultListName)==0:
                    listname=self.result[index][2]
                    self.db.update("playlist",["listname","id","listname"],[listname,self.id,self.text])
                    self.db.update("videolist",["id","listname","listname"],[self.id,listname,self.text])
                    self.ui.PlayPageMoveToVideoList[index].setText(self.text)
                    self.ui.resultDialog("수정에 성공하셨습니다")
                    self.PlayListPrint()
                else:
                    self.ui.resultDialog("이미 존재하는 이름")
            else:
                self.ui.resultDialog("재생목록의 길이는 20자 미만입니다.")

    def MoveToVideoPage(self,index):
        self.listname=self.result[index][2]
        print(self.listname)
        self.referVideoListPage=VideoListPage.VideoListPage(self.ui, self.id, self.listname)
        self.ui.stackedWidget.setCurrentWidget(self.ui.VideoListPage)

