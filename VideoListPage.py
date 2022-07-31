from re import X
from PyQt5 import QtCore, QtGui, QtWidgets
import bs4
import DataBase
import requests
from bs4 import BeautifulSoup
import urllib.request 
import pafy
from PyQt5.QtGui import*
import VideoPlay

class VideoListPage:
    def __init__(self,ui,id,listname):
        self.db=DataBase.DataBase()
        self.ui=ui
        self.id=id
        self.listname=listname
        self.linkname=[]
        self.imagelink=[]

        self.VideoListPrint()

        self.ui.VideoListPageBackBtn.clicked.connect(self.backMove)
        self.ui.VideoListPageAddBtn.clicked.connect(self.AddList)

        for i in range(0,len(self.ui.VideoPlayBtnNameList)):
            self.ui.VideoPlayBtnList[i].clicked.connect(lambda event, nowIndex=i : self.referVideoPlay.PlayStopVideo(nowIndex))

        for i in range(0,self.ui.VideoListNum):
            self.ui.VideoPageList[i].clicked.connect(lambda event, nowIndex=i : self.Play(nowIndex))
            self.ui.VideoPageDeleteBtnList[i].clicked.connect(lambda event, nowIndex=i : self.DeleteClickEvent(nowIndex))

    def backMove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PlayListPage)
    
    def VideoListPrint(self):
        
        self.result=self.db.read("videolist",["id","listname"],[self.id,self.listname])
        
        for i in range(0,len(self.result)):
            self.linkname.append(self.result[i][4])
            
            self.imageFromWeb = urllib.request.urlopen(self.result[i][3]).read()
            self.imagelink.append(self.imageFromWeb)

        self.ui.VideoListNum=len(self.result)
        self.ui.VideoListBtn(self.linkname,self.imagelink)


    def AddList(self):
        try:
            text="추가하실 영상의 링크를 작성해주세요"
            self.ui.InputDialog(text)

            if self.ui.ok:

                self.url=self.ui.input
                video=pafy.new(self.url)
                name=f"{video.title}"
                self.result=self.db.read("videolist",["listname"],[self.url])
                if len(name)>30:
                    name=name[:29]+"..."

                if len(self.result)==0:
                    self.linkname.append(self.url)
                    self.imageFromWeb = urllib.request.urlopen(self.url).read()
                    
                    self.imagelink.append(self.imageFromWeb)

                    self.db.insert("videolist",["id","listname","listlink","linkname"],[self.id,self.listname,self.url,name])
                    self.ui.VideoListNum+=1
                    self.ui.resultDialog("추가에 성공하셨습니다")
                    self.VideoListPrint()

                else:
                    self.ui.resultDialog("이미 존재하는 이름")

        except:
            self.ui.resultDialog("url을 입력해주세요") 


    def DeleteClickEvent(self,index):

        self.ui.DeleteDialog("플레이리스트를 삭제하시겠습니까?")
        if self.ui.retval == QtWidgets.QMessageBox.Ok :
            self.ui.VideoListNum-=1
            del self.ui.VideoPageList[index]
            del self.ui.VideoPageDeleteBtnList[index]
            del self.ui.VideoListPicList[index]
            listlink=self.result[index][3]
            self.db.delete("videolist",["listname","listlink"],[self.listname,listlink])
            self.ui.resultDialog("삭제 성공했습니다.")
            self.VideoListPrint()
        
        elif self.ui.retval == QtWidgets.QMessageBox.Cancel:
            self.ui.resultDialog("삭제하지 않습니다.")

    def Play(self,index):
        self.result=self.db.read("videolist",["listname"],[self.listname])
        url=self.result[index][3]
        print(url)
        self.referVideoPlay=VideoPlay.VideoPlay(self.ui,url)