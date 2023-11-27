# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:28:26 2023

@author: Marcin
"""

import csv
import os
from openai import OpenAI
client = OpenAI()

DIRECTORY ='c:\\Users\\Marcin\\Documents\\GitHub\\openai-python\\'
setup = DIRECTORY + 'setup.csv'
chat = DIRECTORY + 'chat.csv'

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
print (messages)
while True:

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages = setup_data + chat_data
    )
    reply = response.choices[0].message.content
    # reply = 'reply'
    print ("Bot: " + reply)
    chat_data.append({"role": "assistant", "content": reply})
    
    user_input = input("You: ")
    if user_input.lower() == "s":
        setup_input = input("System: ")
        setup_data.append({"role": "system", "content": setup_input})
    if user_input.lower() == "exit":
        print("Exiting the chat.")
        break  # Exit the loop
    chat_data.append({"role": "user", "content": user_input})


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


