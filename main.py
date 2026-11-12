import os
import requests
import random
import string
import time
import asyncio
import aiohttp

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1565543244249436295/RMMJ0TBdDNnX-_Tn5ALUZ4R-ZqfmiWznJ8pvLQc3uq0D_ug0FNT8cbnUNEOe6vpOwJJM"

PINK = '\033[38;5;206m'
CYAN = '\033[38;5;51m'
GREEN = '\033[38;5;118m'
RED = '\033[38;5;196m'
ORANGE = '\033[38;5;208m'
WHITE = '\033[38;5;15m'
RESET = '\033[0m'
BOLD = '\033[1m'

Logo = f"""
{CYAN} ALPHA XK CLOUD SNIPER (HYPER SPEED)
{WHITE} ⁂------------------------------⁂
{ORANGE} [*] Threads: 100 (Asynchronous)
{ORANGE} [*] Mode: Multi-Platform Fast
{WHITE} ⁂------------------------------⁂"""

hits_count = 0
misses_count = 0

def clear_screen():
    print('\033c', end='')

def send_to_discord(user):
    payload = {
        "username": "ALPHA XK Hyper Sniper",
        "embeds": [{
            "title": f"🎯 HIT! TIKTOK AVAILABLE",
            "description": f"**USER:** `@{user}`\n**LINK:** https://www.tiktok.com/@{user}",
            "color": 5763719,
            "footer": {"text": "Cloud Hyper Speed - ALPHA XK"}
        }]
    }
    try:
        requests.post(DISCORD_WEBHOOK, json=payload, timeout=5)
    except: pass

async def check_user(session, user, sem):
    global hits_count, misses_count
    async with sem:
        url = f"https://www.tiktok.com/api/user/detail/?uniqueId={user}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        try:
            async with session.get(url, headers=headers, timeout=5) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get('statusCode') == 10221:
                        hits_count += 1
                        print(f"{GREEN}[+] HIT: @{user} | Total: {hits_count}{RESET}")
                        send_to_discord(user)
                    else:
                        misses_count += 1
                        print(f"{RED}[x] MISS: @{user} | Total: {misses_count}{RESET}")
        except:
            pass

async def stats_reporter():
    while True:
        await asyncio.sleep(30)
        payload = {
            "username": "ALPHA XK Stats",
            "embeds": [{
                "title": "📊 Hyper Speed Stats",
                "description": f"**HITS:** `{hits_count}`\n**MISSES:** `{misses_count}`\n**STATUS:** Mach 10...",
                "color": 3447003
            }]
        }
        try: requests.post(DISCORD_WEBHOOK, json=payload, timeout=5)
        except: pass

async def main():
    clear_screen()
    print(Logo)
    
    # تشغيل مراسل الإحصائيات
    asyncio.create_task(stats_reporter())
    
    # السرعة الخارقة: 100 مسار
    sem = asyncio.Semaphore(100)
    end_time = time.time() + (5.5 * 3600)
    
    # تمرير الطول من جيت هاب (افتراضياً 4)
    length = int(os.environ.get("USER_LENGTH", 4))

    print(f"{GREEN}[*] Starting Hyper Speed Sniper with 100 Threads...{RESET}\n")

    async with aiohttp.ClientSession() as session:
        tasks = []
        while time.time() < end_time:
            user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
            task = asyncio.create_task(check_user(session, user, sem))
            tasks.append(task)
            
            # تنظيف المهام القديمة عشان الرام ما يمتلئ
            if len(tasks) > 1000:
                await asyncio.gather(*tasks)
                tasks = []

if __name__ == "__main__":
    asyncio.run(main())