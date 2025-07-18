def chatbot(): 
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.") 
    while True: 
        user_input = input("You: ").lower() 
        if "hello" in user_input: 
            print("Chatbot: Hi there! How can I help you?") 
        elif "how are you" in user_input: 
            print("Chatbot: I'm a bot, but I'm doing great!") 
        elif "your name" in user_input: 
            print("Chatbot: I'm a Python chatbot.") 
        elif user_input == "bye": 
            print("Chatbot: Goodbye! Have a great day!") 
            break 
        else: 
            print("Chatbot: Sry, I don't understand that.") 
chatbot() 
 
