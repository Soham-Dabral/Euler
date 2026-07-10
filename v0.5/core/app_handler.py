import psutil
import subprocess
import webbrowser

APPS = {
    "Calculator": {"aliases": ["calc", "calculator"], "command": "calc.exe"},
    "Calendar": {"aliases": ["calendar"], "command": "outlookcal:"},
    "Camera": {"aliases": ["cam", "camera"], "command": "microsoft.windows.camera:"},
    "Clock": {"aliases": ["alarm", "clock"], "command": "timedate.cpl"},
    "Discord": {"aliases": ["dc", "discord"], "command": ""},
    "Firefox": {"aliases": ["firefox"], "command": "C:/Program Files/Mozilla Firefox/firefox.exe"},
    "Microsoft Edge": {"aliases": ["browser", "edge", "msedge", "tab"], "command": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"},
    "Microsoft Paint": {"aliases": ["mspaint", "paint"], "command": "mspaint.exe"},
    "Notepad": {"aliases": ["notes", "notepad"], "command": "notepad.exe"},
    "Minecraft": {"aliases": ["minecraft", "tlauncher"], "command": ""},
    "Roblox": {"aliases": ["roblox"], "command": ""},
    "Spotify": {"aliases": ["spotify"], "command": "Spotify.exe"},
    "WhatsApp": {"aliases": ["whatsapp"], "command": ""}
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
    "Apps": {"aliases": ["app", "apps"], "command": "ms-settings:appsfeatures"},
    "Bluetooth": {"aliases": ["bluetooth", "bt"], "command": "ms-settings:bluetooth"},
    "Display": {"aliases": ["display"], "command": "ms-settings:display"},
    "Personalization": {"aliases": ["personalization"], "command": "ms-settings:personalization"},
    "Sound": {"aliases": ["sound"], "command": "ms-settings:sound"},
    "Wifi": {"aliases": ["internet", "network", "wifi", "wi-fi"], "command": "ms-settings:network-wifi"}
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
            
def close_apps(app_name):
    for app in APPS:
        aliases = APPS[app]["aliases"]
        command = APPS[app]["command"]
        for alias in aliases:
            for name in app_name:
                if name == alias:
                    for process in psutil.process_iter(["name"]):
                        if process.info["name"] in command:
                            process.terminate()
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

def close_links(link_name):
    all_links = []
    for link in LINKS:
        all_links.append(LINKS[link])
    
    from playwright.sync_api import sync_playwright
    with sync_playwright() as web:
        browser = web.chromium.connect_over_cdp("http://localhost:9222")
    
    for context in browser.contexts:
        for page in context.pages:
            for link in link_name:
                for metadata in all_links:
                    if link in metadata["aliases"] and metadata["url"] in page.url:
                        page.close()
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

def close_settings(settings_name):
    ...

def search(query):
    webbrowser.open_new_tab(f"https://www.bing.com/search?q={query}")
    return query