import ollama
MODEL="llama3.2:3b"

messages = []
while True:
    user_input = input("You: ")
    if user_input.lower() in ("quit", "exit", "q"):
        break
    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(model=MODEL, messages=messages)
    reply = response["message"]["content"]
    print(f"Bot: {reply}\n")
    messages.append({"role": "assistant", "content": reply})