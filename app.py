import gradio as gr
import psycopg2
from src.postbycitizen import get_LC


lc_instance = get_LC()
likesCount, commentsCount, shareCount = lc_instance.get_user_data()
rows1 = lc_instance.max_engagments(likesCount, commentsCount, shareCount)
############## rows is tuple
formatted_data = []

conn = psycopg2.connect(database="nxtgovtestdb",
                                    host="database-nxtgov.cidtw9qpn6wx.ap-south-1.rds.amazonaws.com",
                                    user="postgres",
                                    password="!pSKPdJ3awx*9J9Xq",
                                    port="5432")
cur = conn.cursor()
cur.execute('''
                        SELECT "id","citizenId","likesCount","commentsCount","shareCount",("likesCount"+"commentsCount"+"shareCount") AS totalengagment
                        FROM post_by_citizens
                        ORDER BY totalengagment DESC
                        LIMIT 10
                        ''')
rows = cur.fetchall()







if rows:
    for idx, rows in enumerate(rows, 1):
        
        id,citizen_id,likes,comments,shares,total_engagement = rows
        
        if total_engagement is not None:
            formatted_row = f"Rank {idx}: ID: {id}, Citizen ID: {citizen_id},likes:{likes},comments:{comments},shares:{shares} Total Engagement: {total_engagement}"
            formatted_data.append(formatted_row)
        else:
            print("check values your are passsing")
        
print(type(formatted_data))


iface = gr.Interface(
    fn=lambda: {"Table": "\n".join(formatted_data)},
    inputs=[],
    outputs=gr.outputs.Textbox(label="Table Data"),
    title="Max Engagements",
    description="Top engagements in a table format.",
    live=False  # To prevent displaying the interface while launching the script
)
iface.launch()