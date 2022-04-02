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

def search_email():
    os.system("clear")
    print(banner)
    print("Using: auxiliary/gather/search_email_collector")
    domain = input("Give me the domain: ")
    output = input("Output file: ")
    print("Ok!")
    print("+--------------------------------------------+ ")
    print("+-> Auxiliary data")
    print("+-> Auxiliary: auxiliary/gather/search_email_collector")
    print("+-> Domain: "+domain+" ")
    print("+-> Output: "+output+" ")
    print("+--------------------------------------------+ ")
    os.system("echo 'use auxiliary/gather/search_email_collector' >> emails.rb")
    os.system("echo 'set DOMAIN "+domain+"' >> emails.rb")
    os.system("echo 'set OUTFILE "+output+"' >> emails.rb")
    os.system("echo 'exploit' >> emails.rb")
    print("Running metasploit-framework...")
    os.system("gnome-terminal -- msfconsole -r emails.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")