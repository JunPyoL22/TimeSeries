import pymysql as pmsql
import numpy as np

class datafromDB(object):
    def __init__ (self,DBHOSE,PORT,USER,PW,SERVER) :
        self.DBHOST = DBHOSE
        self.PORT = PORT
        self.USER = USER
        self.PW = PW
        self.DB=DB

    def connectDB(self):
        try:
            conn = pmsql.connect(host=self.DBHOST,port=self.PORT,user=self.USER,passwd=self.PW,db=self.DB)
        except Exception as e:
            print(e)
        else:
            cur = conn.cursor()
            return cur

    def getDataList(self, sql):
        result = []
        data = self.connectDB().execute(sql)
        for row in data:
            tempList=[]
            for column in row:
                # print (column, "Int?:", isInt(column),",  Float?:", isFloat(column))
                if not isInt(column) and not isFloat(column): #TT_AOU
                     #tempList.append(column)
                     pass
                elif not isInt(column) and isFloat(column):
                    tempList.append(float(column))
                elif isInt(column) and not isFloat(column):
                    tempList.append(int(column))
            result.append(list(row))
        return result

    def getDataArray(self, sql):
        return np.array(self.getDataList(sql))

def isInt(x):
    try:
        if type(int(x))==int:
            return True
    except Exception:
        return False
    else:
        return False

def isFloat(x):
    try:
        if type(float(x))==float and not isInt(x):
            return True
    except Exception:
        return False
    else:
        return False
