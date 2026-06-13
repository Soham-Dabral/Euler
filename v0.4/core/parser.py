from core.app_launcher import APPS

def app_parser(tokens: list):
    requested_apps = []
    error = None
    for app in APPS:
        requested_apps.append(APPS[app])
    
    for app in requested_apps:
        aliases = app["aliases"]
        for app_name in aliases:
            if app_name in tokens:
                return app_name, error

def timer_parser(tokens: list):
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
    
    for i in range(len(tokens)):
        try: 
            if i + 1 < len(tokens) and tokens[i + 1] in units:
                value = int(tokens[i])
                unit = tokens[i + 1]
                error = None
                seconds += value * units[unit]
            
        except ValueError:
            error = 'ValueError'
            pass
    return seconds, error