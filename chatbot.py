import json
import random

# Load intents from the JSON file
def load_intents(file_path="intents.json"):
    with open(file_path, "r") as file:
        return json.load(file)

# Find a response based on user input
def chatbot_response(user_input, intents):
    user_input = user_input.lower()  # Convert input to lowercase for consistency

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            # Check if the user's input matches any pattern exactly or contains the pattern as a keyword
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])

    return "I'm sorry, I didn't quite understand that. Could you rephrase?"


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
