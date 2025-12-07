"""
Memory Chatbot
-----------------
A simple text based Chatbot that:
- Remembers your name
- Remembers your favorite color, food, and hobby
- Responds differently based on what it remembers
- Keeps a short conversation history

Good next step project for practicing:
- Loops
- Functions
- Dictionaries
- String handling
"""

#------ Memory structure ------
memory = {
"name" : None,
"favorite_color" : None,
"favorite_food" : None,
"hobby" : None,
"history" : []
}

#------ Helper Functions ------
def remember(speaker, message):
    """Store a line of conversation in history."""
    memory["history"].append((speaker, message))
    # Keep history from getting too long
    if len(memory["history"]) >= 20:
        memory["history"].pop(0)

def print_history():
    """Prints the conversations history."""
    print("\n --- Conversation History ---")
    for speaker, message in memory("history"):
        print(f"{speaker} : {message}")
    print("-------------------------")

def ask_for_name():
    """Asks the usre for their name if we don't know it yet."""
    if memory["name"] is None:
        print("Bot: I don't think we have met before. What is your name?")
        user_input = input("You: ")
        remember("You", user_input)

        #Simple cleaning
        name = user_input.strip().title()
        memory["name"] = name
        print(f"Bot: Nice to meet you, {name}!" )
    else:
        print(f"Bot: I remember you, {memory['name']}! Welcome back! \n")
        remember("Bot", f"I remember you, {memory['name']}! Welcome back! \n")

def handle_small_talk(message):
    """Respond to basic greetings or how are you questions."""
    text = message.lower()

    if any(word in text for word in ["Hi", "hello", "hey"]):
        return f"Hi {memory['name']  or "" }! How are you feeling today?"
    
    if "how are you" in text:
        return "I am just a bunch of python code, but I am doing great!"

    if "thank" in text:
        return 'You are welcome! Happy to chat anytime.'
    
    if "bye" in text or "goodnight" in text or "good night" in text:
        return "Bye! It was fun talking to you"
    
    return None #This means that no small talk match

def update_prefrences(message):
    """Look for sentences like: 
    - my favorite color is blue
    - I like pizza
    - My hobby is playing chess
    Update Memory
    """
    text = message.lower()

    #favorite color
    if "favorite colour is" in text:
        color = text.split("favorite color is ", 1)[1].strip().strip(".!?")
        memory["favorite_color"] = color
        return f"Cool! I will remember that your favorite color is {color}"
    
    #favorite food
    if "favorite food is" in text:
        food = text.split("favorite food is ", 1)[1].strip().strip()(".!?")
        memory["favorite_food"] = food
        return f"Yummy! {food} sounds delicious. I will remember it! "
    
    if "I like to eat" in text:
        food = text.split("I like to eat", 1)[1].strip().strip(".!?")
        memory["I like to eat"] = food
        return f"Nice! I will remember that you like to eat  {food}"

    if " favorite hobby is" in text:
        hobby = text.split(" favorite hobby is", 1)[1].strip().strip(".!?")
        memory["My favorite hobby is"] = hobby
        return f"Cool! I also think that {hobby} is cool too!"

    return None #Means no preference update

def asnwer_questions(message):
    """Answers questions about what the bot remembers."""
    text = message.lower()
    #Asks what the bot remembers
    if "what do you remember?" in text or "what do you know about me" in text:
        facts = []
        if memory["name"]:
            facts.append(f"Your name is {memory['name']}")

        if memory["favorite_color"]:
            facts.append(f"Your favorite color is {memory['favorite_color']}")

        if memory["favorite_food"]:
            facts.append(f"Your favorite food is {memory['favorite_food']}")

        if memory["hobby"]:
            facts.append(f"Your hobby is {memory['hobby']}")

        if not facts:
            return "I don't remember much yet. Tell me your favorite color, food, or hobby!"
        
        else:
            return "I remember that " +",".join(facts)+ "."
        
    #Asks about favorite things
    if "favorite color" in text and "my" not in text:
        if memory["favorite_color"]:
            return f"You told me that your favorite color is {memory['favorite_color']}"
        else:
            return "You haven't told me your favorite color yet. You can say: 'my favorite color is blue'."

    if "favorite food" in text and "my" not in text:
        if memory["favorite_food"]:
            return f"You told me that your favorite food is {memory['favorite_food']}"
        else:
            return "You haven't told me your favorite food yet. You can say: 'my favorite food is pizza'."     

    if "hobby" in text and "my" not in text:
        if memory["hobby"]:
            return f"You told me that your favorite hobby is {memory['hobby']}"
        else:
            return "You haven't told me your favorite hobby yet. You can say: 'my favorite hobby is  playing chess'."  
    
    return None #No questions answered

def generate_default_reply(message):
    """Fall back reply. Nothing else matches."""
    text = message.lower()

    if "bored" in text:
        return "Are your bored? Maybe try teaching me something new in python: 😂"
    
    if "school" in text:
        return "School can be tough, but learning cool things like how to code is pretty cool!"
    
    if "game" in text:
        return "I love games! You could even code a new game in python and show it to me"
    
    return "Interesting, tell me more or tell me about your favorite color, food, or hobby/activity!"

#------- Main chat loop -------
def chat():
    print("Bot: Hello! I am a memory bot 🤖")
    remember("Bot: ", "Hello! I am a memory bot 🤖")

    ask_for_name()

    print("Bot: You can talk to me about your favorite color, food, or hobby or you could just chat!")
    print("Bot: Type 'history' to see our conversation history or 'quit' to stop chatting/exit. \n")
    remember("Bot: ","You can talk to me about your favorite color, food, or hobby or you could just chat!")

    while True:
        user_input = input("You: ")

        #Store in history
        remember("You", user_input)
        
        #Commands
        if user_input.lower().strip() == "quit":
            print("Bot: I had a nice time chatting with you! 👋")
            remember("Bot: ","I had a nice time chatting with you! 👋")
            break
        
        if user_input.lower().strip() == 'history':
            print_history()
            continue

        # 1. Try small talk
        reply = handle_small_talk(user_input)
        if reply:
            print("Bot: ", reply)
            remember("Bot: ", reply)
            #If the user said bye, end after reply
            if "bye" in reply:
                print("Bot: Bye! 👋")
                break
            continue

        # 2. Try to update preferences
        reply = update_prefrences(user_input)
        if reply:
            print("Bot: ", reply)
            remember("Bot: ", reply)
            continue

        # 3. Try to answer questions
        reply = asnwer_questions(user_input)
        if reply:
            print("Bot: ", reply)
            remember("Bot: ", reply)
            continue

        # 4. Fall back reply
        reply = generate_default_reply(user_input)
        print("Bot: ", reply)
        remember("Bot: ", reply)
    
# Runs the chatbot/program

if __name__ == "__main__":
    chat()