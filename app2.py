import gradio as gr
from src.postbycitizen import get_LC

# def get_max_eng(likesCount, commentsCount, shareCount):
#     lc_instance = get_LC()
#     max_eng = lc_instance.max_engagments(likesCount, commentsCount, shareCount)
#     return [max_eng]  # Return a list of tuples

# def fetch_data():
#     lc_instance = get_LC()
#     likesCount, commentsCount, shareCount = lc_instance.get_user_data()
#     return likesCount, commentsCount, shareCount

# likesCount, commentsCount, shareCount = fetch_data()

# iface = gr.Interface(
#     fn=get_max_eng,
#     inputs=[
#         gr.inputs.Dropdown(choices=likesCount, label="Likes Count"),
#         gr.inputs.Dropdown(choices=commentsCount, label="Comments Count"),
#         gr.inputs.Dropdown(choices=shareCount, label="Share Count")
#     ],
#     outputs=gr.outputs.Textbox(type="auto", label="Max Engagement"),
#     title="Max Engagement Calculator",
#     description="Select from available options to calculate max engagement."
# )
# iface.launch()


# ''''''
# lc_instance = get_LC()

# likesCount, commentsCount, shareCount = lc_instance.get_user_data() 
    
# max_eng =  lc_instance.max_engagments(likesCount,commentsCount,shareCount)

# print(list(max_eng))


import gradio as gr
from src.postbycitizen import get_LC

lc_instance = get_LC()
likesCount, commentsCount, shareCount = lc_instance.get_user_data()
max_eng = lc_instance.max_engagments(likesCount, commentsCount, shareCount)
##############max_eng is tuple
table_data = {"Rank": [], "ID": [], "Citizen ID": [], "Likes": [], "Comments": [], "Shares": [], "Total Engagement": []}
print(type(table_data))
################ table_data is dict
for idx, data in enumerate(max_eng, 1):
    table_data["Rank"].append(1)
    # table_data["ID"].append(data[0])
    # table_data["Citizen ID"].append(data[1])
    # table_data["Likes"].append(data[0])
    # table_data["Comments"].append(data[1])
    # table_data["Shares"].append(data[2])
    # table_data["Total Engagement"].append(data[3])

iface = gr.Interface(
    fn=lambda: table_data,
    inputs=[],
    outputs=gr.outputs.Table(),
    title="Max Engagements",
    description="Top engagements in a table format.",
    live=False  # To prevent displaying the interface while launching the script
)
iface.launch()











