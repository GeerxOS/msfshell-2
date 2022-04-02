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

def search_sdomains():
    os.system("clear")
    print("Using: auxiliary/gather/searchengine_subdomains_collector")
    domain = input("Give me the domain: ")
    print("Ok!")
    print("+------------------------------------------------------------------+ ")
    print("+-> Auxiliary data")
    print("+-> Auxiliary: auxiliary/gather/searchengine_subdomains_collector")
    print("+-> Target: "+domain+"")
    print("+------------------------------------------------------------------+ ")
    os.system("echo 'use auxiliary/gather/searchengine_subdomains_collector' >> sdomains.rb")
    os.system("echo 'set TARGET "+domain+"' >> sdomains.rb")
    os.system("echo 'exploit' >> sdomains.rb")
    print("Running metasploit-framework...")
    os.system("gnome-terminal -- msfconsole -r sdomains.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")