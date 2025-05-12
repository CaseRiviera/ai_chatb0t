# Project A.R.I.E.L. 

from nlp.chatbot import Chatbot
from nlp.chatbot import ChatbotConfig
from nlp.chatbot import ChatbotResponse
from nlp.chatbot import ChatbotResponseType
from nlp.chatbot import ChatbotResponseStatus
from nlp.chatbot import ChatbotResponseError
from nlp.chatbot import ChatbotResponseSuccess
from nlp.chatbot import ChatbotResponseInfo
from nlp.chatbot import ChatbotResponseWarning
from nlp.chatbot import ChatbotResponseDebug
from nlp.chatbot import ChatbotResponseCritical
from nlp.chatbot import ChatbotResponseFatal
from nlp.chatbot import ChatbotResponseUnknown
from nlp.chatbot import ChatbotResponseNotFound
from nlp.chatbot import ChatbotResponseUnauthorized
# I'm sorry Dave but I cannot do that. 
from nlp.chatbot import ChatbotResponseForbidden
from nlp.chatbot import ChatbotResponseBadRequest
from nlp.chatbot import ChatbotResponseInternalServerError
from nlp.chatbot import ChatbotResponsiveServiceUnavailable
from nlp.chatbot import ChatbotReponseGatewayTimeout
from nlp.chatbot import ChatbotResponseConflict
from nlp.chatbot import ChatbotResponseTooManyRequests
from nlp.chatbot import ChatbotReponseNotImplemented
from nlp.chatbot import ChatbotResponseBadGateway

def start_ariel():
 # Initialize the chatbot with default configuration
    """Start the A.R.I.E.L."""
    print("Welcome to A.R.I.E.L. Mr. Timez!")
    config = ChatbotConfig()
    chatbot = Chatbot(config)
    

    print("I am here to assist you with your definitions and synonym requests.")
    print("Type 'exit' to end the conversation or escape key to stop search.")

    bot = chatbot

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit','quit', 'stop':
            print("A.R.I.E.L. is shutting down.")
            break
        elif user_input.lower() == 'escape':
            print("A.R.I.E.L. is stopping the search.")
        continue
            response = bot.get_response(user_input)
        if response.status == ChatbotResponseStatus.
            SUCCESS:
                print(f"A.R.I.E.L.: {response}")
        if user  
            _user_input.lower() == 'help':
                print('Available commands:')
                print('- exit: End the conversation')
                print('- escape: Stop the search')
        elif user_input.lower() == 'help':
         # Get response from the chatbot
        try:
            response = chatbot.get_response(user_input)
            if response.status == "success":  # Assuming "success" is the status for a valid response
                print(f"A.R.I.E.L.: {response.message}")
            else:
                print(f"A.R.I.E.L. encountered an issue: {response.error_message}")
        except Exception as e:
            print(f"Error: {e}")

    return chatbot