import threading
import vlc
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
import  time
from itsdangerous import exc
import pafy
import Timer

class VideoPlay(QThread):
    signal = pyqtSignal(int)  
    def __init__(self,playvideo,sec,index):
        super().__init__()
        self.player=playvideo
        self.referTimer=Timer.Timer(sec,index)
        
    def run(self):
        try:
            self.player.play()
            # self.referTimer.start()
        except:
            pass


    def VideoControlEvent(self,index):
        if self.player==None:
                pass
        #비디오 일시정지, 재생, 멈춤 기능
        else:
            if index==0:
                if self.player.is_playing()==False:
                    self.player.play()
                    # self.referTimer.timerStart()

            elif index==1:
                self.player.stop()
                # self.referTimer.timerStop()
            
            elif index==2:
                if self.player.is_playing():
                    self.player.pause()
                    # self.referTimer.timerRestart()

        
        