def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi! How can I help you?")
        elif user == "how are you":
            print("Chatbot: I am functioning well. Thank you!")
        elif user == "what is ai":
            print("Chatbot: AI stands for Artificial Intelligence.")
        elif user == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
