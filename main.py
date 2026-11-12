import os
import sys
import requests
import random
import string
import time
import threading
from concurrent.futures import ThreadPoolExecutor

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1565543244249436295/RMMJ0TBdDNnX-_Tn5ALUZ4R-ZqfmiWznJ8pvLQc3uq0D_ug0FNT8cbnUNEOe6vpOwJJM"

PINK = '\033[38;5;206m'
PURPLE = '\033[38;5;129m'
CYAN = '\033[38;5;51m'
GREEN = '\033[38;5;118m'
RED = '\033[38;5;196m'
GOLD = '\033[38;5;220m'
BLUE = '\033[38;5;33m'
WHITE = '\033[38;5;15m'
ORANGE = '\033[38;5;208m'
MAGENTA = '\033[38;5;201m'
BPurple = '\033[1;35m'
BWhite = '\033[1;37m'
BBlue = '\033[1;34m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
R = "\x1b[38;5;93m"

Logo = f"""
{R}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
{R}⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉

{BWhite}  ALPHA XK CLOUD TERMINAL (@A_73A3){BWhite} 
{BWhite} ⁂ {BBlue}GITHUB ACTIONS SNIPER{BWhite} ⁂
{BWhite}[{BPurple}={BWhite}]{BBlue} TARGET{BWhite}:{BPurple} TIKTOK
{BWhite}[{BPurple}={BWhite}]{BBlue} STATUS{BWhite}:{BPurple} ACTIVE (24/7)
{BWhite}[{BPurple}={BWhite}]{BBlue} TYPE  {BWhite}:{BPurple} CLOUD WORKER
{BWhite} ⁂ {BBlue}---------------------------------------"""

hits_count = 0
misses_count = 0
lock = threading.Lock()

def clear_screen():
    print('\033c', end='')

def send_to_discord(user, followers=0, mode="Available OG"):
    payload = {
        "username": "ALPHA XK Cloud Sniper",
        "embeds": [{
            "title": f"🎯 HIT! TIKTOK AVAILABLE ({mode})",
            "description": f"**USER:** `@{user}`\n**FOLLOWERS:** `{followers}`\n**LINK:** https://www.tiktok.com/@{user}",
            "color": 5763719,
            "footer": {"text": "GitHub Cloud - ALPHA XK"}
        }]
    }
    try:
        requests.post(DISCORD_WEBHOOK, json=payload, timeout=5)
    except:
        pass

def stats_reporter():
    global hits_count, misses_count
    while True:
        time.sleep(30)
        if hits_count > 0 or misses_count > 0:
            payload = {
                "username": "ALPHA XK Stats",
                "embeds": [{
                    "title": "📊 Live Statistics (Cloud)",
                    "description": f"**HITS:** `{hits_count}`\n**MISSES:** `{misses_count}`\n**STATUS:** Running 24/7...",
                    "color": 3447003,
                    "footer": {"text": "GitHub Cloud - ALPHA XK"}
                }]
            }
            try:
                requests.post(DISCORD_WEBHOOK, json=payload, timeout=5)
            except:
                pass

def log(user):
    global hits_count, misses_count
    url = f"https://www.tiktok.com/api/user/detail/?uniqueId={user}"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        r = requests.get(url, headers=headers, timeout=10)
        
        if r.status_code in [403, 429]:
            time.sleep(2)
            return
            
        if r.status_code == 200:
            data = r.json()
            is_hit = data.get('statusCode') == 10221
        else:
            is_hit = False
    except Exception:
        return

    with lock:
        if is_hit:
            hits_count += 1
            clear_screen()
            print(Logo)
            print(f"""
{GREEN}{BOLD}┌────────────────────────────────────────────────────┐{RESET}
{GREEN}{BOLD}│  {WHITE}✓ HIT! {GREEN}TIKTOK AVAILABLE{RESET}                           │{RESET}
{GREEN}{BOLD}├────────────────────────────────────────────────────┤{RESET}
{GREEN}{BOLD}│  {WHITE}USER     {WHITE}»  {PINK}@{user}{RESET}
{GREEN}{BOLD}├────────────────────────────────────────────────────┤{RESET}
{GREEN}{BOLD}│  {WHITE}GOOD     {WHITE}»  {GREEN}{hits_count}{RESET}
{GREEN}{BOLD}│  {WHITE}BAD      {WHITE}»  {RED}{misses_count}{RESET}
{GREEN}{BOLD}└────────────────────────────────────────────────────┘{RESET}
""")
            send_to_discord(user, 0, "Available OG")
            
        else:
            misses_count += 1
            print(f"{RED}[x] MISS | @{user} | GOOD: {hits_count} | BAD: {misses_count}{RESET}")

def generate_username(length, mode='1'):
    if mode == '1': chars = string.ascii_lowercase + string.digits
    elif mode == '2': chars = string.ascii_lowercase
    elif mode == '3': chars = string.digits
    else: chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=length))

def main():
    clear_screen()
    print(Logo)
    print(f"{CYAN}[*] Starting Cloud Sniper on GitHub Actions...{RESET}")
    
    threading.Thread(target=stats_reporter, daemon=True).start()
    
    end_time = time.time() + (5.5 * 3600)
    
    print(f"{GREEN}[*] Hunting 4-Letter Usernames...{RESET}\n")

    with ThreadPoolExecutor(max_workers=10) as executor:
        while time.time() < end_time:
            user = generate_username(4, '1')
            executor.submit(log, user)
            time.sleep(0.05)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{ORANGE}[!] Stopped.{RESET}")
