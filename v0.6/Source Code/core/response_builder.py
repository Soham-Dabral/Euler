phrases = {
    "date": "today is",
    "open": "opening",
    "close": "closing",
    "search": "searching",
    "time": "the current time is",
    "timer": "your timer has"
}

def handle_response(facts, error):
        response = ''
        if len(facts) == 0:
            return "Apologies, I cannot find that command"
        
        else:
            for fact in facts:
                    key, value = fact
                    if error == 'AppNotFound':
                        return f"Apologies, I can't find the application '{value}'"
                    if error == 'SettingsNotFound':
                        return f"Apologies, I can't find the setting '{value}'"
                    if error == 'LinkNotFound':
                        return f"Apologies, I can't find the link '{value}'"
                    
                    if key in phrases:
                        phrase = (f"{phrases[key]} {value} ")
                        if response == '':
                            response = phrase
                        else:
                            response = response + "and " + phrase
                        
                        final_response = response[0].upper() + response[1:]
            
            return final_response