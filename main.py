import chatbot

chatbot = chatbot.Chatbot(intents="intents.json")

chatbot.load_model("model.h5")

print(chabot.get_response())
