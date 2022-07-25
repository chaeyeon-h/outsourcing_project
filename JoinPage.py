from PyQt5 import QtCore, QtGui, QtWidgets
import DataBase

class JoinPage:
    def __init__(self,ui):
        self.db=DataBase.DataBase()
        self.ui=ui
        self.check=0

        for index in range(0, len(self.ui.JoinPageBtnList)):
            self.ui.JoinPageBtnList[index].clicked.connect(lambda event, nowIndex=index : self.clickEvent(nowIndex))
            
        self.ui.JoinPageEditList[0].textChanged[str].connect(self.Changed)
    
    def Changed(self):
        self.check=0
        
    def clickEvent(self,index):
        if index==0:
            self.idCheck()
        elif index==1:
            self.infoCheck()
        elif index==2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)
            for index in range(0, len(self.ui.JoinPageBtnList)):
                #disconnect 된건지 확인
                self.ui.JoinPageBtnList[index].clicked.disconnect()
            
    def idCheck(self):

        self.info=[]

        id=self.ui.JoinPageEditList[0].text()
        self.resultId=self.db.read("user",["id"],[id])
        if len(self.resultId)!=0 and len(id)>0:
            text="사용 불가능한 아이디"
            self.ui.resultDialog(text)
        else:
            text="사용가능한 아이디 "
            self.check=1
            self.ui.resultDialog(text)
    
    def infoCheck(self):
        if self.check==1:
            for i in range(0,len(self.ui.JoinPageEditList)):
                text=self.ui.JoinPageEditList[i].text()
                if 0<len(text)<12:
                    print(text)
                    self.info.append(text)

            if len(self.info)==len(self.ui.JoinPageEditList):    
                result=self.db.read("user",["name","contact"],[self.info[2],self.info[3]])
                # print(result,self.info[2],self.info[3])
                if len(result)==0:
                    self.db.insert("user",["id","pw","name","contact"],self.info)
                    text="회원가입 성공 \n-> 로그인 하세요"
                    self.ui.resultDialog(text)
                    self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

                elif len(result)!=0:
                    text="존재하는 회원정보 입니다."
                    self.ui.resultDialog(text)
            else:
                print(self.info)
                text="모든 정보는\n1-11자리여야합니다"
                self.ui.resultDialog(text)
            self.textClear() 
        else:
            text= "아이디 중복체크를 완료해주세요"
            self.ui.resultDialog(text)
        
        


    def textClear(self):
        for i in range(0, len(self.ui.JoinPageEditList)):
            self.ui.JoinPageEditList[i].setText("")
