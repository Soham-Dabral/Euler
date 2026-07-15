import subprocess
import webbrowser

APPS = {
    "calculator": {"aliases": ["calc", "calculator"], "command": "calc.exe"},
    "calendar": {"aliases": ["calendar"], "command": "outlookcal:"},
    "camera": {"aliases": ["cam", "camera"], "command": "microsoft.windows.camera:"},
    "chrome": {"aliases": ["browser", "chrome", "google"], "command": "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"},
    "clock": {"aliases": ["alarm", "clock"], "command": "timedate.cpl"},
    "discord": {"aliases": ["dc", "discord"], "command": ""},
    "firefox": {"aliases": ["firefox"], "command": "C:/Program Files/Mozilla Firefox/firefox.exe"},
    "microsoft edge": {"aliases": ["edge", "msedge", "tab"], "command": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"},
    "microsoft paint": {"aliases": ["mspaint", "paint"], "command": "mspaint.exe"},
    "notepad": {"aliases": ["notes", "notepad"], "command": "notepad.exe"},
    "minecraft": {"aliases": ["minecraft", "tlauncher"], "command": ""},
    "roblox": {"aliases": ["roblox"], "command": ""},
    "spotify": {"aliases": ["spotify"], "command": "Spotify.exe"},
    "whatsApp": {"aliases": ["whatsapp"], "command": ""}
}

LINKS = {
    "ChatGPT": {"aliases": ["chatgpt"], "URL": "https://chatgpt.com"},
    "Gemini": {"aliases": ["gemini"], "URL": "https://gemini.google.com"},
    "GitHub": {"aliases": ["git", "github"], "URL": "https://github.com"},
    "Gmail": {"aliases": ["gmail", "g-mail", "mail"], "URL": "https://gmail.com"},
    "Instagram": {"aliases": ["insta", "instagram"], "URL": "https://instagram.com"},
    "LinkedIn": {"aliases": ["linkedin"], "URL": "https://linkedin.com"},
    "NetMirror": {"aliases": ["netflix", "netmirror"], "URL": ""},
    "YouTube": {"aliases": ["youtube", "yt"], "URL": "https://youtube.com"}
}

SETTINGS = {
    "apps": {"aliases": ["app", "apps"], "command": "ms-settings:appsfeatures"},
    "bluetooth": {"aliases": ["bluetooth", "bt"], "command": "ms-settings:bluetooth"},
    "display": {"aliases": ["display"], "command": "ms-settings:display"},
    "personalization": {"aliases": ["personalization"], "command": "ms-settings:personalization"},
    "sound": {"aliases": ["sound"], "command": "ms-settings:sound"},
    "wifi": {"aliases": ["internet", "network", "wifi", "wi-fi"], "command": "ms-settings:network-wifi"}
}

def open_apps(app_name):
    for app in APPS:
        aliases = APPS[app]["aliases"]
        command = APPS[app]["command"]
        for alias in aliases:
            for name in app_name:
                if name == alias:
                    subprocess.run([command])
                    return app

def open_links(link_name):
    for link in LINKS:
        aliases = LINKS[link]["aliases"]
        url = LINKS[link]["URL"]
        for alias in aliases:
            for name in link_name:
                if name == alias:
                    webbrowser.open_new_tab(url)
                    return link

def open_settings(settings_name):
    for setting in SETTINGS:
        aliases = SETTINGS[setting]["aliases"]
        command = SETTINGS[setting]["command"]
        for alias in aliases:
            for name in settings_name:
                if name == alias:
                    subprocess.run(["start", command], shell=True, check=True)
                    return setting

def search(query):
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    return query