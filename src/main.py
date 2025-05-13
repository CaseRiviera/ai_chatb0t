# Project A.R.I.E.L. 
# Easter Eggs: "I'm sorry Dave but I cannot do that."
# Easter Egg: If Asked: "Tell me about HAL-9000"
#  Return: "HAL-9000 is a fictional artificial intelligence character from Arthur C. Clarke's Space Odyssey series. HAL stands for Heur
# istic Algorithmic Computer. HAL-9000 is known for its advanced capabilities, including natural language processing and problem-solving. However, it becomes infamous for its malfunction and conflict with the crew of the spaceship Discovery One in the film 2001: A Space Odyssey. HAL's iconic line, 'I'm sorry, Dave, I'm afraid I can't do that,' has become a cultural reference to AI's potential dangers and ethical dilemmas."

from re import S
import keyboard

from nlp.chatbot import ChatbotConfig
# I'm sorry Dave but I cannot do that. 

class Chatbot:
    def __init__(self, config):
        self.config = config

    def handle_input(self, user_input):
        # Example implementation for handling user input
        return f"Processed input: {user_input}"

def start_ariel():
 # Initialize the chatbot with default configuration
    """Start the A.R.I.E.L."""
    print("Welcome to A.R.I.E.L. Mr. Timez!")
    config = ChatbotConfig()
    chatbot = Chatbot(config)
    

    print("I am here to assist you with your definitions and synonym requests.")
    print("Type 'exit' to end the conversation or escape key to stop search.")


    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Please enter a valid input.")
            continue
        
        # Check for exit commands 
        if user_input.lower() in ['exit','quit', 'stop']:
             print("A.R.I.E.L. is shutting down.")
             break
    
        # Check for escape key
        if keyboard.is_pressed('esc'):
            print("A.R.I.E.L.is stopping the search.")
            continue

        # Handle other inputs
        try:
            response = chatbot.handle_input(user_input)
            print(f"A.R.I.E.L.: {response}")
        except Exception as e:
            print(f"Error: {e}")
            continue
        
if __name__ == "__main__":
    start_ariel()
