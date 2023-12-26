import psycopg2
import jsonify
import sys
# from src.db_politician import get_LC()
# from get_LC import get_user_data

conn = psycopg2.connect(database="nxtgovtestdb",
                                    host="database-nxtgov.cidtw9qpn6wx.ap-south-1.rds.amazonaws.com",
                                    user="postgres",
                                    password="!pSKPdJ3awx*9J9Xq",
                                    port="5432")
print("database connected successfully")
            
cur = conn.cursor()
    
cur.execute('select "likesCount","commentsCount"  from post_by_leaders ')
commentsCount_leader= []
likesCount_leader=[]

for row in cur.fetchall():
    commentsCount_leader.append(row[0])
    likesCount_leader.append(row[1])
    
print("commentsCount_leader",commentsCount_leader)
print("likesCount_leader:",likesCount_leader)

cur.close()
conn.close()
# return commentsCount_leader,likesCount_leader



