import sqlite3
# pk = 하나의 열을 기본키로 선택 -> null이 아니게끔 해준다 , 모든 row를 통틀어서 하나의 값만 있어야함 (유일한 값)
# fk = 메모리를 절약할 수 있다. ..   원본이 한개라서 값을 바꾸면 한번에 바뀐.다
class DataBase:
    def __init__(self):

        #여러개의 db는 하나의 cursor와 connect 사용 가능

        self.connect1=sqlite3.connect("UserData.db")
        self.cursor1=self.connect1.cursor()
        self.cursor1.execute("CREATE TABLE IF NOT EXISTS user ( INTEGER PRIMARY KEY, id TEXT , pw TEXT, name TEXT, contact TEXT)")
        self.cursor1.execute("CREATE TABLE IF NOT EXISTS playlist ( INTEGER PRIMARY KEY, id TEXT, PLAYLIST TEXT  )")
        self.cursor1.execute("CREATE TABLE IF NOT EXISTS videolist ( INTEGER PRIMARY KEY, id TEXT, VIDEOLIST TEXT  )")

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

    def update(self,tableName,column,values):
        value=[] 
        ment="UPDATE "+tableName+" SET "
        for i in range(1,len(column)):
            ment+=column[i]+"=?"
            if i!=len(column)-1:
                ment+=", "
            value.append(values[i])
      
        ment+= " WHERE "+ column[0]+"= '"+ values[0] +"'"
        self.cursor1.execute(ment,value)
        self.connect1.commit()

###########################################################################################

    def delete(self,tableName,column,values): 
        ment="DELETE FROM "
        ment+=tableName+" WHERE "+str(column)+"="+str(values)+";"
        print(ment)
        self.cursor1.execute(ment)
        self.connect1.commit()