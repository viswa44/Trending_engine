import psycopg2
import jsonify
import pandas as pd
import sys
import uuid

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
            cur.execute('SELECT "likesCount", "commentsCount","shareCount" FROM post_by_citizens')
            commentsCount = []
            likesCount = []
            shareCount =[]

            for row in cur.fetchall():
                likesCount.append(row[0])
                commentsCount.append(row[1])
                shareCount.append(row[2])

            cur.close()
            return likesCount, commentsCount, shareCount
        else:
            print("No database connection")
            return [], [], []


    '''
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
        
        
        SELECT column_name
        FROM table_name
        WHERE ID_column = your_desired_ID;
    '''      
    def findmax_likes(self,likesCount):
        max_likes = max(likesCount)
        
        return max_likes
    def findmax_comments(self,commentsCount):
        max_comments = max(commentsCount)
        
        return max_comments
    def findmax_shares(self,shareCount):
        max_shares = max(shareCount)
        
        return max_shares
    
    
    def findmax_likes_id(self,likesCount):
        max_likes_id_no = pd.Series(likesCount).idxmax()
        if self.conn:
            cur = self.conn.cursor()
            cur.execute('''
                        SELECT "citizenId" 
                        FROM post_by_citizens
                        WHERE "likesCount" = (SELECT MAX("likesCount") FROM post_by_citizens)
            ''')
            rows = cur.fetchall()
            for row in rows:
                print(f"Liked Citizen ID: {row[0]}")
            
            cur.close()
            
        return max_likes_id_no
    
    def findmax_comments_id(self,commentsCount):
        max_comments_id_no = pd.Series(commentsCount).idxmax()
        if self.conn:
            cur = self.conn.cursor()
            cur.execute('''
                        SELECT "citizenId" 
                        FROM post_by_citizens
                        WHERE "likesCount" = (SELECT MAX("commentsCount") FROM post_by_citizens)
            ''')
            rows = cur.fetchall()
            for row in rows:
                print(f"Commented Citizen ID: {row[0]}")
            
            cur.close()

        
        return max_comments_id_no
    
    
    
    def findmax_shares_id(self,shareCount):
        max_shares_id_no = pd.Series(shareCount).idxmax()
        if max_shares_id_no > 0:
            if self.conn:
                cur = self.conn.cursor()
                cur.execute('''
                            SELECT "citizenId" 
                            FROM post_by_citizens
                            WHERE "likesCount" = (SELECT MAX("shareCount") FROM post_by_citizens)
                ''')
                rows = cur.fetchall()
                for row in rows:
                    print(f"shared Citizen ID: {row[0]}")
                
                cur.close()
            return max_shares_id_no
        else:
             return "No share count"
    
    
    
if __name__ =="__main__":
    lc_instance = get_LC()
    likesCount, commentsCount, shareCount = lc_instance.get_user_data() 
    
    max_likes = lc_instance.findmax_likes(likesCount)
    max_comments = lc_instance.findmax_comments(commentsCount)
    max_shares = lc_instance.findmax_shares(shareCount)
    
    max_likes_id = lc_instance.findmax_likes_id(likesCount)
    max_comments_id = lc_instance.findmax_comments_id(commentsCount)
    max_shares_id = lc_instance.findmax_shares_id(shareCount)
    
    print("max likes of all post",max_likes)
    print("max comments of all post",max_comments)
    print("max shares of all posts",max_shares)

    print("max likes - ID",max_likes_id)
    print("max comments - ID",max_comments_id)
    print("max shares - ID",max_shares_id)
    
    # max_index = pd.Series(likesCount).idxmax()
    # print("Maximum Index position:",max_index) 

    # # print(commentsCount)
    # max_likes_id= lc_instance.findmax_likes()
    # print(max_likes_id)
    # # print(likes_count)

    
