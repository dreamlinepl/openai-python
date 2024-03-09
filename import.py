# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:28:26 2023

@author: Marcin
"""

import csv
import os
import json
from openai import OpenAI

def create_json_line(user_input, assistant_input):
    json_line ='{"messages":[{"role": "system", "content": "Jestes Marcin"}'
    json_line = json_line +','+ json.dumps(user_input, ensure_ascii=False)
    json_line = json_line +','+ json.dumps(assistant_input, ensure_ascii=False) 
    json_line = json_line +']}\n'
    return json_line


client = OpenAI()

DIRECTORY ='c:\\Users\\Marcin\\Documents\\GitHub\\openai-python\\'
setup = DIRECTORY + 'setup.csv'
chat = DIRECTORY + 'chat.csv'
jsonl_filename = DIRECTORY + 'dataset.jsonl'

# Import from CSV
setup_data = []
if os.path.exists(setup):
    with open(setup, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            setup_data.append({"role": row["role"], "content": row["content"]})

chat_data = []
if os.path.exists(chat):
    with open(chat, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            chat_data.append({"role": row["role"], "content": row["content"]})  
messages = setup_data + chat_data

json_data = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "s":
        setup_input = input("System: ")
        setup_data.append({"role": "system", "content": setup_input})
    if user_input.lower() == "exit":
        print("Exiting the chat.")
        break  # Exit the loop
    row_user = {"role": "user", "content": user_input}   
    chat_data.append(row_user)  
    
    
    # response_tuned_model = client.chat.completions.create(
    #   model="ft:gpt-3.5-turbo-1106:personal::8PzeNnoK",
    #   messages = setup_data + chat_data
    # )
    # reply_tuned_model = response_tuned_model.choices[0].message.content
    # chat_data.append({"role": "assistant", "content": reply_tuned_model})
    # print ("Tuned model: " + reply_tuned_model)

    
    response = client.chat.completions.create(
        # model="gpt-3.5-turbo-1106",
        # model="ft:gpt-3.5-turbo-1106:personal::8PzeNnoK",
        model = "ft:gpt-3.5-turbo-1106:personal::8QZkRfq0",
      messages = setup_data + chat_data
    )
    reply = response.choices[0].message.content

    print ("Bot: " + reply)

    # bot_input = input("Jak powinien odpowiedzieć?: ")
    
    row_assistant = {"role": "assistant", "content": reply}
    row_user = {"role": "user", "content": user_input}
    # row_model = {"role": "assistant", "content": bot_input}
    
    chat_data.append(row_assistant)
    # json_data.append(create_json_line(row_user, row_model))


with open(jsonl_filename, 'a', encoding='utf-8') as jsonl_file:
    for row in json_data:  
        jsonl_file.write(row)

# Export to CSV
with open(chat, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["role", "content"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Write the header
    writer.writeheader()
    # Write the data
    writer.writerows(chat_data)
    
with open(setup, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["role", "content"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Write the header
    writer.writeheader()
    # Write the data
    writer.writerows(setup_data)


