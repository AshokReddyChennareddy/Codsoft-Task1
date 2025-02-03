import re
from datetime import datetime

# A simple function to get the chatbot's response
def chatbot_response(user_input):
    # Converting user input to lowercase to handle case insensitivity
    user_input = user_input.lower()

    # Rule-based responses using if-else statements...
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing great! How about you?"

    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot created by Ashok. What can I help you with?"

    elif re.search(r"weather|temperature", user_input):
        return "I cannot fetch real-time weather information, but it's always a good idea to check a weather app."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day ahead."

    elif re.search(r"thank you|thanks", user_input):
        return "You're welcome! Feel free to ask if you need more help."

    elif re.search(r"help|assist", user_input):
        return "Sure! I'm here to help. What do you need assistance with?"

    elif re.search(r"time", user_input):
        current_time = datetime.now().strftime('%H:%M %p')
        return f"The current time is {current_time}."

    elif re.search(r"day|date", user_input):
        current_date = datetime.now().strftime('%A, %B %d, %Y')
        return f"Today is {current_date}."

    elif re.search(r"joke", user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif re.search(r"favorite color", user_input):
        return "I don't have eyes to see, but if I could, I'd love all colors equally!"

    elif re.search(r"programming language|coding", user_input):
        return "I was built using Python, a versatile and powerful programming language."

    elif re.search(r"food", user_input):
        return "I don't eat, but if I could, I'd try pizza first!"

    elif re.search(r"music", user_input):
        return "I love the sound of code running smoothly, but I hear classical music is relaxing!"

    elif re.search(r"sports", user_input):
        return "I don't play sports, but I hear soccer and basketball are quite popular."

    elif re.search(r"favorite movie", user_input):
        return "I don't watch movies, but if I could, 'The Matrix' seems like a great choice!"

    elif re.search(r"good morning", user_input):
        return "Good morning! I hope you have an amazing day!"

    elif re.search(r"good night", user_input):
        return "Good night! Sleep well and recharge for a new day."

    elif re.search(r"age", user_input):
        return "I don't age, but I was created to keep learning!"

    elif re.search(r"story", user_input):
        return "Once upon a time, there was a chatbot who helped people with their queries. The end!"

    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Chatbot conversation loop
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")

        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break

        # Get the chatbot's response based on the input
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Running the chatbot
if __name__ == "__main__":
    chatbot()
