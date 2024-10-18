import random
from answer_generator import get_answer
from text2audio import text_to_audio


responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!", "How can I help you?"],
    "hi": ["Hi there!", "Hello!", "Greetings!", "How can I help you?"],
    "hey": ["Hi there!", "Hello!", "Greetings!", "How can I help you?"],
    "how are you": ["I'm just a program, but thanks for asking!", "Doing well, how about you?"],
    "what is your name": ["I am a chatbot.", "You can call me Chatbot!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def get_response(user_input):

    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        out = get_answer(user_input)
        if out:
            return out
    
    return "I'm sorry, I don't understand that."


print("JARVIS: Hello! I'm here to help you. (Type 'bye' to exit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("JARVIS: Goodbye!")
        break
    
    response = get_response(user_input)
    print(f"JARVIS: {response}\n")
    text_to_audio(response)


