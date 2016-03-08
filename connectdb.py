
import pymysql as pmsql
import numpy as np


class datafromDB(object):
    def __init__ (self,DBHOSE,PORT,USER,PW) :
        self.DBHOST = DBHOSE
        self.PORT = PORT
        self.USER = USER
        self.PW = PW

    def connectDB(self):
        try:
            conn = pmsql.connect(host=self.DBHOST,port=self.PORT,user=self.USER,passwd=self.PW)
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

def main():
    DBHOST='10.1.70.113'
    PORT = 3306
    USER = 'jplee031107'
    PW = '$kpc1004'

    conn = pmsql.connect(host=DBHOST,port=PORT,user=USER,passwd=PW)
    cur =conn.cursor()

    # select database named 'LPS'
    cur.execute("USE LPS")
    # select quaterly and yearly datas from the table 'LPS212' after 2008
    sql = "SELECT YEAR,MQ,MM_INPUT FROM LPS212 WHERE MQ>=14 AND KISC_CODE=%s;"

    cur.execute(sql % "'TT_AOU'" )

    mmList=[]
    for row in cur:
        tempList=[]
        for column in row:
            # print (column, "Int?:", isInt(column),",  Float?:", isFloat(column))
            if not isInt(column) and not isFloat(column): #TT_AOU
                #tempList.append(column)
                pass
            elif not isInt(column) and isFloat(column): #
                tempList.append(float(column))
            elif isInt(column) and not isFloat(column):
                tempList.append(int(column))
        mmList.append(tempList)
    mmList=mmList[:][0:1]
    print(mmList)
    mmArr =np.array(mmList[0])
    print (mmArr)

    # print (type((mmArr[0][3])))
    # print (len((mmArr)))
    # print (len((mmArr[0])))


if __name__ == '__main__':
    main()
