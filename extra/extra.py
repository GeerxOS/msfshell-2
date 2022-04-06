import os

from colorama import *

#Script

from asp_tcp import asptcp
from bash import bash
from jsp import jsp
from perl import perl
from py_shell import py_shell
from war_jsp import war

# Java

from java.java_http import java_http
from java.java_tcp import java_tcp
from java.java_shell_http import java_shell_http
from java.java_shell_tcp import java_shell_tcp

credits="""

+-----------------------+
|Created BY     GeerxOS |
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
banner="""

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

def bannerpp():
    print(" ")
    print(" ")
    print(Fore.BLUE + (banner))
    print(" ")
    print("=== !Payloads! ===")
    print(" ")
    print(Fore.RED + "[1] Python")
    print(Fore.RED + "[2] Perl")
    print(Fore.RED + "[3] ASP")
    print(Fore.RED + "[4] Bash")
    print(Fore.RED + "[5] WAR")
    print(Fore.RED + "[6] JSP")
    print(Fore.RED + "[7] Java")
    print(" ")
    print(Fore.WHITE + "[0] Back")
    print(" ")

#Cosas extras para el tool

os.system("clear")
bannerpp()

def main():

    msf = input(Fore.GREEN + "MsfShell/Extras:~# ")

    if msf == "credits":
        os.system("clear")
        print(credits)
        main()
        input("--> ")
        bannerpp()
        main()

    if msf == "0":
        exit()

    if msf == "1":
        os.system("clear")
        print(banner)
        print(" ")
        print("[1] cmd/unix/reverse_python")
        print(" ")
        print("[00] Back")
        print(" ")
        py = input("MsfShell/Extras/Python:~# ")

        if py == "1":
            py_shell()
            os.system("clear")
            bannerpp()
            main()

        if py == "00":
            os.system("clear")
            bannerpp()
            main()

        else:
            os.system("clear")
            bannerpp()
            main()

    if msf == "2":
        os.system("clear")
        print(banner)
        print(" ")
        print("[1] cmd/unix/reverse_perl")
        print(" ")
        print("[00] Back")
        print(" ")

        pl = input("MsfShell/Extras/Perl:~# ")

        if pl == "1":
            perl()
            os.system("clear")
            bannerpp()
            main()

        if pl == "00":
            os.system("clear")
            bannerpp()
            main()

        else:
            os.system("clear")
            bannerpp()
            main()

    if msf == "3":
        os.system("clear")
        print(banner)
        print(" ")
        print("   ASP  ")
        print("[1] windows/meterpreter/reverse_tcp ")
        print(" ")
        print("[00] Back")
        print(" ")

        asp = input("MsfShell/Extras/ASP:~# ")

        if asp == "1":
            asptcp()
            os.system("clear")
            bannerpp()
            main()

        if asp == "00":
            os.system("clear")
            bannerpp()
            main()

        else:
            os.system("clear")
            bannerpp()
            main()

    if msf == "4":
        os.system("clear")
        print(banner)
        print(" ")
        print("[1] cmd/unix/reverse_bash")
        print(" ")
        print("[00] Back")
        print(" ")

        bs = input("MsfShel/Extras/Bash:~# ")

        if bs == "1":
            bash()
            os.system("clear")
            bannerpp()
            main()

        if bs == "00":
            os.system("clear")
            bannerpp()
            main()
        
        else:
            os.system("clear")
            bannerpp()
            main()

    if msf == "5":
        os.system("clear")
        print(banner)
        print(" ")
        print("[1] java/jsp_shell_reverse_tcp")
        print(" ")
        print("[00] Back")
        print(" ")

        wr = input("MsfShell/Extras/Bash:~# ")

        if bs == "1":
            war()
            os.system("clear")
            bannerpp()
            main()

        if bs == "00":
            os.system("clear")
            bannerpp()
            main()
        
        else:
            os.system("clear")
            bannerpp()
            main()

    if msf == "6":
        os.system("clear")
        print(banner)
        print(" ")
        print("[1] java/jsp_shell_reverse_tcp")
        print(" ")
        print("[00] Back")
        print(" ")

        js = input("MsfShell/Extras/Jsp:~# ")

        if js == "1":
            jsp()
            os.system("clear")
            bannerpp()
            main()

        if js == "00":
            os.system("clear")
            bannerpp()
            main()

        else:
            os.system("clear")
            bannerpp()
            main()

    if msf == "7":
        os.system("clear")
        print(banner)
        print(" ")
        print("[1] java/meterpreter/reverse_tcp")
        print(" ")
        print("[2] java/meterpreter/reverse_http")
        print(" ")
        print("[3] java/shell/reverse_http")
        print(" ")
        print("[4] java/shell/reverse_tcp")
        print(" ")
        print("[00] Back")
        print(" ")

        jv = input("MsfShell/Extras/Java:~# ")

        if jv == "1":
            java_tcp()
            os.system("clear")
            bannerpp()
            main()

        if jv == "2":
            java_http()
            os.system("clear")
            bannerpp()
            main()

        if jv == "3":
            java_shell_http()
            os.system("clear")
            bannerpp()
            main()

        if jv == "4":
            java_shell_tcp()
            os.system("clear")
            bannerpp()
            main()

        if jv == "00":
            os.system("clear")
            bannerpp()
            main()

        else:
            os.system("clear")
            bannerpp()
            main()

    else:
        os.system("clear")
        bannerpp()
        main()
try:
    if __name__ == '__main__' :
        os.system("clear")
        bannerpp()
        main()    

except(KeyboardInterrupt):
    print(Fore.RED + "CTRL+C Exit!")
    exit()
