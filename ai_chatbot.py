print("Bot: Hello! I am an AI Chatbot.")

while True:
    user = input("You: ").lower()

    # Greetings
    if "hi" in user or "hello" in user:
        print("Bot: Hi! How are you?")

    elif "fine" in user or "good" in user:
        print("Bot: That's great! Ask me something about AI.")

    # AI
    elif "what is ai" in user:
        print("Bot: Artificial Intelligence is a technology")
        print("Bot: that enables machines to think like humans.")

    # Machine Learning
    elif "machine learning" in user:
        print("Bot: Machine Learning is a subset of AI")
        print("Bot: where systems learn from data.")

    # Deep Learning
    elif "deep learning" in user:
        print("Bot: Deep Learning uses neural networks")
        print("Bot: to learn patterns from data.")

    # Data Science
    elif "data science" in user:
        print("Bot: Data Science means analyzing data")
        print("Bot: to get useful insights.")

    # Python
    elif "python" in user:
        print("Bot: Python is used in AI and web development.")

    # ChatGPT
    elif "chatgpt" in user:
        print("Bot: ChatGPT is an AI chatbot developed by OpenAI.")

    # AI Tools
    elif "ai tools" in user:
        print("Bot: Popular AI tools are ChatGPT and Gemini.")

    # Future of AI
    elif "future of ai" in user:
        print("Bot: AI has a bright future in technology.")

    # AI Jobs
    elif "jobs in ai" in user:
        print("Bot: AI Engineer, Data Scientist,")
        print("Bot: and ML Engineer are popular jobs.")

    # Bye
    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
