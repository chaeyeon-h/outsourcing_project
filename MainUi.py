from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MainUi:
    def __init__(self):

    #MainWindow

        self.MainWindow=QtWidgets.QMainWindow()
        self.MainWindow.resize(1200,900)

        self.centralWidget= QtWidgets.QWidget(self.MainWindow)
        self.centralWidget.setStyleSheet("background-color: white; border-color:red; border-width: 5px;")
        self.centralWidget.resize(1200,900)
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.resize(1200,900)
        
###########################################################################################
    #LoginPage

        self.LoginPage = QtWidgets.QWidget()
        self.LoginPage.setObjectName("LoginPage")
        self.LoginPage.resize(1200,900)

        LoginBorder=QtWidgets.QLabel(self.LoginPage)
        LoginBorder.setGeometry(10,10,1180,880)
        LoginBorder.setStyleSheet("background-color: white ;border-style:solid; border-color: red; border-width: 3px;")
#########
        #0 : idEdit, 1: pwEdit
        LoginPageTextList=["id","pw"]
        for index in range(0,len(LoginPageTextList)):
            LoginPageLogo = QtWidgets.QLabel(self.LoginPage)
            LoginPageLogo.setGeometry(280,460+(index*60),100,40)
            LoginPageLogo.setText(LoginPageTextList[index])
            font = QtGui.QFont()
            font.setFamily("HY 견고딕")
            font.setPixelSize(12)
            LoginPageLogo.setFont(font)
            
        self.LoginPageEditList=[]
        for index in range(0,2):
            LoginPageEdit= QtWidgets.QLineEdit(self.LoginPage)
            LoginPageEdit.setGeometry(380,460+(index*60),450,40)
            LoginPageEdit.setStyleSheet("border: 1.25px solid red;")
            self.LoginPageEditList.append(LoginPageEdit)
            if index==1:
                self.LoginPageEditList[index].setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
#########
        self.LoginPageBtnNameList=["로그인","회원가입","아이디/비밀번호 찾기"]
        self.LoginPageBtnList=[]
        for index in range(0,len(self.LoginPageBtnNameList)):
            LoginPageBtn= QtWidgets.QPushButton(self.LoginPage)
            LoginPageBtn.setGeometry(QtCore.QRect(400,610+(index*60),380,40))
            LoginPageBtn.setStyleSheet("background-color: #FFD5D5; ")
            font = QtGui.QFont()            
            font.setFamily("HY 견고딕")
            LoginPageBtn.setFont(font)
            LoginPageBtn.setText(self.LoginPageBtnNameList[index])
            LoginPageBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.LoginPageBtnList.append(LoginPageBtn)
#########
        LoginPageLogo = QtWidgets.QLabel(self.LoginPage)
        LoginPageLogo.setGeometry(QtCore.QRect(490, 140, 200, 200))
        font = QtGui.QFont()
        font.setPixelSize(200) 
        LoginPageLogo.setFont(font)
        LoginPageLogo.setText("▶")
        LoginPageLogo.setStyleSheet("color:red;")
        
        self.stackedWidget.addWidget(self.LoginPage)

###################################################################################################################

#joinPage
        self.JoinPage = QtWidgets.QWidget()
        self.JoinPage.setObjectName("JoinPage")
        self.JoinPage.resize(1200,900)

        JoinBorder=QtWidgets.QLabel(self.JoinPage)
        JoinBorder.setGeometry(10,10,1180,880)
        JoinBorder.setStyleSheet("background-color: white ;border-style:solid; border-color: red; border-width: 3px;")
#########
        #0 : idEdit, 1: pwEdit, 2: nameEdit, 3:contactEdit
        self.JoinPageEditList=[]
        for index in range(0,4):
            JoinPageEdit= QtWidgets.QLineEdit(self.JoinPage)
            JoinPageEdit.setGeometry(380,250+(index*100),450,40)
            JoinPageEdit.setStyleSheet("border: 1px solid red; border-radius : 1px;")
            self.JoinPageEditList.append(JoinPageEdit)

        self.JoinPageLabelNameList=["아이디*", "비밀번호*", "이름*", "연락처*"]
        self.JoinPageLabelList=[]
        for index in range(0,4):
            JoinPageLabel= QtWidgets.QLabel(self.JoinPage)
            JoinPageLabel.setGeometry(280,250+(index*100),100,40)
            font = QtGui.QFont()
            font.setPixelSize(13)
            JoinPageLabel.setFont(font)
            JoinPageLabel.setText(self.JoinPageLabelNameList[index])
            self.JoinPageLabelList.append(JoinPageLabel)
#########
        JoinPageJoinBtn = QtWidgets.QPushButton(self.JoinPage)
        JoinPageJoinBtn.setGeometry(QtCore.QRect(400, 710, 400, 40))
        font = QtGui.QFont()
        JoinPageJoinBtn.setStyleSheet("background-color: #FFD5D5; ")
        JoinPageJoinBtn.setFont(font)
        JoinPageJoinBtn.setText("가입")
        JoinPageJoinBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        JoinPageJoinBtn.setObjectName("JoinPageJoinBtn")
        
        JoinPageIdCheckBtn=QtWidgets.QPushButton(self.JoinPage)
        JoinPageIdCheckBtn.setGeometry(QtCore.QRect(780,250,50,40))
        JoinPageIdCheckBtn.setStyleSheet("background-color: red; ")
        font = QtGui.QFont()
        JoinPageIdCheckBtn.setFont(font)
        JoinPageIdCheckBtn.setText("확인")
        JoinPageIdCheckBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        JoinPageBackBtn = QtWidgets.QPushButton(self.JoinPage)
        JoinPageBackBtn.setGeometry(QtCore.QRect(20, 20, 50, 50))
        font = QtGui.QFont()
        font.setPixelSize(30)
        font.setBold(True)
        JoinPageBackBtn.setFont(font)
        JoinPageBackBtn.setStyleSheet("color: red; ")
        JoinPageBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        JoinPageBackBtn.setObjectName("JoinPageBackBtn")
        JoinPageBackBtn.setText("←")

        self.JoinPageBtnList=[JoinPageIdCheckBtn,JoinPageJoinBtn,JoinPageBackBtn]

        
        self.stackedWidget.addWidget(self.JoinPage)

###################################################################################################################

#FindPage

        self.FindPage = QtWidgets.QWidget()
        self.FindPage.setObjectName("FindIdPwPage")
        self.FindPage.resize(1200,900)

        FindIdPwBorder=QtWidgets.QLabel(self.FindPage)
        FindIdPwBorder.setGeometry(10,10,1180,880)
        FindIdPwBorder.setStyleSheet("background-color: white ;border-style:solid; border-color: red; border-width: 3px;")
#########
        self.findId = QtWidgets.QWidget()
        self.findPw = QtWidgets.QWidget()

        self.chooseBoxBtn=QtWidgets.QTabWidget(self.FindPage)
        self.chooseBoxBtn.setGeometry(100,150, 1000, 700)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("나눔고딕")
        self.chooseBoxBtn.setFont(font)

        self.chooseBoxBtn.addTab(self.findId,"id")
        self.chooseBoxBtn.addTab(self.findPw,"pw")
#########
        self.FindIdPageLabelNameList=["이름*", "연락처*"]
        self.FindIdPageLabelList=[]
        self.FindIdPageEditList=[]

        for index in range(0,2):
            FindIdPageLabel= QtWidgets.QLabel(self.findId)
            FindIdPageLabel.setGeometry(200,200+(index*100),100,40)
            font = QtGui.QFont()
            font.setPixelSize(13)
            FindIdPageLabel.setFont(font)
            FindIdPageLabel.setText(self.FindIdPageLabelNameList[index])
            self.FindIdPageLabelList.append(FindIdPageLabel)

            FindIdPageEdit= QtWidgets.QLineEdit(self.findId)
            FindIdPageEdit.setGeometry(300,200+(index*100),450,40)
            FindIdPageEdit.setStyleSheet("border: 1px solid red; border-radius : 1px;")
            self.FindIdPageEditList.append(FindIdPageEdit)
        
        self.FindIdOkBtn=QtWidgets.QPushButton(self.findId)
        self.FindIdOkBtn.setGeometry(270,420,450,40)
        self.FindIdOkBtn.setText("확인")
        font = QtGui.QFont()
        font.setPixelSize(13)
        self.FindIdOkBtn.setStyleSheet("background-color: #FFD5D5; ")
        self.FindIdOkBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#########
        self.FindPwPageLabelNameList=["이름*","연락처*","아이디*"]
        self.FindPwPageLabelList=[]
        self.FindPwPageEditList=[]
        
        for index in range(0,3):

            FindPwPageLabel= QtWidgets.QLabel(self.findPw)
            FindPwPageLabel.setGeometry(200,200+(index*100),100,40)
            font = QtGui.QFont()
            font.setPixelSize(13)
            FindPwPageLabel.setFont(font)
            FindPwPageLabel.setText(self.FindPwPageLabelNameList[index])
            self.FindPwPageLabelList.append(FindPwPageLabel)

            FindPwPageEdit= QtWidgets.QLineEdit(self.findPw)
            FindPwPageEdit.setGeometry(300,200+(index*100),450,40)
            FindPwPageEdit.setStyleSheet("border: 1px solid red; border-radius : 1px;")
            self.FindPwPageEditList.append(FindPwPageEdit)
      
        self.FindPwOkBtn=QtWidgets.QPushButton(self.findPw)
        self.FindPwOkBtn.setGeometry(270,520,450,40)
        self.FindPwOkBtn.setText("확인")
        font = QtGui.QFont()
        font.setPixelSize(13)
        self.FindPwOkBtn.setStyleSheet("background-color: #FFD5D5; ")
        self.FindPwOkBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#########
        self.FindIdPwPageBackBtn = QtWidgets.QPushButton(self.FindPage)
        self.FindIdPwPageBackBtn.setGeometry(QtCore.QRect(20, 20, 50, 50))
        font = QtGui.QFont()
        font.setPixelSize(30)
        font.setBold(True)
        self.FindIdPwPageBackBtn.setFont(font)
        self.FindIdPwPageBackBtn.setStyleSheet("color: red; ")
        self.FindIdPwPageBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FindIdPwPageBackBtn.setObjectName("FindIdPwPageBackBtn")
        self.FindIdPwPageBackBtn.setText("←")

        self.FindPageBtnList=[self.FindIdOkBtn,self.FindPwOkBtn,self.FindIdPwPageBackBtn]

        self.stackedWidget.addWidget(self.FindPage)

###################################################################################################################
# playlistPage    

        self.PlayListPage = QtWidgets.QWidget()
        self.PlayListPage.setObjectName("playListPage")
        self.PlayListPage.resize(1200,900)

        playListBorder=QtWidgets.QLabel(self.PlayListPage)
        playListBorder.setGeometry(10,10,1180,880)
        playListBorder.setStyleSheet("background-color: white ;border-style:solid; border-color: red; border-width: 3px;")
#########
        self.scrollArea = QtWidgets.QScrollArea(self.PlayListPage)
        self.scrollArea.setGeometry(QtCore.QRect(60,60,1080,780))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(60,60,1080,780))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.scrollBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.scrollBox.setGeometry(60,60,1080,780)
        self.scrollBox.setObjectName("scrollBox")

        self.Layout = QtWidgets.QVBoxLayout(self.scrollBox)
        self.Layout.setContentsMargins(10, 10, 135, 300)
        
        self.Layout.setObjectName("verticalLayout")
#########      
        self.PlayListNum=0
        self.PlayPageMoveToVideoList=[]
        self.PlayPageDeleteBtnList=[]
        self.PlayPageChangeBtnList=[]

#playlistnum으로 범위수정해줘야함
        for index in range(0,20):
            PlayListMoveToVideoBtn= QtWidgets.QPushButton(self.scrollBox)
            PlayListMoveToVideoBtn.setStyleSheet("border-style:solid; border-color: red; border-width: 1.25px;")
            PlayListMoveToVideoBtn.setFixedHeight(80)
            font = QtGui.QFont()
            font.setFamily("HY견고딕")
            font.setPixelSize(14)
            PlayListMoveToVideoBtn.setFont(font)
            PlayListMoveToVideoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.PlayPageMoveToVideoList.append(PlayListMoveToVideoBtn)
            self.Layout.addWidget(PlayListMoveToVideoBtn)
        
        for index in range(0,20):
            PlayListChangeBtn= QtWidgets.QPushButton(self.scrollBox)
            PlayListChangeBtn.setGeometry(QtCore.QRect(925,10+(index*86),60,80))

            PlayListDeleteBtn= QtWidgets.QPushButton(self.scrollBox)
            PlayListDeleteBtn.setGeometry(QtCore.QRect(990,10+(index*86),60,80))

            PlayListChangeBtn.setStyleSheet("background-color: red;")
            PlayListDeleteBtn.setStyleSheet("background-color: red;")

            font = QtGui.QFont()
            font.setPixelSize(13)

            PlayListChangeBtn.setFont(font)
            PlayListDeleteBtn.setFont(font)

            PlayListChangeBtn.setText("수정")
            PlayListDeleteBtn.setText("삭제")

            PlayListChangeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            PlayListDeleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            self.PlayPageDeleteBtnList.append(PlayListChangeBtn)
            self.PlayPageChangeBtnList.append(PlayListDeleteBtn)
    
        self.scrollBox.setLayout(self.Layout)
        self.scrollArea.setWidget(self.scrollBox)
#########
        self.playListPageBackBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.playListPageBackBtn.setGeometry(QtCore.QRect(20, 20, 30, 30))
        font = QtGui.QFont()
        font.setPixelSize(20)
        font.setBold(True)
        self.playListPageBackBtn.setFont(font)
        self.playListPageBackBtn.setStyleSheet("color: red; ")
        self.playListPageBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playListPageBackBtn.setObjectName("FindIdPwPageBackBtn")
        self.playListPageBackBtn.setText("←")

        self.playListPageAddBtn= QtWidgets.QPushButton(self.PlayListPage)
        self.playListPageAddBtn.setGeometry(QtCore.QRect(1100, 20, 50, 30))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.playListPageAddBtn.setFont(font)
        self.playListPageAddBtn.setStyleSheet("background-color: red; ")
        self.playListPageAddBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playListPageAddBtn.setText("추가")



        self.stackedWidget.addWidget(self.PlayListPage)

###############################################################################################################################################################
#videoPage

        self.VideoListPage = QtWidgets.QWidget()
        self.VideoListPage.setObjectName("playListPage")
        self.VideoListPage.resize(1200,900)

        VideoListBorder=QtWidgets.QLabel(self.VideoListPage)
        VideoListBorder.setGeometry(10,10,1180,880)
        VideoListBorder.setStyleSheet("background-color: white ;border-style:solid; border-color: red; border-width: 3px;")
#########
        self.scrollArea = QtWidgets.QScrollArea(self.VideoListPage)
        self.scrollArea.setGeometry(QtCore.QRect(60,450,1080,400))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(60,450,1080,400))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.scrollBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.scrollBox.setGeometry(QtCore.QRect(60,450,1080,400))
        self.scrollBox.setObjectName("scrollBox")

        self.Layout = QtWidgets.QVBoxLayout(self.scrollBox)
        self.Layout.setContentsMargins(10, 10, 135, 300)
        
        self.Layout.setObjectName("verticalLayout")
#########      
        self.VideoListNum=0
        self.VideoPageList=[]
        self.VideoPageDeleteBtnList=[]
        self.VideoPageChangeBtnList=[]

#Videolistnum으로 범위수정해줘야함
        for index in range(0,20):
            VideoListMoveToVideoBtn= QtWidgets.QPushButton(self.scrollBox)
            VideoListMoveToVideoBtn.setStyleSheet("border-style:solid; border-color: red; border-width: 1.25px;")
            VideoListMoveToVideoBtn.setFixedHeight(70)
            font = QtGui.QFont()
            font.setPixelSize(14)
            VideoListMoveToVideoBtn.setFont(font)
            VideoListMoveToVideoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.VideoPageList.append(VideoListMoveToVideoBtn)
            self.Layout.addWidget(VideoListMoveToVideoBtn)
        
        for index in range(0,20):
            VideoListChangeBtn= QtWidgets.QPushButton(self.scrollBox)
            VideoListChangeBtn.setGeometry(QtCore.QRect(925,11+(index*76),60,70))

            VideoListDeleteBtn= QtWidgets.QPushButton(self.scrollBox)
            VideoListDeleteBtn.setGeometry(QtCore.QRect(990,11+(index*76),60,70))

            VideoListChangeBtn.setStyleSheet("background-color: red;")
            VideoListDeleteBtn.setStyleSheet("background-color: red;")

            font = QtGui.QFont()
            font.setPixelSize(13)

            VideoListChangeBtn.setFont(font)
            VideoListDeleteBtn.setFont(font)

            VideoListChangeBtn.setText("수정")
            VideoListDeleteBtn.setText("삭제")

            VideoListChangeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            VideoListDeleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            self.VideoPageChangeBtnList.append(VideoListChangeBtn)
            self.VideoPageDeleteBtnList.append(VideoListDeleteBtn)
    
        self.scrollBox.setLayout(self.Layout)
        self.scrollArea.setWidget(self.scrollBox)
#########
#########
        self.VideoListPageBackBtn = QtWidgets.QPushButton(self.VideoListPage)
        self.VideoListPageBackBtn.setGeometry(QtCore.QRect(20, 20, 50, 50))
        font = QtGui.QFont()
        font.setPixelSize(30)
        font.setBold(True)
        self.VideoListPageBackBtn.setFont(font)
        self.VideoListPageBackBtn.setStyleSheet("color: red; ")
        self.VideoListPageBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.VideoListPageBackBtn.setObjectName("FindIdPwPageBackBtn")
        self.VideoListPageBackBtn.setText("←")

        self.VideoPlayBtnNameList=["일시정지","정지","재생"]
        self.VideoPlayBtnList=[]
        for index in range(0,len(self.VideoPlayBtnNameList)):
            VideoBtn= QtWidgets.QPushButton(self.VideoListPage)
            VideoBtn.setGeometry(QtCore.QRect(1050, 140+(index*80), 70, 40))
            VideoBtn.setStyleSheet("background-color:#FF3232")
            font = QtGui.QFont()
            font.setPixelSize(12)
            VideoBtn.setFont(font)
            VideoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            VideoBtn.setText(self.VideoPlayBtnNameList[index])
            self.VideoPlayBtnList.append(VideoBtn)

        self.stackedWidget.addWidget(self.VideoListPage)


###############################################################################################################################################################

        self.MainWindow.setCentralWidget(self.centralWidget)
        self.MainWindow.show()

###################################################################################################################
# Dialog

    def dialog(self,Dialog,text):

        Dialog.setObjectName("Dialog")
        Dialog.resize(600,600)
        Dialog.setStyleSheet("background-color:#FFE7E7; ")

        self.LabelDialog = QtWidgets.QLabel(Dialog)
        self.LabelDialog.setGeometry(QtCore.QRect(100, 100, 400, 400))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("나눔고딕")
        self.LabelDialog.setFont(font)
        self.LabelDialog.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelDialog.setObjectName("LabelDialog")
        self.LabelDialog.setText(text)
    
    def resultDialog(self,text):
        dialog=QtWidgets.QDialog()
        self.dialog(dialog,text)
        dialog.exec()

###################################################################################################################



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui=MainUi() 
    ui.stackedWidget.setCurrentWidget(ui.VideoListPage)
    ui.VideoListPage.show()
    sys.exit(app.exec_())
 


