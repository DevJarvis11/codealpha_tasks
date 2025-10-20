"""
TASK 4: BASIC RULE-BASED CHATBOT
File: basic_chatbot.py
Description: A simple conversational chatbot with predefined responses
"""

import random
from datetime import datetime

class SimpleChatBot:
    """A simple rule-based chatbot"""
    
    def __init__(self, bot_name="ChatBot"):
        self.bot_name = bot_name
        self.user_name = None
        self.conversation_count = 0
        
    def get_greeting_response(self):
        """Return random greeting"""
        greetings = [
            f"Hello! I'm {self.bot_name}. How can I help you today?",
            f"Hi there! {self.bot_name} here. What's on your mind?",
            "Hey! Great to see you! What would you like to talk about?",
            "Greetings! How are you doing today?",
            "Hello friend! How can I assist you?"
        ]
        return random.choice(greetings)
    
    def get_howru_response(self):
        """Return response to 'how are you'"""
        responses = [
            "I'm doing great, thanks for asking! How about you?",
            "I'm functioning perfectly! How are you feeling?",
            "Pretty good! What brings you here today?",
            "I'm excellent, thank you! How can I help you?",
            "All systems operational! How are things with you?"
        ]
        return random.choice(responses)
    
    def get_joke(self):
        """Return a random joke"""
        jokes = [
            "Why don't programmers like nature? It has too many bugs! 🐛",
            "Why do Python programmers prefer dark mode? Because light attracts bugs! 💡🐞",
            "What's a programmer's favorite hangout? Foo Bar! 🍺",
            "Why did the programmer quit his job? He didn't get arrays! 😄",
            "How many programmers does it take to change a light bulb? None, it's a hardware problem! 💡",
            "Why do Java developers wear glasses? Because they don't C#! 👓",
            "What do you call 8 hobbits? A hobbyte! 🧙",
            "Why was the JavaScript developer sad? Because he didn't Node how to Express himself! 😢",
            "What's the object-oriented way to become wealthy? Inheritance! 💰",
            "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?' 🍻"
        ]
        return random.choice(jokes)
    
    def get_default_response(self):
        """Return default response for unrecognized input"""
        defaults = [
            "I'm not sure I understand. Can you rephrase that?",
            "Hmm, I didn't quite catch that. Could you say it differently?",
            "That's interesting! Tell me more.",
            "I'm still learning. Try asking me something else!",
            "I don't have an answer for that yet. Try asking about the time, weather, or tell me a joke!",
            "Could you explain that in a different way?",
            "I'm not programmed to understand that yet, but I'm always learning!"
        ]
        return random.choice(defaults)
    
    def analyze_input(self, user_input):
        """Analyze user input and return appropriate response"""
        
        user_input = user_input.lower().strip()
        self.conversation_count += 1
        
        # Greeting patterns
        if any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings', 'sup', 'yo']):
            return self.get_greeting_response()
        
        # How are you patterns
        elif any(phrase in user_input for phrase in ['how are you', 'how are u', 'how r u', 'how do you do']):
            return self.get_howru_response()
        
        # Bot name query
        elif any(phrase in user_input for phrase in ['your name', 'who are you', 'what are you called']):
            return f"I'm {self.bot_name}, your friendly assistant! What's your name?"
        
        # User introduces themselves
        elif 'my name is' in user_input:
            name = user_input.split('my name is')[-1].strip()
            self.user_name = name.title()
            return f"Nice to meet you, {self.user_name}! How can I help you today?"
        
        elif "i'm" in user_input and user_input.startswith("i'm"):
            possible_name = user_input.replace("i'm", "").strip()
            if len(possible_name.split()) <= 2 and possible_name.replace(" ", "").isalpha():
                self.user_name = possible_name.title()
                return f"Nice to meet you, {self.user_name}!"
        
        # Time query
        elif any(word in user_input for word in ['time', 'what time']):
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time} ⏰"
        
        # Date query
        elif any(word in user_input for word in ['date', 'what day', 'today']):
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {current_date} 📅"
        
        # Help query
        elif any(word in user_input for word in ['help', 'what can you do', 'commands']):
            return ("I can chat with you! Here's what I can do:\n"
                    "  💬 Respond to greetings (hi, hello, hey)\n"
                    "  🤔 Answer 'how are you?'\n"
                    "  🤣 Tell you jokes\n"
                    "  ⏰ Tell you the time\n"
                    "  📅 Tell you the date\n"
                    "  🌤️ Talk about weather (basic)\n"
                    "  👤 Remember your name\n"
                    "  💬 Have casual conversations!")
        
        # Joke request
        elif any(word in user_input for word in ['joke', 'funny', 'laugh', 'humor']):
            return self.get_joke()
        
        # Thank you
        elif any(word in user_input for word in ['thank', 'thanks', 'thx']):
            thanks_responses = [
                "You're welcome! 😊",
                "Happy to help!",
                "Anytime! That's what I'm here for!",
                "My pleasure!",
                "Glad I could help!"
            ]
            return random.choice(thanks_responses)
        
        # Age query
        elif any(phrase in user_input for phrase in ['how old', 'your age', 'when were you born']):
            return "I'm just a program, so I don't really have an age. But I was created using Python! 🐍"
        
        # Weather query
        elif 'weather' in user_input:
            weather_responses = [
                "I can't check live weather data, but I hope it's nice where you are! ☀️",
                "I don't have access to weather services, but you can check weather.com!",
                "I wish I could tell you! Try asking about the time or date instead. 🌤️"
            ]
            return random.choice(weather_responses)
        
        # Feeling good
        elif any(phrase in user_input for phrase in ["i'm good", "i'm fine", "i'm great", "doing well", "pretty good"]):
            return "That's wonderful to hear! 😊 What would you like to talk about?"
        
        # Feeling bad
        elif any(phrase in user_input for phrase in ["i'm sad", "i'm not good", "feeling bad", "not well", "depressed"]):
            return "I'm sorry to hear that. 😔 I hope things get better soon! Want to hear a joke to cheer you up?"
        
        # Goodbye patterns
        elif any(word in user_input for word in ['bye', 'goodbye', 'see you', 'exit', 'quit', 'later']):
            farewell_messages = [
                "Goodbye! Have a wonderful day! 👋",
                "See you later! Take care! 😊",
                "Bye! Come back anytime!",
                "Farewell! It was nice chatting with you!",
                f"Goodbye{', ' + self.user_name if self.user_name else ''}! Hope to see you again! 👋"
            ]
            return random.choice(farewell_messages)
        
        # Default response
        else:
            return self.get_default_response()

def main():
    """Main function to run the chatbot"""
    
    bot = SimpleChatBot("ChatBot")
    
    print("=" * 65)
    print("🤖 WELCOME TO CHATBOT!")
    print("=" * 65)
    print(f"Hello! I'm {bot.bot_name}, your friendly conversational assistant.")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("Type 'help' to see what I can do.")
    print("=" * 65)
    
    while True:
        user_input = input("\n😊 You: ").strip()
        
        if not user_input:
            print("🤖 Bot: Please say something!")
            continue
        
        response = bot.analyze_input(user_input)
        print(f"🤖 Bot: {response}")
        
        # Check for exit commands
        if any(word in user_input.lower() for word in ['bye', 'goodbye', 'exit', 'quit', 'see you', 'later']):
            print("\n" + "=" * 65)
            print(f"Total messages exchanged: {bot.conversation_count}")
            print("Thank you for chatting! Come back soon! 💙")
            print("=" * 65)
            break

if __name__ == "__main__":
    main()