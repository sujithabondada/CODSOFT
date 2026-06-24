# ============================================================
# CodSoft AI Internship — Task 1
# Rule-Based Chatbot using Pattern Matching
# ============================================================

import re
import random
from datetime import datetime

# ──────────────────────────────────────────────
# Rules: list of (patterns, responses) tuples
# ──────────────────────────────────────────────
rules = [
    (
        [r'\b(hi|hello|hey|howdy|greetings)\b'],
        [
            "Hello! 👋 Great to meet you! How can I help you today?",
            "Hey there! 😊 Welcome! Ask me anything.",
            "Hi! Nice to see you. What's on your mind?"
        ]
    ),
    (
        [r'\b(how are you|how do you do|how.s it going)\b'],
        [
            "I'm doing great, thanks for asking! 😊 How about you?",
            "Running at full capacity! 🚀 All systems operational.",
        ]
    ),
    (
        [r'\b(what is your name|who are you|your name)\b'],
        [
            "I'm CodSoft AI Assistant 🤖 — a rule-based chatbot built for Task 1 of the CodSoft AI Internship!"
        ]
    ),
    (
        [r'\b(who made you|who built you|who created you)\b'],
        [
            "I was built as part of the CodSoft AI Internship — Task 1: Rule-Based Chatbot! 💻"
        ]
    ),
    (
        [r'\b(what can you do|help|capabilities)\b'],
        [
            "I can help with:\n  • AI & tech questions\n  • Jokes\n  • Simple math\n  • Time & date\n  • General conversation\nJust ask!"
        ]
    ),
    (
        [r'\b(what is ai|artificial intelligence|explain ai)\b'],
        [
            "Artificial Intelligence (AI) 🤖 is the simulation of human intelligence in machines.\n"
            "It includes Machine Learning, NLP, Computer Vision, and Robotics!"
        ]
    ),
    (
        [r'\b(machine learning|ml)\b'],
        [
            "Machine Learning 📊 is a subset of AI where algorithms learn from data.\n"
            "Key types: Supervised, Unsupervised, and Reinforcement Learning."
        ]
    ),
    (
        [r'\b(deep learning|neural network)\b'],
        [
            "Deep Learning 🧬 uses multi-layered neural networks to learn complex patterns.\n"
            "It powers image recognition, NLP, and models like GPT!"
        ]
    ),
    (
        [r'\b(python|programming|coding)\b'],
        [
            "Python 🐍 is the #1 language for AI!\n"
            "Key libraries: NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch."
        ]
    ),
    (
        [r'\b(joke|funny|make me laugh|tell me a joke)\b'],
        [
            "Why do programmers prefer dark mode?\nBecause light attracts bugs! 🐛😄",
            "Why did the AI break up with the algorithm?\nBecause it kept taking things too literally! 😂",
            "Why do Java developers wear glasses?\nBecause they don't C#! 😄"
        ]
    ),
    (
        [r'\b(fun fact|did you know|interesting fact)\b'],
        [
            "Fun fact 🤓: The first computer bug was an actual bug!\n"
            "In 1947, a moth was found inside a Harvard computer.",
            "Fun fact 🤖: The term 'Artificial Intelligence' was coined in 1956 by John McCarthy!"
        ]
    ),
    (
        [r'\b(thank you|thanks|thx|appreciate)\b'],
        [
            "You're welcome! 😊 Happy to help anytime!",
            "No problem at all! 🙌 That's what I'm here for!"
        ]
    ),
    (
        [r'\b(bye|goodbye|see you|exit|quit)\b'],
        [
            "Goodbye! 👋 It was great chatting with you. Come back anytime!",
            "See you later! 😊 Keep learning and building amazing things!"
        ]
    ),
]

default_responses = [
    "Hmm, I'm not sure about that 🤔 Try asking about AI, Python, or request a joke!",
    "I didn't quite catch that. Could you rephrase? 💬",
    "That's outside my knowledge base. Try asking 'what can you do?' to see what I know!",
]

# ──────────────────────────────────────────────
# Core response function
# ──────────────────────────────────────────────
def get_response(user_input):
    text = user_input.lower().strip()

    # Special: simple math (e.g. "5 + 3", "10 * 2")
    math_match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', text)
    if math_match:
        a, op, b = math_match.group(1), math_match.group(2), math_match.group(3)
        try:
            result = eval(f"{a} {op} {b}")
            return f"🧮 {a} {op} {b} = {result}"
        except:
            pass

    # Special: current time
    if re.search(r'\b(what time|current time|what.s the time)\b', text):
        return f"🕐 Current time: {datetime.now().strftime('%I:%M %p')}"

    # Special: current date
    if re.search(r'\b(what.s the date|today.s date|date today)\b', text):
        return f"📅 Today is {datetime.now().strftime('%A, %B %d, %Y')}"

    # Pattern matching against rules
    for patterns, responses in rules:
        for pattern in patterns:
            if re.search(pattern, text):
                return random.choice(responses)

    # Default fallback
    return random.choice(default_responses)

# ──────────────────────────────────────────────
# Main chat loop
# ──────────────────────────────────────────────
def main():
    print("=" * 50)
    print("   CodSoft AI Chatbot — Task 1")
    print("   Rule-Based Chatbot")
    print("   Type 'quit' or 'bye' to exit")
    print("=" * 50)
    print("\nChatbot: Hello! 👋 I'm CodSoft AI Assistant.")
    print("         Ask me about AI, ML, Python, or just chat!\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Chatbot: {response}\n")

        # Exit condition
        if re.search(r'\b(bye|goodbye|exit|quit)\b', user_input.lower()):
            break

if __name__ == "__main__":
    main()
