import os
from sys import *
from colorama import *
import time


#CREADO POR GEERXOS GITHUB: https://github.com/GeerxOS


# Exploits

from exploit.win_vlc import win_vlc
from exploit.adobe_pdf import adobe_exe

# Auxiliarys

from auxiliarys.search_domains import search_sdomains
from auxiliarys.search_gmails import search_email

# Meterpreter

#iOS Meterpreter

from ios.aarch64_http import ios64_http
from ios.aarch64_tcp import ios64_tcp
from ios.armle_http import armle_http
from ios.armle_tcp import armle_tcp

# Android Meterpreter

from meterpreter.android.and_http import and_http
from meterpreter.android.and_tcp import and_tcp

# Linux meterpreter

from meterpreter.linux.li_py import li_py
from meterpreter.linux.li64_http import li64_http
from meterpreter.linux.li64_tcp import li64_tcp
from meterpreter.linux.li86_http import li86_http
from meterpreter.linux.li86_tcp import li86_tcp

# Windows meterpreter

from meterpreter.windows.wind_http import wind_http
from meterpreter.windows.wind_py import wind_py
from meterpreter.windows.wind_tcp import wind_tcp

# Netcat

# Android NetCat
from netcat.android.and_net_http import and_net_http
from netcat.android.and_net_tcp import and_net_tcp

# Linux NetCat

from netcat.linux.li_net_py import li_net_py

# Windows NetCat

from netcat.windows.win_net_http import win_net_http
from netcat.windows.win_net_tcp import win_net_tcp
from netcat.windows.win_net_udp import win_net_udp

# Banners
help="""


 /'\_/`\          /'___\ 
/\      \    ____/\ \__/ 
\ \ \__\ \  /',__\ \ ,__|
 \ \ \_/\ \/\__, `\ \ \_/                 
  \ \_\\ \_\/\____/\ \_\ 
   \/_/ \/_/\/___/  \/_/ 

+------------------------------------------------+
|               Commands                         |
| Command          | Description                 |  
| use              | Use a module                |
| help             | Show available commands.    |
| exit             | Finish the script.          |
| update           | Update the script.          |
| show all         | Show all Modules.           |
| install          | Add the tool to the terminal|
+------------------------------------------------+

/\  _`\ /\ \            /\_ \  /\_ \     
\ \,\L\_\ \ \___      __\//\ \ \//\ \    
 \/_\__ \\ \  _ `\  /'__`\\ \ \  \ \ \   
   /\ \L\ \ \ \ \ \/\  __/ \_\ \_ \_\ \_ 
   \ `\____\ \_\ \_\ \____\/\____\/\____|
    \/_____/\/_/\/_/\/____/\/____/\/____/

"""

ban="""

 /$$      /$$            /$$$$$$       /$$$$$$  /$$                 /$$ /$$
| $$$    /$$$           /$$__  $$     /$$__  $$| $$                | $$| $$
| $$$$  /$$$$  /$$$$$$$| $$  \__/    | $$  \__/| $$$$$$$   /$$$$$$ | $$| $$
| $$ $$/$$ $$ /$$_____/| $$$$ /$$$$$$|  $$$$$$ | $$__  $$ /$$__  $$| $$| $$
| $$  $$$| $$|  $$$$$$ | $$_/|______/ \____  $$| $$  \ $$| $$$$$$$$| $$| $$
| $$\  $ | $$ \____  $$| $$           /$$  \ $$| $$  | $$| $$_____/| $$| $$
| $$ \/  | $$ /$$$$$$$/| $$          |  $$$$$$/| $$  | $$|  $$$$$$$| $$| $$
|__/     |__/|_______/ |__/           \______/ |__/  |__/ \_______/|__/|__/

GeerxOS                                                              GeerxOS
       GeerxOS                                                GeerxOS                                                                      
"""

credits="""

+-----------------------+
|Created By GeerxOS     |  
|=======================|
|Telegram: t.me/geraaxd |
|=======================|
|Discord: Geerx#5380    |
|=======================|
|TikTok: whois_.gerx    |
|=======================|
|Instagram: whois_.gerx |
|=======================|
|YouTube: Geras !       |
+=======================+

"""


winpayloads="""

+-------------------------------------+ 
|          Windows Payloads           | 
| [1] windows/meterpreter/reverse_tcp |
|                                     |
| [2] windows/meterpreter/reverse_http| 
|                                     | 
| [3] python/meterpreter/reverse_tcp  |  
|=====================================|  
|            Netcat                   | 
| [4] windows/shell/reverse_tcp       |  
|                                     |  
| [5]windows/shell/reverse_udp        |  
|                                     |  
| [6] python/shell_reverse_tcp        |  
+-------------------------------------+

[0] Back

"""

linpayloads="""

+---------------------------------------+
|        Linux Payloads                 |
| [1] linux/x86/meterpreter/reverse_tcp |
|                                       |
| [2] linux/x86/meterpreter_reverse_http|
|                                       |
| [3] linux/x64/meterpreter/reverse_tcp |
|                                       |
| [4] linux/x64/meterpreter_reverse_http|
|                                       |
| [5] python/meterpreter/reverse_tcp    |
|=======================================|
|              Netcat                   |
| [6] python/shell_reverse_tcp          |
+---------------------------------------+

[0] Back

"""

andpayloads="""

+-------------------------------------+
|       Android Payloads              |  
|                                     |
| [1] android/meterpreter/reverse_tcp | 
|                                     | 
| [2] android/meterpreter/reverse_http|
|=====================================|
|           Netcat                    | 
| [3] android/shell/reverse_tcp       | 
|                                     | 
| [4] android/shell/reverse_http      |
+-------------------------------------+ 

[0] Back

"""
iospayloads="""

+-------------------------------------------------+
|              iOS Payloads                       |  
|                                                 |
| [1] apple_ios/aarch64/meterpreter_reverse_http  | 
|                                                 | 
| [2] apple_ios/aarch64/meterpreter_reverse_tcp   |
|                                                 |
| [3] apple_ios/armle/meterpreter_reverse_http    |
|                                                 |
| [4] apple_ios/armle/meterpreter_reverse_tcp     |
|                                                 |
+-------------------------------------------------+

[0] Back

"""

auxiliarys="""

+---------------------------------------------------------+
|                 Auxiliarys                              |
|                                                         |
| [1] auxiliary/gather/searchengine_subdomains_collector  |
|                                                         |
| [2] auxiliary/gather/search_email_collector             |
|                                                         |
+---------------------------------------------------------+

[0] Back

"""

exploits="""

+-----------------------------------------------------------+ 
|                     Exploits                              | 
|                                                           |
| [1]      exploit/windows/fileformat/vlc_mkv               | 
|                                                           |
| [2] exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs| 
|                                                           | 
+-----------------------------------------------------------+ 

[0] Back

"""

def back():
    os.system("clear")
    bannerp()
    msfshell()

# Script principal

def bannerp():
    print(" ")
    print(" ")
    print(Fore.WHITE + (ban))
    print(" ")
    print("=== !Payloads! ===")
    print(" ")
    print(Fore.BLUE + "[1] Windows")
    print(Fore.BLUE + "[2] Linux")
    print(Fore.BLUE + "[3] Android")
    print(Fore.BLUE + "[4] Apple iOS")
    print(" ")
    print(Fore.WHITE + "=== !Extra modules! ===")
    print(" ")
    print(Fore.BLUE + "[5] Auxiliarys")
    print(Fore.BLUE + "[6] Exploits")
    print("")
    print(Fore.BLUE + "[01] Extra")
    print(Fore.BLUE  + "[0] Exit")
    print(" ")

def msfshell():

    opc = input(Fore.GREEN + "MsfShell:~# ")

    if opc == "credits":
        os.system("clear")
        print(credits)
        input("--> ")
        msfshell()

    if opc == "exit":
        exit()

    if opc == "clear":
        back()

    if opc == "ls":
        os.system("ls")
        msfshell()

    if opc == "01":
        os.system("clear")
        os.chdir("extra")
        os.system("python3 extra.py")
        os.chdir("..")
        back()

    if opc == "help":
        os.system("clear")
        print(help)
        input("--> ")
        msfshell()

    if opc == "1":
        os.system("clear")
        os.system("figlet -f banner Windows")
        print(Fore.BLUE + (winpayloads))

        win = input(Fore.BLUE + "MsfShell:~/Windows# ")

        if win == "1":
            wind_tcp()
            back()

        if win == "2":
            wind_http()
            back()
        
        if win == "3":
            wind_py()
            back()

        if win == "4":
            win_net_tcp()
            back()

        if win == "5":
            win_net_udp()
            back()

        if win == "6":
            win_net_http()
            back()

        if win == "0":
            back()

        else:
            back()

    if opc == "2":
        os.system("clear")
        os.system("figlet -f banner Linux")
        print(Fore.BLUE + (linpayloads))

        lin = input(Fore.BLUE + "MsfShell:~/Linux# ")

        if lin == "1":
            li86_tcp()
            back()

        if lin == "1":
            li86_http()
            back()

        if lin == "3":
            li64_tcp()
            back()

        if lin == "4":
            li64_http()
            back()

        if lin == "5":
            li_py()
            back()

        if lin == "6":
            li_net_py()
            back()

        if lin == "0":
            os.system("clear")
            back()

        else:
            back

    if opc == "3":
        os.system("clear")
        os.system("figlet -f banner Android")
        print(Fore.BLUE + (andpayloads))

        andr = input(Fore.BLUE + "MsfShell:~/Linux# ")

        if andr == "1":
            and_tcp()
            back()

        if andr == "2":
            and_http()
            back()

        if andr == "3":
            and_net_tcp()
            back()

        if andr == "4":
            and_net_http()
            back()

        if andr == "0":
            os.system("clear")
            back()

        else:
            back()

    if opc == "4":
        os.system("clear")
        os.system("figlet -f banner iOS ")
        print(Fore.BLUE + (iospayloads))

        ios = input(Fore.BLUE + "MsfShell:~/iOS ")

        if ios == "1":
            ios64_http()
            back()

        if ios == "2":
            ios64_tcp()
            back()

        if ios == "3":
            armle_http()
            back()

        if ios == "4":
            armle_tcp()
            back()

        if ios == "0":
            back()

        else:
            back()
    

    if opc == "5":
        os.system("clear")
        os.system("figlet -f banner Auxiliarys")
        print(Fore.BLUE + (auxiliarys))

        aux = input(Fore.BLUE + "MsfShell:~/Auxiliarys# ")

        if aux == "1":
            search_sdomains()
            back()

        if aux == "2":
            search_email()
            back()

        if aux == "0":
            os.system("clear")
            back()

        else:
            os.system("clear")
            back()

    if opc == "6":
        os.system("clear")
        os.system("figlet -f banner Exploits")
        print(Fore.BLUE + (exploits))

        exp = input(Fore.BLUE + "MsfShell:~/Exploits# ")

        if exp == "1":
            win_vlc()
            back()

        if exp == "2":
            adobe_exe()
            back()

        if exp == "0":
            back()

        else:
            back()

    if opc == "0":
        exit()

    else:
        print("[MsfShell] "+opc+" Is not a command!!")
        time.sleep(2)
        msfshell()

if __name__ == '__main__':
    try:
        Fore.WHITE
        print("Created by gerx")
        print(" ")
        if input(Fore.RED + "Do you want to continue? y/n --> ") == "y":
            os.system("clear")
            Fore.BLUE
            back()

    except(KeyboardInterrupt):
        print("\nCTRL+C Detected!, force program to stop\n")
        print("Good bye")
        os.system("rm -rf __pycache__")
        exit()

back()
