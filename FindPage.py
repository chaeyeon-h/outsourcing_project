from PyQt5 import QtCore, QtGui, QtWidgets
import DataBase

class FindPage:
    def __init__(self,ui):
        self.db=DataBase.DataBase()
        self.ui=ui
        self.info=[]        
        
        for index in range(0, len(self.ui.FindPageBtnList)):
            self.ui.FindPageBtnList[index].clicked.connect(lambda event, nowIndex=index : self.clickEvent(nowIndex))

    def clickEvent(self,index):
        if index==0:
            self.findId()
        elif index==1:
            self.findPw()
            self.ui.messageBox( "정말로 찾겠습니까",["예","아니요"])
        elif index==2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)
            # self.ui.FindPageBtnList[index].clicked.disconnect()

    def findId(self):
        for i in range(0,len(self.ui.FindIdPageLabelNameList)):
            text=self.ui.FindIdPageEditList[i].text() 
            self.info.append(text)

        result=self.db.read("user",["name","contact"],[self.info[0],self.info[1]])

        if len(result)!=0:
            text="아이디는\n"+result[0][1]+"입니다."
            self.ui.resultDialog(text)
        else:
            text="없는 정보입니다."
            self.ui.resultDialog(text)

        self.textClear(self.ui.FindIdPageEditList)

    def findPw(self):
        for i in range(0,len(self.ui.FindPwPageLabelNameList)):
            text=self.ui.FindPwPageEditList[i].text() 
            self.info.append(text)
        result=self.db.read("user",["name","contact","id"],[self.info[0],self.info[1],self.info[2]])
        if len(result)!=0:
            text="비밀번호는\n"+result[0][2]+"입니다."
            self.ui.resultDialog(text)
        else:
            text="없는 정보입니다."
            self.ui.resultDialog(text)

        self.textClear(self.ui.FindPwPageEditList)
        
    def textClear(self,list):
        List=list
        for index in range(0, len(List)):
            List[index].setText("")
        self.info=[]
