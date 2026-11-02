
# Simple Rule-Based Chatbot

def chatbot(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "your name" in message:
        return "I am a simple Python chatbot."

    elif "how are you" in message:
        return "I am fine. Thank you!"

    elif "college" in message:
        return "College is a place for learning."

    elif "bye" in message:
        return "Goodbye! Have a nice day!"

    elif "help" in message:
        return "Sure! Tell me what you need help with."

    else:
        return "Sorry, I don't understand that."


print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = chatbot(user_input)
    print("Chatbot:", response)

    if "bye" in user_input.lower():
        break
