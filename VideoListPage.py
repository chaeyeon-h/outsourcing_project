from re import X
from PyQt5 import QtCore, QtGui, QtWidgets
import bs4
import DataBase
import requests
from bs4 import BeautifulSoup
import urllib.request 
import vlc
import pafy
from PyQt5.QtGui import*
import VideoPlay

class VideoListPage:
    def __init__(self,ui,listnum):
        self.db=DataBase.DataBase()
        self.ui=ui
        self.listnum=listnum
        self.linkname=[]
        self.imagelink=[]
        self.referVideoPlay=VideoPlay.VideoPlay(None,None,None)

        self.VideoListPrint()
            
        

    def backMove(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.PlayListPage)
        self.referVideoPlay.VideoControlEvent(1)
        self.ui.VideoListPageBackBtn.mousePressEvent=None
        self.ui.VideoListPageAddBtn.mousePressEvent = None

        for i in range(0,len(self.ui.VideoPlayBtnNameList)):
            self.ui.VideoPlayBtnList[i].mousePressEvent=None
            
        for i in range(0,self.ui.VideoListNum):
            self.ui.VideoPageList[i].mousePressEvent=None
            self.ui.VideoPageDeleteBtnList[i].mousePressEvent=None
        

    def VideoListPrint(self):

        self.linkname=[]
        self.imagelink=[]

        self.result=self.db.read("videolist",["numfromplaylist"],[self.listnum])
        print(self.result)
        
        for i in range(0,len(self.result)):
            self.linkname.append(self.result[i][3])
            self.imagelink.append(self.result[i][4])

        self.ui.VideoListNum=len(self.result)
        self.ui.VideoListBtn(self.linkname,self.imagelink)

        self.ui.VideoListPageBackBtn.mousePressEvent= lambda event: self.backMove()
        self.ui.VideoListPageAddBtn.mousePressEvent = lambda event: self.AddList()

        for i in range(0,self.ui.VideoListNum):
            self.ui.VideoPageList[i].mousePressEvent= lambda event, nowIndex=i : self.setVideo(nowIndex)
            self.ui.VideoPageDeleteBtnList[i].mousePressEvent=lambda event, nowIndex=i : self.DeleteClickEvent(nowIndex)

        for i in range(0,len(self.ui.VideoPlayBtnNameList)):
            self.ui.VideoPlayBtnList[i].mousePressEvent= lambda event, nowIndex=i : self.referVideoPlay.VideoControlEvent(nowIndex)

    def AddList(self):
        try:
            text="추가하실 영상의 링크를 작성해주세요"
            self.ui.InputDialog(text)

            if self.ui.ok:

                self.url=self.ui.input
                video=pafy.new(self.url)
                videoTime=int(video.duration[0])*36000+int(video.duration[1])*3600+int(video.duration[3])*600+int(video.duration[4])*60+int(video.duration[6])*10+int(video.duration[7])
                name=f"{video.title}"
                self.result=self.db.read("videolist",["numfromplaylist","listlink"],[self.listnum,self.url])
                print(self.result)
                if len(self.result)==0:
                    if len(name)>20:
                        name=name[:19]+"..."
                    self.linkname.append(name)
                    self.iimage=video.getbestthumb()
                    self.imageFromWeb=video.getbestthumb() +".jpg"
                    print(self.imageFromWeb)
                    self.imagelink.append(self.iimage)

                    self.db.insert("videolist",["numfromplaylist","listlink","linkname","imagelink","videotime"],[self.listnum,self.url,name,self.imageFromWeb,videoTime])
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
            self.db.delete("videolist",["num"],[self.result[index][0]])
            self.ui.resultDialog("삭제 성공했습니다.")
            self.VideoListPrint()
        
        elif self.ui.retval == QtWidgets.QMessageBox.Cancel:
            self.ui.resultDialog("삭제하지 않습니다.")


    def setVideo(self,index):
        
        self.result=self.db.read("videolist",["numfromplaylist"],[self.listnum])
        url=self.result[index][2]
        time=self.result[index][5]
        print(url)

        try:
            video=pafy.new(url)
        except:
            pass
        #최고의 해상도
        best = video.getbest()
        videourl = best.url

        vlcInstance = vlc.Instance()
        self.player = vlcInstance.media_player_new()
        Media = vlcInstance.media_new(videourl)
        #get_mrl -> mp4
        Media.get_mrl()
        self.player.set_media(Media)
        #videoplay frame/label set
        self.player.set_hwnd(self.ui.videoPlay.winId())
        self.referVideoPlay=VideoPlay.VideoPlay(self.player,time,index)
        self.referVideoPlay.start()

    

