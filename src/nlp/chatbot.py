# chatbot classes and configurations
# This module contains classes and configurations for a simple chatbot simulation.

class ChatbotConfig:
    """Configuration for the chatbot."""

    """Attributes:
    model (str):The model to use for the chatbot
    temperature (float): Sampling temperature for response generation
    top_p (float): Nucleus sampling parameter.
    max_tokens (int): Maximum number of tokens for the response.
    max_tolerance (float): Maximum tolerance for response generation.
    """


    # Default parameters for the chatb0t mk I 
    def __init__(self, 
                 annotations = None,  
                 author = 'Outcast (Not the band)',
                 docstring = '',
                 history = [],
                 max_tokens = 1500, 
                 max_tolerance = 0.1,
                 model = 'gpt-3.5-turbo', 
                 name = 'Chatb0t',
                 qualname = 'Chatb0t Mk I',
                 response = None,
                 temperature = 1.0, 
                 top_p = 1.0,
                 version = 1.0
                 ):
               
        """Initialize the chatbot configuration."""
        # Check if the parameters are valid
        if not isinstance(docstring, str):
            raise ValueError("docstring must be a string")
        if max_tokens <= 0:
            raise ValueError ("Max_tokens must be a positive integer")
        if max_tolerance < 0 or max_tolerance > 1:
            raise ValueError ("Max_tolerance must be between 0 and 1")
        if temperature < 0 or temperature > 1:
            raise ValueError ("Temperature must be between 0 and 1")
        if top_p < 0 or top_p > 1:
            raise ValueError ("Top_p must be between 0 and 1") 
                             
        self.author = author # Author of the configuration
        self.annotations = [] # Annotations for the configuration
        self.doc = docstring # Documentation for the configuration
        self.history = [] # To keep track of conversation history
        self.max_tokens = max_tokens # Maximum number of tokens for the response
        self.max_tolerance = max_tolerance # Maximum tolerance for response generation
        self.model = model # The model to use for the chatbot          
        self.name = "ChatbotConfig" # Name of the configuration
        self.qualname = "ChatbotConfig" # Qualified name of the configuration
        self.response = None # Placeholder for the chatbot's response
        self.status = "Initialized" # Status of the configuration
        self.temperature = temperature # Sampling temperature for response generation
        self.top_p = top_p # Nucleus sampling parameter
        self.version = "1.0" # Version of the configuration 
        self.debug_info = {
            "author": author,
            "annotations": annotations,
            "model": model,
            "temperature": temperature,
                    "top_p": top_p,
                    "max_tokens": max_tokens,
                    "max_tolerance": max_tolerance,
                    "status": "Initialized",
                    "response": None,
                    "history": [],
                    "error": None,
                    "error_code": None,
                    "error_message": None,
                    "error_description": None,
                    "error_traceback": None,
                    "error_stack": None }
                 

class Chatbot:
    """A Simple chatbot class simulation."""

    """Attributes:"""
    def __init__ (self, config: ChatbotConfig):
        super().__init__() # Initialize the parent class
        """Initialize the chatbot with a configuration."""
        self.name = "SimpleChatbot" # Name of the chatbot
        self.version = "1.0" # Version of the chatbot
        self.author = "Your Name" # Author of the chatbot
        self.status = "Initialized" # Status of the chatbot;
        self.qualname = "SimpleChatbot" # Qualified name of the chatbot
        self.response = None # 
        self.model = config.model # The model to use for the chatbot # Placeholder for the chatbot's response
        self.temperature = config.temperature # Sampling temperature for response generation
        self.top_p = config.top_p # Nucleus sampling parameter
        self.max_tokens = config.max_tokens # Maximum number of tokens for the response
        self.history = [] # To keep track of conversation history
        self.config = config # Store the configuration for later use
        self.max_tolerance = config.max_tolerance # Store the maximum tolerance for response generation
        self.status = "initialized" # Set the initial status of the chatbot
        self.debug_info = {
             "author": self.author,
             "annotations": self.config.annotations,
             "doc": self.config.doc,
             "history": self.history,
             "model": self.model,
             "max_tokens": self.max_tokens,
             "max_tolerance": self.max_tolerance,
             "name": self.name,
             "qualname": self.qualname,
             "response": self.response,
             "status": self.status,
             "temperature": self.temperature,
             "top_p": self.top_p,
             "version": self.version,
        }
class ChatbotPrompt:
    
    """Prompts user for word to search"""
    
    def __init__(self,
                prompt = [],
                status = []):
                """Initialize the chatbot prompt."""
                self.status = "Prompting user for input" # Status of the prompt
                self.prompt = "Please enter a word to search: " # Prompt for user input
                self.response = None # Placeholder for the user's response
                self.history = [] # To keep track of conversation history
                self.debug_info = {
                     "prompt": self.prompt,
                     "status": self.status,
                     "response": self.response,
                     "history": self.history,
                     "error": None,
                     "error_code": None,
                     "error_message": None,
                     "error_description": None,
                     "error_traceback": None,
                     "error_stack": None,
                     "error_type": None,
                     "error_location": None,
                     "error_context": None,
                     "error_suggestion": None,
                     "error_solution": None,
                     "error_resolution": None
                        }
                
class chatbotPromptError(Exception):
    """Custom exception for chatbot prompt errors.
        
    Attributes:
        message (str): The error message describing the issue. 
        error_code (int, optional): A specific error code for categorizing the error.
    """
    def ___init__(self, message, error_code=None):
        """
        Initialize the chatbot prompt error.
            
        Args:
            message (str): The error message.
            error_code (int, optional): A specific error code  for the error (default: None). 
        """
        super().__init__(message) # Initialize the parent class
        self.status = "Prompt Error" # Status of the prompt error
        self.name = "ChatbotPromptError" # Name of the prompt error
        self.prompt = "Please enter a word to search: " # Prompt for user input
        self.response = None # Placeholder for the user's response
        self.history = [] # To keep track of conversation history
        self.debug_info = {}
        self.message = message
        self.error_code = error_code

    def __str__ (self):
        """ Return a string representation of the error. """
            
        if self.error_code is not None:
            return f"ChatbotPromptError [Code {self.error_code}]: {self.message}:]"
        return f"ChatbotPromptError: {self.message}"
         
class ChatbotRuntimeError(Exception):
    """Custom exception for chatbot errors. 
    This class is used to handle errors that occur during the chatbot's runtime. 
    
    Attributes:
        message (str): The error message describing the issue.
        error_code (int, optional): A specific error code for categorizing the error. 
    """
    def __init__(self, message, error_code=None):
        """
        Initialize the ChatbotRuntimeError.
    
        Args:
            message (str): the error message.
            error_code (int, optional): A specific error code for the error (default: None).
        """      
        super().__init__(message) # Call the parent Exception class's __init__method
        self.message = message
        self.error_code = error_code
    
    def __str__(self):
        """Return a string representation of the error."""
        if self.error_code is not None:
            return f"ChatbotError [Code {self.error_code}]: {self.message}"
        return f"ChatbotError: {self.message}"
    
class ChatbotRuntimeErrorWarning(ChatbotRuntimeError):
    """Warning for chatbot runtime errors."""
    def __init__(self, message, error_code=None):
        super().__init__(message, error_code)
        self.status = "warning - runtime error"
        

class ChatbotRuntimeErrorDebug(ChatbotRuntimeError):
    """Debugging information for chatbot runtime errors."""
    def __init__(self, message, error_code=None, history=None):
       super().__init__(message, error_code)
       self.status = "Debug - Runtime Error"
       self.debug_info = {
           "model": None,
           "temperature": None,
           "top_p": None,
           "max_tokens": None,
           "max_tolerance": None,
           "history": history, # Default to an empty list if history is None
        }
        if history is None:
            self.history = []
        else:
            self.history = history
            self.debug_info = {
                "model": None,
                "temperature": None,
                "top_p": None,
                "max_tokens": None,
                "max_tolerance": None,
                "history": self.history,
                "error": None,
                "error_code": None,
            }

try: 
      raise ChatbotRuntimeError("An error occurred", error_code=404)
except ChatbotRuntimeError as e:
      print(e)