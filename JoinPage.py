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
        print(self.resultId)
        print(len(self.resultId))
        if len(self.resultId)!=0:
            text="이미 사용중인 아이디"
            self.ui.resultDialog(text)
        elif 4>len(id) or 15<len(id):
            text="아이디는 4~15자리여야합니다"
            self.ui.resultDialog(text)
        else:
            text="사용가능한 아이디"
            self.check=1
            self.ui.resultDialog(text)
    
    def infoCheck(self):
        if self.check==1:
            for i in range(0,len(self.ui.JoinPageEditList)):
                text=self.ui.JoinPageEditList[i].text()
                self.info.append(text)
            result=self.db.read("user",["name","contact"],[self.info[2],self.info[3]])
            # print(result,self.info[2],self.info[3])
            print(self.info)
            if len(result)==0:
                if  8<=len(self.info[1])<=20 and 2<=len(self.info[2])<=5 and 10<=len(self.info[3])<=11:
                    self.db.insert("user",["id","pw","name","contact"],self.info)
                    text="회원가입 성공 \n-> 로그인 하세요"
                    self.ui.resultDialog(text)
                    self.textClear() 
                    self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

                else:
                    text="아이디는 4-15자리\n비번은 8-20자리\n이름은 2-5자리\n연락처는 10-11자리"
                    self.ui.resultDialog(text)
                    self.info=[]
                    						
            elif len(result)!=0:
                text="존재하는 회원정보 입니다."
                self.ui.resultDialog(text)
        
            print(self.info)

        else:
            text= "아이디 중복체크를 완료해주세요"
            self.ui.resultDialog(text)
        
        


    def textClear(self):
        for i in range(0, len(self.ui.JoinPageEditList)):
            self.ui.JoinPageEditList[i].setText("")
