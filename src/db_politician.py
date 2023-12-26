import psycopg2
import jsonify

import sys

class get_LC():
    
    def __init__(self):
        pass
    
    def connect_to_db(self):
    
    
        try:

            conn = psycopg2.connect(database="nxtgovtestdb",
                                    host="database-nxtgov.cidtw9qpn6wx.ap-south-1.rds.amazonaws.com",
                                    user="postgres",
                                    password="!pSKPdJ3awx*9J9Xq",
                                    port="5432")
            
            print("database connected successfully")
        except:
            print("db not connected..try hard boy")

        def get_user_data(self):
            if not self.conn:
                self.connect_to_db()

            cur = conn.cursor()
            cur.execute('select "likesCount","commentsCount"  from post_by_citizens ')
            commentsCount= []
            likesCount=[]

            for row in cur.fetchall():
                commentsCount.append(row[0])
                likesCount.append(row[1])

            cur.close()
        
            return commentsCount,likesCount 

    def findmax_likes(self):
        if self.conn:
            self.connect_to_db()

        cur = self.conn.cursor()
        cur.execute("SELECT ID FROM your_table ORDER BY LikesCount DESC LIMIT 1")
        max_likes_ids = cur.fetchone()[0]
        print(f"ID with maximum likes: {max_likes_id}")
        
        cur.close()

        return max_likes_ids
        
    
    
    
if __name__ =="__main__":
    lc_instance = get_LC() 
    max_likes_id = lc_instance.findmax_likes()
    print(max_likes_id)

    
