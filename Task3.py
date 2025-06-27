import spacy
from datetime import datetime

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

# Simple intent recognition responses
RESPONSES = {
    'greet': "Hello! I'm your AI chatbot. How can I help you today?",
    'about': "I'm a simple AI chatbot built with Python and spaCy!",
    'time': lambda: f"The current time is {datetime.now().strftime('%H:%M:%S')}",
    'weather': "I'm not connected to real weather data, but I hope the weather is nice where you are!",
    'fallback': "Sorry, I didn't understand that. Can you rephrase?"
}

# Intent detection function
def get_intent(user_input):
    doc = nlp(user_input.lower())
    if any(token.lemma_ in ['hello', 'hi', 'hey'] for token in doc):
        return 'greet'
    if 'your name' in user_input.lower() or 'who are you' in user_input.lower():
        return 'about'
    if 'time' in user_input.lower():
        return 'time'
    if 'weather' in user_input.lower():
        return 'weather'
    return 'fallback'

# Main chat loop
print("Bot: Hello! I'm your AI chatbot. How can I help you today?")
while True:
    user_message = input("You: ")
    if user_message.lower() in ['exit', 'quit', 'bye']:
        print("Bot: Goodbye! Have a nice day.")
        break
    intent = get_intent(user_message)
    response = RESPONSES[intent]
    if callable(response):
        response = response()
    print(f"Bot: {response}")
