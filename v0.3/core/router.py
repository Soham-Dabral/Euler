from commands.command import current_time
from commands.command import current_date
from commands.command import set_timer
from core.parser import timer_parser

#Dictionary to store keywords
KEYWORDS = {
    "time": {"function": current_time, "parser": None},
    "date": {"function": current_date, "parser": None},
    "timer": {"function": set_timer, "parser": timer_parser}
    }


#Main router body
def handle_prompt(prompt: str):
    #Normalizing the input
    prompt = prompt.strip().lower()
    
    #Removing irrelevant characters and storing them into cleaned_prompt
    irrelevant_characters = ['.', ',', '!', '?']
    cleaned_prompt = ''
    for character in prompt:
        if character not in irrelevant_characters:
            cleaned_prompt += character
    
    #Checks for different intents
    matched_requests = []

    #Stores facts that are later sent to response_builder module
    facts = []
    
    tokens = cleaned_prompt.split(" ")

    #To check if a keyword is already typed
    seen = set()

    #Checks the number of pre-defined intents that user has asked in their prompt 
    for word in tokens:
        if word in KEYWORDS:
            if word not in seen:
                seen.add(word)
                matched_requests.append((word, KEYWORDS[word]))

        else:
            continue
    
    #Check for asked pre-defined intents
    if len(matched_requests) == 0:
        error = "Command not found \n"
        return facts, error
    
    else:
        for key, metadata in matched_requests:
                func = metadata["function"]
                parser = metadata["parser"]

                if parser is not None: 
                    parser_args, error = parser(tokens)
                    facts.append((key, func(parser_args)))          

                else:
                    facts.append((key, func()))
                    error = None
        
        return facts, error