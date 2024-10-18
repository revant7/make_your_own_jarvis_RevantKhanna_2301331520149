import nltk
from nltk.stem import WordNetLemmatizer

import random


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')
lemmatizer = WordNetLemmatizer()
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!", "How can I help you?"],
    "how are you": ["I'm just a program, but thanks for asking!", "Doing well, how about you?"],
    "what is your name": ["I am a chatbot.", "You can call me Chatbot!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

# def get_response(user_input):

#     user_input = user_input.lower()
    

#     for question in responses:
#         if question in user_input:
#             return random.choice(responses[question])
    
#     return "I'm sorry, I don't understand that."

def lemmatize_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in words]



def get_response(user_input):
    lemmatized_input = lemmatize_sentence(user_input)
    
    for question in responses:
        if lemmatized_input[0]+lemmatized_input[1] in question:
            return random.choice(responses[question])
    
    return "I'm sorry, I don't understand that."
print("Chatbot: Hello! I'm here to help you. (Type 'bye' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    
    response = get_response(user_input)
    print(f"Chatbot: {response}")




