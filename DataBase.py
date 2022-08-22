import sqlite3
# pk = 하나의 열을 기본키로 선택 -> null이 아니게끔 해준다 , 모든 row를 통틀어서 하나의 값만 있어야함 (유일한 값)
# fk = 메모리를 절약할 수 있다. ..   원본이 한개라서 값을 바꾸면 한번에 바뀐.다
class DataBase:
    def __init__(self):

        #여러개의 db는 하나의 cursor와 connect 사용 가능

        self.connect1=sqlite3.connect("UserData.db")
        self.cursor1=self.connect1.cursor()
        self.cursor1.execute("CREATE TABLE IF NOT EXISTS user ( num INTEGER PRIMARY KEY, id TEXT , pw TEXT, name TEXT, contact TEXT )")
        self.cursor1.execute("CREATE TABLE IF NOT EXISTS playlist ( num INTEGER PRIMARY KEY, id TEXT, listname TEXT )")
        # num을 foriegn key로 받으면 id 필요없음 왜냐면 pk 값 안겹치니까 < ex) id=>123 인사람이 1을 가져감 id=> 234 인 사람이 2를 가져감 >
        self.cursor1.execute("CREATE TABLE IF NOT EXISTS videolist ( num INTEGER PRIMARY KEY, numfromplaylist TEXT, listlink TEXT, linkname TEXT, imagelink TEXT, videotime INTEGER, FOREIGN KEY (numfromplaylist) REFERENCES user (num) )")

###########################################################################################

    def insert(self,tableName,column,values):
        ment="INSERT INTO "+ tableName +" (" 
        for i in range(0,len(column)):
            ment+=column[i]
            if i!=len(values)-1:
                ment+=", "
        ment+=") VALUES("
        for i in range(0,len(values)):
            ment+="?"
            if i!=len(values)-1:
                ment+=", "
        ment+=")"
        self.cursor1.execute(ment,values)
        self.connect1.commit()
   
###########################################################################################
  
    def read(self,tableName,column,values):
        ment="SELECT * FROM "+ tableName + " WHERE " 
        for i in range(0,len(column)):
            ment+=column[i]+"=?"
            if i!=len(column)-1:
                ment+=" AND "
        self.cursor1.execute(ment,values)
        result= self.cursor1.fetchall()
        return result

###########################################################################################

    def update(self,tableName,column1,column2,values):
        value=[] 
        ment="UPDATE "+tableName+" SET "
        for i in range(0,len(column1)):
            ment+=column1[i]+"=? "
            if i!=len(column1)-1:
                ment+=", "

        ment+="WHERE "
        for i in range(0,len(column2)):
            ment+=column2[i]+"=?"
            if i!=len(column2)-1:
                ment+=" AND "
        
        print(ment)
        self.cursor1.execute(ment,values)
        self.connect1.commit()

###########################################################################################

    def delete(self,tableName,column,values): 
        ment="DELETE FROM " + tableName+" WHERE "
        for i in range(0,len(column)):
            ment+=str(column[i])+"= '"+str(values[i])+"'"
            if i!=len(column)-1:
                ment+=" AND "

        print(ment)
        self.cursor1.execute(ment)
        self.connect1.commit()