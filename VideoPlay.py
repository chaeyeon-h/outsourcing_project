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

class VideoPlay(threading.Thread):
    def __init__(self,ui,url):
        threading.Thread.__init__(self)

        self.url=url
        self.ui=ui
        self.run()

    def run(self):
        try:
            video=pafy.new(self.url)
        except:
            pass    

    def PlayStopVideo(self,index):
        #비디오 일시정지, 재생, 멈춤 기능
        if index==0:
            if self.video.is_playing()==False:
                self.video.play()

        elif index==1:
            self.video.stop()
        
        elif index==2:
            if self.video.is_playing():
                self.video.pause()

  
