# Bot Token Validator with SlowType & Gradient
# Styled like AirFlow Nuker
# Author: Adapted for AirFlow by ChatGPT

import requests
import os
from pystyle import Write, Colors, Colorate, Anime, System
from time import sleep

os.system('mode con: cols=120 lines=35')
System.Title("AirFlow Bot Token Checker")
System.Clear()

banner = r"""
 /$$$$$$$              /$$           /$$$$$$            /$$$$$$         
| $$__  $$            | $$          |_  $$_/           /$$__  $$        
| $$  \ $$  /$$$$$$  /$$$$$$          | $$   /$$$$$$$ | $$  \__//$$$$$$ 
| $$$$$$$  /$$__  $$|_  $$_/          | $$  | $$__  $$| $$$$   /$$__  $$
| $$__  $$| $$  \ $$  | $$            | $$  | $$  \ $$| $$_/  | $$  \ $$
| $$  \ $$| $$  | $$  | $$ /$$        | $$  | $$  | $$| $$    | $$  | $$
| $$$$$$$/|  $$$$$$/  |  $$$$/       /$$$$$$| $$  | $$| $$    |  $$$$$$/
|_______/  \______/    \___/        |______/|__/  |__/|__/     \______/  
"""

Anime.Fade(banner, Colors.blue_to_purple, Colorate.Vertical, enter=True)
sleep(1.5)
System.Clear()

Write.Print(banner + "\n", Colors.blue_to_purple, interval=0.0015)

def get_bot_info(token):
    base_url = "https://discord.com/api/v10"
    headers = {
        "Authorization": f"Bot {token}"
    }

    res = requests.get(f"{base_url}/users/@me", headers=headers)

    if res.status_code == 200:
        bot = res.json()
        Write.Print("[+] Token is VALID!\n", Colors.blue_to_purple, interval=0.0015)
        Write.Print(f"[+] Bot Username : {bot['username']}#{bot['discriminator']}\n", Colors.blue_to_purple, interval=0.0015)
        Write.Print(f"[+] Bot ID       : {bot['id']}\n", Colors.blue_to_purple, interval=0.0015)
        Write.Print(f"[+] Bot Avatar   : https://cdn.discordapp.com/avatars/{bot['id']}/{bot['avatar']}.png\n", Colors.blue_to_purple, interval=0.0015)

        Write.Print("\n[~] Fetching guilds...\n", Colors.blue_to_purple, interval=0.0015)
        g_res = requests.get(f"{base_url}/users/@me/guilds", headers=headers)

        if g_res.status_code == 200:
            guilds = g_res.json()
            if not guilds:
                Write.Print("[-] Bot is not in any guilds.\n", Colors.blue_to_purple, interval=0.0015)
            else:
                Write.Print(f"[+] Bot is in {len(guilds)} guild(s):\n", Colors.blue_to_purple, interval=0.0015)
                for g in guilds:
                    name = g.get('name', 'Unknown Server')
                    gid = g.get('id', 'N/A')
                    Write.Print(f"    • {name} | ID: {gid}\n", Colors.blue_to_purple, interval=0.001)
        else:
            Write.Print(f"[!] Failed to fetch guilds: {g_res.status_code}\n", Colors.blue_to_purple, interval=0.0015)
    elif res.status_code == 401:
        Write.Print("[-] Invalid bot token (401 Unauthorized)\n", Colors.blue_to_purple, interval=0.0015)
    else:
        Write.Print(f"[!] Unexpected error: {res.status_code}\n", Colors.blue_to_purple, interval=0.0015)
        print(res.text)

token = Write.Input("\n[>] Bot Token: ", Colors.blue_to_purple, interval=0.0015)
print()
get_bot_info(token)

input("\nPress Enter to exit...")
