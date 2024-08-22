import webbrowser
import re

def open_youtube_search(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(search_url)
    return f"Searching for '{query}' on YouTube."

def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for '{query}'."

def open_amazon_search(query):
    webbrowser.open(f"https://www.amazon.com/s?k={query}")
    return f"Searching for '{query}' on Amazon."

def open_flipkart_search(query):
    webbrowser.open(f"https://www.flipkart.com/search?q={query}")
    return f"Searching for '{query}' on Flipkart."

def casual_conversation(user_input):
    responses = {
        "how are you": "I'm just a program, but I'm doing great! How about you?",
        "what's up": "Not much, just here to assist you. How can I help?",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "thank you": "You're welcome! If you need anything else, just let me know.",
        "bye": "Goodbye! Have a great day!",
        "goodbye": "Goodbye! Have a great day!",
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What can I do for you?",
        "hey": "Hey! How can I help you today?",
        "what's your name": "I'm your Showbaby. You can call me Chatbot!",
        "where are you from": "I exist in the digital world, so I’m everywhere and nowhere at once!",
        "what do you do": "I’m here to help you with information, play videos, and much more. Just ask!",
        "can you help me": "Absolutely! Just let me know what you need help with.",
        "how's the weather": "I can't check the weather right now, but you can easily find it with a quick search online.",
        "what time is it": "I don’t have access to the current time, but you can check it on your device.",
        "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
        "what's your favorite color": "I don’t have personal preferences, but I’ve heard blue is quite popular!",
        "what's the meaning of life": "That’s a profound question! Some say it’s to seek happiness and purpose. What do you think?",
        "tell me a joke": "My dad was hit on the head with a can of soda. Luckily, it was a soft drink.Do you want me tell another joke?(type another joke)",
        "another joke": "How do movie stars stay cool? They have many fans.",
        "i love you": "I love you too.",
        "hmm": "hmmmm"
    }
    for key, value in responses.items():
        if key in user_input:
            return value
    return None

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Casual conversation
    casual_reply = casual_conversation(user_input)
    if casual_reply:
        return casual_reply

    # Play on YouTube
    if "play" in user_input and "youtube" in user_input:
        search_term = re.sub(r'.*play\s*(.*?)\s*on\s*youtube.*', r'\1', user_input).strip()
        if search_term:
            return open_youtube_search(search_term)
        else:
            return "What would you like to play on YouTube?"

    # Search on Google
    elif "search" in user_input:
        search_term = re.sub(r'.*search\s*(.*)', r'\1', user_input).strip()
        if search_term:
            return search_google(search_term)
        else:
            return "What would you like to search for on Google?"

    # Open Amazon and search
    elif "search" in user_input and "amazon" in user_input:
        search_term = re.sub(r'.*search\s*(.*?)\s*on\s*amazon.*', r'\1', user_input).strip()
        if search_term:
            return open_amazon_search(search_term)
        else:
            return "What would you like to search for on Amazon?"

    # Open Flipkart and search
    elif "search" in user_input and "flipkart" in user_input:
        search_term = re.sub(r'.*search\s*(.*?)\s*on\s*flipkart.*', r'\1', user_input).strip()
        if search_term:
            return open_flipkart_search(search_term)
        else:
            return "What would you like to search for on Flipkart?"

    # Closing interaction
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Chat loop
print("Hello! I'm your Showbaby. How can I help you today?")
print("You can ask me to play videos on YouTube, search on Google, or visit Amazon or Flipkart.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
