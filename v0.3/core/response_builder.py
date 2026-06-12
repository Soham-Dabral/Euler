phrases = {
    "time": "the current time is",
    "date": "today is",
    "timer" : "your timer has"
}

def handle_response(facts):
        response = ''
        if len(facts) == 0:
            return "Apologies sir, I cannot find that command"
        
        else:
            for fact in facts:
                    key, value = fact
                    if key in phrases:
                            phrase = (f"{phrases[key]} {value} ")
                            if response == '':
                                response = phrase
                            else:
                                response = response + "and " + phrase
                            final_response = f"Sir, {response}"
            
            return final_response