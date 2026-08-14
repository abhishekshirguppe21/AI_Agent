def ai_agent(user_input):
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        return "Hello! I am your simple AI agent."

    elif "github" in text:
        return "GitHub is a platform for storing and sharing code."

    elif "python" in text:
        return "Python is a popular programming language."

    elif "your name" in text:
        return "I am SimpleAI, your basic AI agent."

    elif "help" in text:
        return "I can answer simple questions about Python, GitHub, and programming."

    elif "bye" in text:
        return "Goodbye!"

    else:
        return "I don't know that yet, but I can learn more responses."


print("Simple AI Agent")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = ai_agent(user_input)

    print("AI:", response)

    if user_input.lower() == "bye":
        break
