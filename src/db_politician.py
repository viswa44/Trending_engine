import psycopg2
import jsonify
import pandas as pd
import sys

class get_LC():
    
    def __init__(self):
        self.conn = None
        self.connect_to_db()  # Establish connection upon initialization
    
    
    def connect_to_db(self):
    
    
        try:

            self.conn = psycopg2.connect(database="nxtgovtestdb",
                                    host="database-nxtgov.cidtw9qpn6wx.ap-south-1.rds.amazonaws.com",
                                    user="postgres",
                                    password="!pSKPdJ3awx*9J9Xq",
                                    port="5432")
            
            print("database connected successfully")
        except Exception as e:
            self.conn = None
            print(f"DB connection error: {str(e)}")

    def get_user_data(self):

        if self.conn:
            cur = self.conn.cursor()
            cur.execute('SELECT "likesCount", "commentsCount" FROM post_by_citizens')
            commentsCount = []
            likesCount = []

            for row in cur.fetchall():
                likesCount.append(row[0])
                commentsCount.append(row[1])

            cur.close()
            return likesCount, commentsCount
        else:
            print("No database connection")
            return [], []



    def findmax_likes(self):

        if self.conn:
            cur = self.conn.cursor()
            cur.execute('SELECT "id","likesCount" FROM post_by_citizens ORDER BY "likesCount" DESC LIMIT 1')
            max_likes_id,likes_count = cur.fetchone()

            if max_likes_id:
                print(f"ID with maximum likes: {max_likes_id[0]}")
                # print(f"likes count:{likes_count[0]}")
            else:
                print("No data found")      

            cur.close()
            return max_likes_id
        
        else:
            print("No database connection")
            return []
    
    
    
if __name__ =="__main__":
    lc_instance = get_LC()
    likesCount, commentsCount = lc_instance.get_user_data()
    print("maxlikes",max(likesCount))
    
    
    max_index = pd.Series(likesCount).idxmax()
    print("Maximum Index position:",max_index) 

    # # print(commentsCount)
    # max_likes_id= lc_instance.findmax_likes()
    # print(max_likes_id)
    # # print(likes_count)

    
