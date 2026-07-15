from core.app_handler import APPS
from core.app_handler import LINKS
from core.app_handler import SETTINGS

def open_app_parser(tokens: list):
    requested_apps = []
    for app in APPS:
        for alias in APPS[app]["aliases"]:
            for i in range(len(tokens)):
                if i + 1 < len(tokens) and tokens[i].lower() == "open" and tokens[i + 1] == alias:
                    requested_apps.append(tokens[i + 1])

    if len(requested_apps) == 0:
        parsed_data = {
        "keyword": "Open",
        "kind": "SETTINGS",
        "target": requested_apps,
        "value": None,
        "error": 'AppNotFound'
        }
        return parsed_data   

    else:
        parsed_data = {
        "keyword": "Open",
        "kind": "APPS",
        "target": requested_apps,
        "value": None,
        "error": None
        }
        return parsed_data

def open_settings_parser(tokens: list):
    requested_settings = []
    for setting in SETTINGS:
        for alias in SETTINGS[setting]["aliases"]:
            for i in range(len(tokens)):
                if i + 1 < len(tokens) and tokens[i].lower() == "open" and tokens[i + 1] == alias:
                    requested_settings.append(tokens[i + 1])

    if len(requested_settings) == 0:
        parsed_data = {
        "keyword": "Open",
        "kind": "LINKS",    
        "target": requested_settings,
        "value": None,
        "error": 'SettingsNotFound'
        }
        return parsed_data   

    else:
        parsed_data = {
        "keyword": "Open",
        "kind": "SETTINGS",
        "target": requested_settings,
        "value": None,
        "error": None
        }
        return parsed_data

def open_link_parser(tokens: list):
    requested_links = []
    for link in LINKS:
        for alias in LINKS[link]["aliases"]:
            for i in range(len(tokens)):
                if i + 1 < len(tokens) and tokens[i].lower() == "open" and tokens[i + 1] == alias:
                    requested_links.append(tokens[i + 1])

    if len(requested_links) == 0:
        parsed_data = {
        "keyword": "Open",
        "kind": "LINKS",    
        "target": requested_links,
        "value": None,
        "error": 'LinkNotFound'
        }
        return parsed_data   

    else:
        parsed_data = {
        "keyword": "Open",
        "kind": "LINKS",
        "target": requested_links,
        "value": None,
        "error": None
        }
        return parsed_data

def search_parser(tokens: list):
    query = ''
    
    for i in range(len(tokens)):
            if i + 1 < len(tokens) and tokens[i] == 'search':
                query = " ".join(tokens[i + 1:])
    
    parsed_data = {
        "keyword": "Search",
        "kind": "SEARCH",    
        "target": query,
        "value": None,
        "error": None
        }
    return parsed_data

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
            if i + 1 < len(tokens) and tokens[i + 1].lower() in units:
                value = int(tokens[i])
                unit = tokens[i + 1]
                error = None
                seconds += value * units[unit]
            
        except ValueError:
            error = 'ValueError'
            pass

    parsed_data = {
        "keyword": "Timer",
        "kind": "TIMER",
        "target": None,
        "value": seconds,
        "error": error
    }
    return parsed_data