import threading
import vlc
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from json import load
from itsdangerous import exc
import pafy

class VideoPlay(QThread):
    signal = pyqtSignal(int)  
    def __init__(self,ui,url):
        super().__init__()


        self.url=url
        self.ui=ui
        self.run()

    def run(self):
        try:
            video=pafy.new(self.url)
        except:
            pass
        
        #최고의 해상도
        best = video.getbest()
        url = best.url

        vlcInstance = vlc.Instance()
        self.player = vlcInstance.media_player_new()
        Media = vlcInstance.media_new(url)
        #get_mrl -> mp4
        Media.get_mrl()
        self.player.set_media(Media)
        #videoplay frame/label set
        self.player.set_hwnd(self.ui.videoPlay.winId())
        self.player.play()
        


    def PlayStopVideo(self,index):
        #비디오 일시정지, 재생, 멈춤 기능
        if index==0:
            if self.player.is_playing()==False:
                self.player.play()

        elif index==1:
            self.player.stop()
        
        elif index==2:
            if self.player.is_playing():
                self.player.pause()

  
    
    