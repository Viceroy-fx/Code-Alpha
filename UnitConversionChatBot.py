from chatterbot import ChatBot


UnitConvertBot = ChatBot("Anas's Unit Converting ChatBot", logic_adapters=["chatterbot.logic.UnitConversion"])

while True:
    user_input = input("Enter to convert (Unit Conversion): ")
    print(f"Unit Conversion ChatBot: {UnitConvertBot.get_response(user_input)}")