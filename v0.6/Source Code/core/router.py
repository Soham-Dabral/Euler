from commands.command import current_time
from commands.command import current_date
from commands.command import set_timer

from core.parser import open_app_parser
from core.parser import open_link_parser
from core.parser import open_settings_parser
from core.parser import search_parser
from core.parser import timer_parser

from core.app_handler import open_apps
from core.app_handler import open_links
from core.app_handler import open_settings
from core.app_handler import search

#Dictionary to store keywords
KEYWORDS = {
    "date": {"function": current_date, "parser": None},
    "open": {"function": open_apps, "parser" : open_app_parser},
    "search": {"function": search, "parser" : search_parser},
    "time": {"function": current_time, "parser": None},
    "timer": {"function": set_timer, "parser": timer_parser}
    }


#Main router body
def handle_prompt(prompt: str):
    #Normalizing the input
    original_prompt = prompt.strip()
    prompt = prompt.strip().lower()
    
    #Removing irrelevant characters and storing them into cleaned_prompt
    irrelevant_characters = ['.', ',', '!', '?']
    cleaned_original_prompt = ''
    cleaned_prompt = ''
    
    for character in original_prompt:
        if character not in irrelevant_characters:
            cleaned_original_prompt += character
    
    for character in prompt:
        if character not in irrelevant_characters:
            cleaned_prompt += character
    
    
    #Checks for different intents
    matched_requests = []

    #Stores facts that are later sent to response_builder module
    facts = []
    
    original_tokens = original_prompt.split(" ")
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
               
                #Checks for parsers
                if parser is not None: 
                    parser_data = parser(tokens)
                    keyword = parser_data["keyword"]
                    kind = parser_data["kind"]
                    target = parser_data["target"]
                    value = parser_data["value"]
                    error = parser_data["error"]
                    
                    #Differentiates between setting a timer and opening apps and links
                    if value is not None:
                        facts.append((key, func(value)))
                        
                    elif target is not None:
                        if keyword == "Open":
                            if kind == "APPS":
                                if error is None:
                                    facts.append((key, func(target)))

                            if kind == "SETTINGS":
                                func = open_settings
                                parser = open_settings_parser
                                parser_data = parser(tokens)
                                kind = parser_data["kind"]
                                target = parser_data["target"]
                                value = parser_data["value"]
                                error = parser_data["error"]
                                
                                if error is None:
                                    facts.append((key, func(target)))
                            
                            if kind == "LINKS":
                                func = open_links
                                parser = open_link_parser
                                parser_data = parser(tokens)
                                kind = parser_data["kind"]
                                target = parser_data["target"]
                                value = parser_data["value"]
                                error = parser_data["error"]
                                
                                if error is None:
                                    facts.append((key, func(target)))
                            
                        else:                                
                            if error is None:
                                facts.append((key, func(target)))
                
                else:
                    facts.append((key, func()))
                    error = None
        
        return facts, error