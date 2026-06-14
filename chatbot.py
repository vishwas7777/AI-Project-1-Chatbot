responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I am fine.",
    "what is your name": "I am DecodeBot.",
    "python": "Python is a programming language.",
    "bye": "Goodbye!"
}

print("🤖 DecodeBot Started")
print("Type exit to quit")

while True:
    user = input("You: ").lower().strip()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    print("Bot:", responses.get(user, "Sorry, I don't understand."))