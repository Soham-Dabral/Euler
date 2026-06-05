from commands.command import current_time
from commands.command import current_date
from commands.command import set_timer

def timer_parser(prompt: list):
    units = {
        "hour": 3600,
        "hours": 3600,
        "hr": 3600,
        "minute": 60,
        "minutes": 60,
        "min": 60,
        "second": 1,
        "seconds": 1,
        "sec": 1,
        "s": 1
        }

    seconds = 0
    
    for i in range(len(prompt)):
        try: 
            if i + 1 < len(prompt) and prompt[i + 1] in units:
                value = int(prompt[i])
                unit = prompt[i + 1]

                seconds += value * units[unit]
            
        except ValueError:
            pass
    
    return seconds


#Dictionary to store keywords
KEYWORDS = {
    "time": {"function": current_time, "parser": None},
    "date": {"function": current_date, "parser": None},
    "timer": {"function": set_timer, "parser": timer_parser}
    }

#Main router body
def handle_prompt(keyword: str):
    #Normalizing the input
    keyword = keyword.strip().lower()
    
    #Removing irrelevant characters and storing them into cleaned_prompt
    irrelevant_characters = ['.', ',', '!', '?']
    cleaned_prompt = ''
    for character in keyword:
        if character not in irrelevant_characters:
            cleaned_prompt += character
    
    #Checks for different intents
    matched_requests = []

    #Stores final output
    final_output = ''
    
    prompt = cleaned_prompt.split(" ")

    #Checks the number of pre-defined intents that user has asked in their prompt 
    for word in set(prompt):
        if word in KEYWORDS:
            matched_requests.append(KEYWORDS[word])
        
        else:
            continue
    #Check for asked pre-defined intents

    if len(matched_requests) == 0:
        return "Command not found \n"
    
    else:
        for request in matched_requests:
                func = request["function"]
                parser = request["parser"]

                if parser is not None: 
                    parser_args = parser(prompt)
                    final_output += func(parser_args) + "\n"

                else:
                    final_output += func() + "\n"
        
        return final_output