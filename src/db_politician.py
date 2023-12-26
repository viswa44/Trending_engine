import psycopg2
import jsonify

import sys

class get_LC():
    def __init__(self):
        pass
    
    
    def get_user_data(self):
    
        try:

            conn = psycopg2.connect(database="nxtgovtestdb",
                                    host="database-nxtgov.cidtw9qpn6wx.ap-south-1.rds.amazonaws.com",
                                    user="postgres",
                                    password="!pSKPdJ3awx*9J9Xq",
                                    port="5432")
            print("database connected successfully")
        except:
            print("db not connected..try hard boy")

        cur = conn.cursor()
        return cur
        # cur.execute('select "likesCount","commentsCount"  from post_by_citizens ')
        # commentsCount= []
        # likesCount=[]

        # for row in cur.fetchall():
        #     commentsCount.append(row[0])
        #     likesCount.append(row[1])

        # cur.close()
        # conn.close()
        # return commentsCount,likesCount 

if __name__ =="__main__":
    lc_instance = get_LC() 
    cur = lc_instance.get_user_data()

    
