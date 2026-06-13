import subprocess

APPS = {
    "Calculator": {"aliases": ["calculator", "calc"], "function": "calc.exe"},
    "Calendar":{"aliases": ["calendar"], "function": "outlookcal:"},
    "Camera": {"aliases": ["camera", "cam"], "function": "microsoft.windows.camera:"},
    "Clock": {"aliases": ["clock", "alarm"], "function": "timedate.cpl"},
    "Discord": {"aliases": ["discord", "dc"], "function": "Discord.Ink"},
    "Firefox": {"aliases": ["firefox"], "function": r"C:\Program Files\Mozilla Firefox\firefox.exe"},
    "LinkedIn": {"aliases": ["linkedin"], "function": "https://linkedin.com"},
    "Microsoft Edge": {"aliases": ["browser", "microsoft edge", "edge", "msedge"], "function": "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"},
    "Minecraft": {"aliases": ["minecraft", "tlauncher"], "function": "Tlauncher.exe"},
    "Roblox": {"aliases": ["roblox"], "function": "RobloxPlayerBeta.exe"},
    "Spotify": {"aliases": ["spotify"], "function": "Spotify.exe"},
    "WhatsApp": {"aliases": ["whatsapp"], "function": "WhatsApp.exe"}
}

def open_apps(app_name: str):
    requested_apps = []
    for app in APPS:
        requested_apps.append(APPS[app])
    
    for app in requested_apps:
        aliases = app["aliases"]
        command = app["function"]
        if app_name in aliases:
            subprocess.run([command])
            return  app_name