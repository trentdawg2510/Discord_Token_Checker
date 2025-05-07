import httpx, threading, os, json, random, base64, datetime, time
from colorama import Fore
from pathlib import Path
from math import *
import ctypes
import sys
import requests
import binascii
import platform
import subprocess
import hashlib
from keyauth import *
import json as jsond
from uuid import uuid4
# from Crypto.Cipher import AES
# from Crypto.Hash import SHA256
# from Crypto.Util.Padding import pad, unpad

def cls(): #clears the terminal
    os.system('cls' if os.name =='nt' else 'clear')

      
if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f"Token Checker")
else:
    pass

config = json.load(open("config.json", encoding="utf-8"))

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name = "",
    ownerid = "",
    secret = "",
    version = "",
    hash_to_check = getchecksum()
)

if keyauthapp.checkblacklist():
    print(Fore.RED + "You are blacklisted from our system." + Fore.RESET)
    quit()

os.system('cls')
      
def answer():
    try:
        print(Fore.LIGHTBLUE_EX+ """
              
"""+ Fore.RESET)  
        print(Fore.WHITE + "                              [1] Login                                [2] Register"     + Fore.RESET)                                                                                                                                       

        ans = input("Select Option: ")
        if ans == "1":
            user = input('Username: ')
            password = input('Password: ')
            keyauthapp.login(user, password)
        elif ans == "2":
            user = input('Username: ')
            password = input('Password: ')
            license = input('License: ')
            keyauthapp.register(user, password, license)
        elif ans == "3":
            user = input('Username: ')
            license = input('License: ')
            os.system('start chrome https://discord.gg/')
            print("                                                     ")                                             
            print(Fore.LIGHTBLUE_EX+("Make A Ticket In The Discord To Upgrade Your License.")
            + Fore.RESET)
            os._exit(1)
        else:
            print("\nNot Valid Option")
            time.sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)


answer()

os.system('cls')

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f"Menu")
else:
    pass
    
l = {
    "threads": 50,
    "thread_wait_time": 1,
    "proxyless": True,
    "1m_tokens_threshold": 5,
    "3m_tokens_threshold": 10,
    "clear_output_files": True,
}

if not os.path.exists("config.json"):
    json_object = json.dumps(l, indent=4)
    with open("config.json", "w") as outfile:
        outfile.write(json_object)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
cls()

def timestamp():
    timestamp = f"{Fore.RESET}{Fore.LIGHTMAGENTA_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
    return timestamp
 
 
def sprint(message, type:bool): #prints 
    if type == True:
        print(f"{Fore.RESET}[{Fore.MAGENTA}{timestamp()}{Fore.RESET}][{Fore.GREEN}/{Fore.RESET}]{message}{Fore.RESET}")
    if type == False:
        print(f"{Fore.RESET}[{Fore.MAGENTA}{timestamp()}{Fore.RESET}][{Fore.GREEN}/{Fore.RESET}]{message}{Fore.RESET}")
        
def checkEmpty(filename): #checks if the file passed is empty or not
    mypath = Path(filename)
 
    if mypath.stat().st_size == 0:
        return True
    else:
        return False
 
def write(content:str, filename: str):
    open(filename, "a").write(f"{content}\n")
    
    
def get_all_tokens(filename:str): #returns all tokens in a file as token from email:password:token
    all_tokens = []
    for j in open(filename, "r").read().splitlines():
        if ":" in j:
            j = j.split(":")[2]
            all_tokens.append(j)
        else:
            all_tokens.append(j)
 
    return all_tokens


def getproxy():
    if config['proxyless'] == False:
        proxy = random.choice(open("input/proxies.txt", "r").read().splitlines())
        return {'http://': f'http://{proxy}', 'https://': f'http://{proxy}'}
    else:
        pass


class data:
    other = 0; valid = 0; valid_lst = []; one_month_tokens = 0; invalid = 0; used = 0; locked = 0; no_nitro = 0; three_month_tokens = 0; checked = 0; sorted = 0
     
def get_super_properties():
    properties = '''{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-GB","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36","browser_version":"95.0.4638.54","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":102113,"client_event_source":null}'''
    properties = base64.b64encode(properties.encode()).decode()
    return properties


def get_fingerprint(s):
    try:
        fingerprint = s.get(f"https://discord.com/api/v9/experiments", timeout=5).json()["fingerprint"]
        return fingerprint
    except Exception as e:
        return "Error"


def get_cookies(s, url):
    try:
        cookieinfo = s.get(url, timeout=5).cookies
        dcf = str(cookieinfo).split('__dcfduid=')[1].split(' ')[0]
        sdc = str(cookieinfo).split('__sdcfduid=')[1].split(' ')[0]
        return dcf, sdc
    except:
        return "", ""
    
    
def get_headers(token):
    while True:
        proxy = getproxy()
        s = httpx.Client(proxies=proxy)
        dcf, sdc = get_cookies(s, "https://discord.com/")
        fingerprint = get_fingerprint(s)
        if fingerprint != "Error":
            break
    super_properties = get_super_properties()
    headers = {
        'authority': 'discord.com',
        'method': 'POST',
        'path': '/api/v9/users/@me/channels',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US',
        'authorization': token,
        'cookie': f'__dcfduid={dcf}; __sdcfduid={sdc}',
        'origin': 'https://discord.com',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-fingerprint': fingerprint,
        'x-super-properties': super_properties,
    }
    return s, headers


def validate_token(s, headers):
    try:
        check = s.get(f"https://discord.com/api/v9/users/@me", headers=headers)
        if check.status_code == 200:
            profile_name = check.json()["username"]
            profile_discrim = check.json()["discriminator"]
            profile_of_user = f"{profile_name}#{profile_discrim}"
            return profile_of_user
        else:
            return False
    except Exception as e:
        validate_token(s, headers)
    
def get_full_token(token:str):
    filename = "input/tokens.txt"
    all_tokens = get_all_tokens(filename)
    all_tokens_full = open(filename, "r").read().splitlines()
    index = all_tokens.index(token)
    return all_tokens_full[index]

used = f"{Fore.RESET}[{Fore.RED}USED{Fore.RESET}]{Fore.RESET}"
unlocked = f"{Fore.RESET}[{Fore.GREEN}UNLOCKED{Fore.RESET}]{Fore.RESET}"
subbed = f"{Fore.RESET}[{Fore.GREEN}SUBBED{Fore.RESET}]{Fore.RESET}"
locked = f"{Fore.RESET}[{Fore.RED}LOCKED{Fore.RESET}]{Fore.RESET}"
invalid = f"{Fore.RESET}[{Fore.RED}INVALID{Fore.RESET}]{Fore.RESET}"
nosubbed = f"{Fore.RESET}[{Fore.GREEN}NOT_SUBBED{Fore.RESET}]{Fore.RESET}"



def checktoken(token):
    try:
        s, headers = get_headers(token)
        profile = validate_token(s, headers)

        if profile != False:

            boost_data = s.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers={'Authorization': token})
            if boost_data.status_code == 403:
                sprint(f"{Fore.BLUE} Checked Token: {token[:39]}, Flags: {Fore.RESET}{locked}{Fore.RESET}", False)
                data.locked += 1; data.checked += 1
                token = get_full_token(token)
                write(token, "output/locked.txt")
                return False
                

            if len(boost_data.json()) != 0 and boost_data.status_code == 200 or boost_data.status_code == 201:
                if boost_data.json()[0]['cooldown_ends_at'] != None:
                    sprint(f"{Fore.BLUE} Checked Token: {token[:39]}, Flags: {Fore.RESET}{used}{Fore.RESET}, {Fore.RESET}{unlocked}{Fore.RESET}, {subbed}{Fore.RESET}", False)
                    data.used += 1; data.checked += 1
                    token = get_full_token(token)
                    write(token, "output/used.txt")
                    return False


            if len(boost_data.json()) == 0 and boost_data.status_code == 200 or boost_data.status_code == 201:
                sprint(f"{Fore.BLUE} Checked Token: {token[:39]}, Flags: {Fore.RESET}{unlocked}{Fore.RESET}, {Fore.RESET}{nosubbed}{Fore.RESET}", True)
                data.no_nitro += 1; data.checked += 1
                token = get_full_token(token)
                write(token, "output/unlocked.txt")
                return False

            else:
                if len(boost_data.json()) != 0 and boost_data.status_code == 200 or boost_data.status_code == 201:
                    if boost_data.json()[0]['cooldown_ends_at'] == None:
                        sprint(f"{Fore.BLUE} Checked Token: {token[:39]}, Flags: {Fore.RESET}{subbed}{Fore.RESET}, {unlocked}{Fore.RESET}", True)
                        data.valid_lst.append(token)
                        data.valid += 1; data.checked += 1
                        token = get_full_token(token)
                        write(token, "output/valid.txt")
                        return True
                        
        else:
            sprint(f"{Fore.BLUE} Checked Token: {token[:39]}, Flags: {Fore.RESET}[{Fore.RED}INVALID{Fore.RESET}]", False)
            data.invalid += 1; data.checked += 1
            token = get_full_token(token)
            write(token, "output/invalid.txt")
            return False
            
    except Exception as e:
        print(e)
        checktoken(token)
        
        
def sorter(token):
    try:
        s, headers = get_headers(token)
        nitro_data = s.get(f"https://discord.com/api/v9/users/@me/billing/subscriptions", headers={'Authorization': token})
        if nitro_data.status_code in [200, 201]:
            
            end = datetime.datetime.strptime(nitro_data.json()[0]['current_period_end'],'%Y-%m-%dT%H:%M:%S.%f%z')
            current = datetime.datetime.now(datetime.timezone.utc)
            left = end - current
            left = str(left)
            days_left = left.split("days")[0]
            days_left = int(days_left)
            if days_left <= 30:
                if days_left >= 30-config['1m_tokens_threshold']:
                    xs = "*"*(len(token) - 30)
                    sprint(f"{Fore.LIGHTBLUE_EX}token={Fore.WHITE}{token[:30]} | {days_left} days left", True)
                    data.one_month_tokens += 1
                    data.sorted += 1
                    token = get_full_token(token)
                    write(token, "output/sorted/valid_1m_tokens.txt")
                elif days_left < 30-config['1m_tokens_threshold']:
                    xs = "*"*(len(token) - 30)
                    sprint(f"{Fore.LIGHTBLUE_EX}token={Fore.WHITE}{token[:30]} | {days_left} days left", False)
                    data.other += 1
                    data.sorted += 1
                    token = get_full_token(token)
                    write(f"{token}, expires = {days_left} days", "output/sorted/other.txt")
            elif days_left <= 90:
                if days_left >= 90-config['3m_tokens_threshold']:
                    xs = "*"*(len(token) - 30)
                    sprint(f"{Fore.LIGHTBLUE_EX}token={Fore.WHITE}{token[:30]} | {days_left} days left", True)
                    data.three_month_tokens += 1
                    data.sorted += 1
                    token = get_full_token(token)
                    write(token, "output/sorted/valid_3m_tokens.txt")
                elif days_left < 90-config['3m_tokens_threshold']:
                    xs = "*"*(len(token) - 30)
                    sprint(f"{Fore.LIGHTBLUE_EX}token={Fore.WHITE}{token[:30]}... | {days_left} days left", False)
                    data.other += 1
                    data.sorted += 1
                    token = get_full_token(token)
                    write(f"{Fore.LIGHTBLUE_EX}token={Fore.WHITE}{token[:30]}, expires = {days_left} days", "output/sorted/other.txt")
        else:
            xs = "*"*(len(token) - 30)
            sprint(f"err: no nitro/locked/used {Fore.LIGHTBLUE_EX}token={Fore.WHITE}{token[:30]}", True)
    except Exception as e:
        print(e)
        sorter(token)
        
        
        
        
def clearfile(filename):
    try:
        open(filename, "w").write("")
    except Exception as e:
        pass
    
    
def removeDuplicates(filename:str): #removes duplicates from a file
    all_tokens = open(filename, "r").read().splitlines()
    without_duplicates = []
    for i in all_tokens:
        if i not in without_duplicates:
            without_duplicates.append(i)
    open(filename, "w").write("")
    for line in without_duplicates:
        open(filename, "a").write(f"{line}\n")
    return len(without_duplicates)
        
if __name__ == '__main__':
    
    if os.path.exists("input/") == False:
        os.mkdir("input/")
        open("input/tokens.txt", "w").write("")
        open("input/proxies.txt", "w").write("")
    if os.path.exists("output/") == False:
        os.mkdir("output/")
        os.mkdir("output/sorted/")
        
    cls()
    if checkEmpty("input/tokens.txt"):
        sprint("No tokens to check. Input some tokens in input/tokens.txt to start checking tokens.", False)
        quit()
        
    original_len = len(get_all_tokens("input/tokens.txt"))
    new_len = removeDuplicates("input/tokens.txt")
    duplicates_removed = original_len - new_len
    if duplicates_removed > 0:
        sprint(f"Removed {duplicates_removed} duplicates in input/tokens.txt", True)
        
    if config['clear_output_files']:
        clearfile("output/invalid.txt")
        clearfile("output/locked.txt")
        clearfile("output/used.txt")
        clearfile("output/valid.txt")
        clearfile("output/sorted/other.txt")
        clearfile("output/sorted/valid_1m_tokens.txt")
        clearfile("output/sorted/valid_3m_tokens.txt")
        clearfile("output/unlocked.txt")
    
    tokens = get_all_tokens("input/tokens.txt")
    tokens_thread = []
    
    for i in range(trunc(len(tokens)/config['threads'])):
        hm = []
        for i in range(config['threads']):
            hm.append(tokens[0])
            tokens.pop(0)
        tokens_thread.append(hm)
    tokens_thread.append(tokens)
    
    for l in tokens_thread:
        threads = []
        numTokens = len(l)
        for i in range(numTokens):
            token = l[i]
            t = threading.Thread(target=checktoken, args=(token, ))
            t.daemon = True
            threads.append(t)
        for i in range(numTokens):
            threads[i].start()
        for i in range(numTokens):
            threads[i].join()

        time.sleep(config['thread_wait_time'])
        
    #cls()
    print()
    if len(data.valid_lst) != 0:
        sprint("Sorting Tokens", True)
        working_thread = []
        working_tokens = data.valid_lst
        for i in range(trunc(len(working_tokens)/config['threads'])):
            hm = []
            for i in range(config['threads']):
                hm.append(working_tokens[0])
                working_tokens.pop(0)
            working_thread.append(hm)

        working_thread.append(working_tokens)

        for l in working_thread:
            threads = []
            numTokens = len(l)
            for i in range(numTokens):
                token = l[i]
                t = threading.Thread(target=sorter, args=(token, ))
                t.daemon = True
                threads.append(t)
            for i in range(numTokens):
                threads[i].start()
            for i in range(numTokens):
                threads[i].join()

            time.sleep(config['thread_wait_time'])
    else:
        print()

    sprint(f" Checked: {data.checked} token(s)", True)
    sprint(f" Nitro tokens: {data.valid} | Used: {data.used} | Unlocked: {data.no_nitro} | Locked: {data.locked} | Invalid: {data.invalid}", True)
    print()
    sprint(f" Sorted: {data.sorted} | 1 Month Nitro Tokens: {data.one_month_tokens} | 3 Months Nitro Tokens: {data.three_month_tokens} | Other Nitro Tokens: {data.other}", True)

    input()
    quit()