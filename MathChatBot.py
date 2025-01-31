from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer #ListTrainer is gonna take a list and pick out the best possible response to what the user is gonna type.




mathbot = ChatBot("Anas's Math ChatBot", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("-------------------------------------MATH CHATBOT ---------------------------------------")


while True:
    user_input = input("User: ")

    print(f"Chatbot: {mathbot.get_response(user_input)}")