from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('SimpleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Start the conversation
print("SimpleBot: Hello! I'm your chatbot. Type 'exit' to end the conversation.")

while True:
    # Get user input
    user_input = input("You: ")

    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        print("SimpleBot: Goodbye!")
        break

    # Get the chatbot's response
    response = chatbot.get_response(user_input)

    # Print the chatbot's response
    print("SimpleBot:", response)
