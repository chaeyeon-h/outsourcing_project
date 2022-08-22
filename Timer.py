import threading
import vlc
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
import  time
from itsdangerous import exc
import pafy
import VideoListPage

class Timer(QThread):

    time = pyqtSignal(int) 

    def __init__(self,sec,index):
        super().__init__()
        self.index=index
        self.timerSec=sec
        self.presentTime=0
        self.setTimer=True
        self.stop=False

    def run(self):
        while self.setTimer==True:
            if self.stop!=True:
                self.time.emit(self.presentTime)
                time.sleep(1)
                self.presentTime+=1
            if self.timerSec<=self.presentTime:
                self.setTimer=False
                self.index+=1
                self.referVideoListPage=VideoListPage.VideoListPage.setVideo(self.index)
                
        
    def timerStart(self): 
        self.setTimer=False
        self.presentTime=0

    def timerStop(self):
       self.stop=True
    
    def timerRestart(self):
       self.stop=False
  