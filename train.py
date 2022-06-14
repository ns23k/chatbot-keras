from chatbot import Chatbot

chatbot = Chatbot(intents="intents.json")

chatbot.train_model()
chatbot.save_model()
