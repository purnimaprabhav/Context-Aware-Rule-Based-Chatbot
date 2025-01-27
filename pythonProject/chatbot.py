import json
import random

# Load intents from the JSON file
def load_intents(file_path="intents.json"):
    with open(file_path, "r") as file:
        return json.load(file)

# Find a response based on user input
def chatbot_response(user_input, intents):
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input.lower():
                return random.choice(intent["responses"])
    return "I'm sorry, I didn't understand that. Can you rephrase?"

# Main chatbot loop
def main():
    print("Chatbot: Hello! I am your assistant. Type 'quit' to exit.")
    intents = load_intents()  # Load the intents

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break

        response = chatbot_response(user_input, intents)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
