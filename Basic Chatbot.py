import random
import re
responses = {
    "hello":["Hi there!","Hello!","Greetings!"],
    "how are you":["I'm doing well,thank you.","I'm fine,and You"],
    "goodbye":["Goodbye!","see you later!","Bye!"]
}

while True:
    user_input = input("You: ")
    user_input = user_input.lower().strip('"').strip('"')
    user_input = re.sub(r'[^\w\s]','',user_input)
    
    
    if user_input == "exit":
        print("Bot:Goodbye!")
        break
    if user_input in responses:
        bot_reply = random.choice(responses[user_input])
        print(f"Bot: {bot_reply}")
    else:
        print("bot: I'm sorry, I didn't understand what you said")
