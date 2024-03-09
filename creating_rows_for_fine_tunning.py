# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:17:47 2023

@author: Marcin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:28:26 2023

@author: Marcin
"""
import json

def create_json_line(user_input, assistant_input):
    
    user_row = {"role": "user", "content": user_input}
    assistant_row = {"role": "assistant", "content": assistant_input}
    json_line ='{"messages":[{"role": "system", "content": "Marcin"}'
    json_line = json_line +','+ json.dumps(user_row, ensure_ascii=False)
    json_line = json_line +','+ json.dumps(assistant_row, ensure_ascii=False) 
    json_line = json_line +']}\n'
    return json_line


DIRECTORY ='c:\\Users\\Marcin\\Documents\\GitHub\\openai-python\\'
chat = DIRECTORY + 'chat_for_fine_tunning.csv'
jsonl_filename = DIRECTORY + 'dataset.jsonl'

json_data = []


while True:

    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting the chat.")
        break  # Exit the loop
       
    bot_input = input("Bot: ")

    json_data.append(create_json_line(user_input, bot_input))
    
   
    
with open(jsonl_filename, 'a', encoding='utf-8') as jsonl_file:
    for row in json_data:  
        jsonl_file.write(row)



