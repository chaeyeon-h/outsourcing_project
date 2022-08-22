from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import DataBase
import MainUi,JoinPage, FindPage, PlayListPage

class LoginPage:
    def __init__(self):
        self.db=DataBase.DataBase()
        self.ui=MainUi.MainUi()

        for index in range(0, len(self.ui.LoginPageBtnList)):
            self.ui.LoginPageBtnList[index].mousePressEvent=lambda event, nowIndex=index : self.clickEvent(nowIndex)
        
    def clickEvent(self,index):
        if index==0:
            self.login()
        elif index==1:  
            self.referJoinPage=JoinPage.JoinPage(self.ui)
            self.ui.stackedWidget.setCurrentWidget(self.ui.JoinPage)
        elif index==2:
            self.referFindPage=FindPage.FindPage(self.ui)
            self.ui.stackedWidget.setCurrentWidget(self.ui.FindPage)
        self.textClear()
    
    def login(self): 
        info=[]
        for index in range(0, len(self.ui.LoginPageEditList)):
            text=self.ui.LoginPageEditList[index].text()
            info.append(text)

        result=self.db.read("user",["id","pw"],info)

        if len(result)!=0:
            self.referPlayListPage=PlayListPage.PlayListPage(self.ui,info[0])
            self.ui.stackedWidget.setCurrentWidget(self.ui.PlayListPage)
        else:   
            self.ui.resultDialog("로그인 실패")


    def textClear(self):
        for index in range(0, len(self.ui.LoginPageEditList)):
            self.ui.LoginPageEditList[index].clear()

#####################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    loginPage=LoginPage() 
    sys.exit(app.exec_())
 