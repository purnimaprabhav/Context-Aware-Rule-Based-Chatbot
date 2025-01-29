import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)

# Dictionary to store conversation state
context = {}

def preprocess_text(text):
    """Tokenize and lemmatize the input text"""
    tokens = nltk.word_tokenize(text.lower())
    return [lemmatizer.lemmatize(word) for word in tokens]

def get_response(user_input, user_id="default_user"):
    """Find the best response based on user input and maintain chat context"""
    global context
    processed_input = preprocess_text(user_input)

    # If context exists, use it to provide a better response
    if user_id in context and context[user_id] is not None:
        if context[user_id] == "waiting_for_order_number":
            context[user_id] = None  # Reset context after use
            return f"Thanks! I'm checking order {user_input} now."

        if context[user_id] == "waiting_for_reservation_details":
            context[user_id] = None
            return f"Got it! Your table is reserved for {user_input}."

    # Check for matching intent
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            tokenized_pattern = preprocess_text(pattern)

            if set(processed_input).intersection(set(tokenized_pattern)):
                response = random.choice(intent["responses"])

                # If the response requires user input, set context
                if intent["tag"] == "order_status":
                    context[user_id] = "waiting_for_order_number"
                    return response  # Example: "Please provide your order number."

                if intent["tag"] == "restaurant_reservation":
                    context[user_id] = "waiting_for_reservation_details"
                    return response  # Example: "How many people and what time?"

                return response

    return "I'm not sure I understand. Can you rephrase?"

# Main chatbot loop
print("Chatbot: Hello! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = get_response(user_input, user_id="user1")  # Simulating a unique user
    print("Chatbot:", response)
