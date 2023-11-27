from openai import OpenAI
client = OpenAI()
DIRECTORY ='c:\\Users\\Marcin\\Documents\\GitHub\\openai-python\\'
initial_setup = DIRECTORY+'setup.csv'
chat = DIRECTORY+ 'chat.csv'

while True:
    with open(initial_setup, 'r') as file:
    # Read the content of the file
        setup = file.read()

    with open(chat, 'r') as file:
    # Read the content of the file
        chat = file.read()




