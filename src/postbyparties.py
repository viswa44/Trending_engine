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
    
cur.execute('select "likesCount","commentsCount"  from post_by_parties ')
commentsCount_parties= []
likesCount_parties=[]

for row in cur.fetchall():
    commentsCount_parties.append(row[0])
    likesCount_parties.append(row[1])
    
print("commentsCount_leader",commentsCount_parties)
print("likesCount_leader:",likesCount_parties)

cur.close()
conn.close()