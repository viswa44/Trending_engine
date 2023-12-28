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
            cur.execute('SELECT "likesCount", "commentsCount","shareCount" FROM post_by_leaders')
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
        filtered_likes = [like for like in likesCount if like is not None]

        max_likes = max(filtered_likes)
        
        return max_likes
    def findmax_comments(self,commentsCount):
        filtered_comments = [ comment for comment in commentsCount if comment is not None]
        max_comments = max(filtered_comments)
        
        return max_comments
    def findmax_shares(self,shareCount):
        filtered_shares = [ share for share in shareCount if share is not None]
        max_shares = max(filtered_shares)
        
        return max_shares
    
    
    def findmax_likes_id(self,likesCount):
        max_likes_id_no = pd.Series(likesCount).idxmax()
        if self.conn:
            cur = self.conn.cursor()
            cur.execute('''
                        SELECT "leaderId" 
                        FROM post_by_leaders
                        WHERE "likesCount" = (SELECT MAX("likesCount") FROM post_by_leaders)
            ''')
            rows = cur.fetchall()
            for row in rows:
                print(f"Liked leader ID: {row[0]}")
            
            cur.close()
            
        return max_likes_id_no
    
    def findmax_comments_id(self,commentsCount):
        max_comments_id_no = pd.Series(commentsCount).idxmax()
        if self.conn:
            cur = self.conn.cursor()
            cur.execute('''
                        SELECT "leaderId" 
                        FROM post_by_leaders
                        WHERE "likesCount" = (SELECT MAX("commentsCount") FROM post_by_leaders)
            ''')
            rows = cur.fetchall()
            for row in rows:
                print(f"Commented leader ID: {row[0]}")
            
            cur.close()

        
        return max_comments_id_no
    
    
    
    def findmax_shares_id(self,shareCount):
        max_shares_id_no = pd.Series(shareCount).idxmax()
        if self.conn:
            cur = self.conn.cursor()
            cur.execute('''
                        SELECT "leaderId" 
                        FROM post_by_leaders
                        WHERE "likesCount" = (SELECT MAX("shareCount") FROM post_by_leaders)
            ''')
            rows = cur.fetchall()
            for row in rows:
                print(f"shared leader ID: {row[0]}")
            
            cur.close()
        return max_shares_id_no
    
    def max_engagments(self,likesCount,commentsCount,shareCount):
        if self.conn:
            
            
            cur = self.conn.cursor()
            cur.execute('''
                        SELECT 
                            "id", "leaderId", 
                            COALESCE("likesCount", 0) AS "likesCount",
                            COALESCE("commentsCount", 0) AS "commentsCount",
                            COALESCE("shareCount", 0) AS "shareCount",
                            ("likesCount" + "commentsCount" + "shareCount") AS totalengagment
                        FROM post_by_leaders
                        ORDER BY totalengagment DESC
                        LIMIT 10
                    ''')
            # id,citizenid,totalengagemnt = cur.fetchall()
            rows = cur.fetchall()
            #print(rows)
            if rows :
                for idx, rows in enumerate(rows, 1):
                    id, leader_id,likes,comments,shares,total_engagement = rows
                    if total_engagement is not None: 
                        print(f"Rank {idx}: ID: {id}, Leader ID: {leader_id},likes:{likes},comments:{comments},shares:{shares} Total Engagement: {total_engagement}")
                    else:
                        print("like is none")
            else:
                print("No data found")

            cur.close()
        else:
            print("No database connection")
    
    
    
    
if __name__ =="__main__":
    lc_instance = get_LC()
    likesCount, commentsCount, shareCount = lc_instance.get_user_data() 
    max_eng =  lc_instance.max_engagments(likesCount,commentsCount,shareCount)

    
    

    
    # max_index = pd.Series(likesCount).idxmax()
    # print("Maximum Index position:",max_index) 

    # # print(commentsCount)
    # max_likes_id= lc_instance.findmax_likes()
    # print(max_likes_id)
    # # print(likes_count)

    
