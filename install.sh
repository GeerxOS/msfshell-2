echo "You must run with root!"
git clone https://github.com/GeerxOS/msfshell-2
sudo apt install python3 
sudo apt install gnome-terminal
cd msfshell-2
mkdir /usr/share/msfshell-2
mv * /usr/share/msfshell-2
cd /usr/bin
echo '#!/bin/bash' >> msfshell-2
echo ' ' >> msfshell-2
echo 'exec python3 /usr/share/msfshell-2/msfshell-2.py' >> msfshell-2
echo 'Installed!'
echo "Open terminal"
echo "Use msfshell-2"
chmod 777 msfshell-2

