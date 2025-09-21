from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd


chatbot = ChatBot(
    'FarmingBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///farmingbot.sqlite3',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry, I do not understand. Can you rephrase?',
            'maximum_similarity_threshold': 0.85
        }
    ]
)


df = pd.read_csv('Farming_FAQ_Assistant_Dataset.csv')


conversation_list = []
for index, row in df.iterrows():
    conversation_list.append(row['question'])
    conversation_list.append(row['answer'])

trainer = ListTrainer(chatbot)
trainer.train(conversation_list)

print("Training completed!")
