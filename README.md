# 🤖 Context-Aware Rule-Based Chatbot

A lightweight, context-aware chatbot built in Python using NLTK. It demonstrates intent recognition, simple multi-turn dialog handling, and stateful interaction logic — all without using a machine learning model.

---

## 🔍 Project Overview

This chatbot simulates customer support conversations. It uses a JSON-based intent system, lemmatization and token matching for classification, and conversation state tracking to handle context-sensitive replies.

**Example Use Cases:**
- Tracking orders (asks for order number)
- Booking restaurant tables (asks for party size/time)
- Basic greetings and fallback responses

---

## 🧠 Features

- 🔹 Rule-based NLP using NLTK (no ML models)
- 🔹 Contextual memory across user turns (e.g., tracks if it’s waiting for info)
- 🔹 Easily extensible with new intents via JSON
- 🔹 Ideal for learning chatbot logic, NLU, and dialogue state handling

---

## 🛠 Tech Stack

| Tool     | Use Case                     |
|----------|------------------------------|
| Python   | Core implementation          |
| NLTK     | Tokenization, Lemmatization  |
| JSON     | Intent structure and storage |

---

## 💡 How It Works

1. **Preprocessing**: User input is tokenized and lemmatized
2. **Intent Matching**: Compares token overlap between input and pattern examples
3. **Context Management**: Stores what information the bot is waiting for (e.g., order number)
4. **Response Selection**: Picks a random reply from the matched intent or asks follow-up questions

---

---

## 🚀 Run It Locally

```bash
git clone https://github.com/purnimaprabhav/Context-Aware-Rule-Based-Chatbot.git
cd Context-Aware-Rule-Based-Chatbot
pip install nltk
python chatbot.py

