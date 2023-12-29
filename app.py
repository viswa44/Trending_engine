import gradio as gr

# ... Your data retrieval and processing logic ...

# Assuming your table data is stored in `table_data` as a list of strings
table_data = [
    "Rank 1: ID: 9ac6a428-a99c-4f29-9976-c846a6cb5c58, Citizen ID: 9a21441e-5f6e-44ef-943c-cd057d738d6f,likes:4,comments:6,shares:0 Total Engagement: 10",
    "Rank 1: ID: 9ac6a428-a99c-4f29-9976-c846a6cb5c58, Citizen ID: 9a21441e-5f6e-44ef-943c-cd057d738d6f,likes:4,comments:6,shares:0 Total Engagement: 10",
    "Rank 2: ID: 9ace14f4-ae9c-44ff-a525-34a65d9a18fc, Citizen ID: 9ace0ce0-c252-4fe6-aadf-78e7239e1b5f,likes:3,comments:6,shares:0 Total Engagement: 9",
    "Rank 3: ID: 9ac884c3-270a-42bd-a326-5dd2bd3382f3, Citizen ID: 9a21441e-5f6e-44ef-943c-cd057d738d6f,likes:2,comments:4,shares:0 Total Engagement: 6",
    "Rank 4: ID: 9ac70e68-4074-49a9-8353-9b7e052898aa, Citizen ID: 9ac6f8ea-eac2-4c56-9988-f3e56a1c93ba,likes:3,comments:3,shares:0 Total Engagement: 6",
    "Rank 5: ID: 9af0b44d-781e-478a-8473-be1aa15485f0, Citizen ID: 9ab85762-b70d-4039-96a7-7c75c3809029,likes:3,comments:3,shares:0 Total Engagement: 6",
    "Rank 6: ID: 9ac6a0da-9d47-4652-9e93-f58b266ecdbc, Citizen ID: 9a21441e-5f6e-44ef-943c-cd057d738d6f,likes:3,comments:2,shares:0 Total Engagement: 5",
    "Rank 7: ID: 9ac89e53-09e9-42e0-bc70-8184fa09339b, Citizen ID: 9ac6f8ea-eac2-4c56-9988-f3e56a1c93ba,likes:2,comments:3,shares:0 Total Engagement: 5",
    "Rank 8: ID: 9accb5ca-85eb-43d6-b4fd-392a3e28b410, Citizen ID: 9a2f8466-0868-43a6-aaec-c8d8eabc5460,likes:1,comments:3,shares:0 Total Engagement: 4",
    "Rank 9: ID: 9ac70a94-c4d8-425e-bcf0-fc349af77778, Citizen ID: 9ac6f8ea-eac2-4c56-9988-f3e56a1c93ba,likes:2,comments:2,shares:0 Total Engagement: 4",
    "Rank 10: ID: 9ace242f-0808-4de4-a0c8-cf71a5292dc2, Citizen ID: 9ace0ce0-c252-4fe6-aadf-78e7239e1b5f,likes:4,comments:0,shares:0 Total Engagement: 4"
    # ... Other data entries ...
]
print(type(table_data))
iface = gr.Interface(
    fn=lambda: {"Table": "\n".join(table_data)},
    inputs=[],
    outputs=gr.outputs.Textbox(label="Table Data"),
    title="Max Engagements",
    description="Top engagements in a table format.",
    live=False  # To prevent displaying the interface while launching the script
)
iface.launch()
