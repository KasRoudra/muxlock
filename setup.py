# -*- coding: UTF-8 -*-
import os, time
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"
ask = green + '[' + white + '?' + green + '] '+ yellow
success = green + '[' + white + '√' + green + '] '
error = red + '[' + white + '!' + red + '] '
info= yellow + '[' + white + '+' + yellow + '] '+ cyan
logo='''
'''+green+'''  __  __            _                _    
'''+red+''' |  \/  |          | |              | |   
'''+cyan+''' | \  / |_   ___  __ |     ___   ___| | __
'''+yellow+''' | |\/| | | | \ \/ / |    / _ \ / __| |/ /
'''+blue+''' | |  | | |_| |>  <| |____ (_) | (__|   < 
'''+purple+''' |_|  |_|\__,_/_/\_\______\___/ \___|_|\_\
'''+green+'''                                          
'''
def main():
    print(yellow+'''Choose one of the following options below!
    
>>>1. Lock and Welcome Name-Text

>>>2. Only Lock, no Welcome Name-Text

>>>3. Only Welcome Name-Text, no lock

>>>0. Exit the setup
''')

    while True:
        num= input(ask+" > ",)
        if num== "1":
            setlock()
            setwc()
            exit()
        elif num== "2":
            setlock()
            exit()
        elif num== "3":
            setwc()
            exit()
        elif num=="0":
            exit()
        else:
            print(error+"Wrong input")
            time.sleep(2)
            main()
def setlock():
    if os.system("command -v figlet > /dev/null 2>&1")!=0:
        print(info+"Installing figlet....")
        os.system("apt update && apt upgrade -y && apt install figlet -y")
    os.system("clear")
    print(logo)
    x=input("\n"+ask+"Enter your username > "+green)
    if x=="":
        print(error+"No name")
        time.sleep(2)
        setlock()
    y=input("\n"+ask+"Enter your password > "+green)
    if y=="":
        print(error+"No Password")
        time.sleep(2)
        setlock()
    data='''
figlet MuxLock
loop=true

while $loop; do
	echo -e "\e[1;;34mEnter the username:\e[0m"
	read usr
	echo -e "\e[1;;37mEnter the password:\e[0m"
	read pwd
	if [[ ($usr == "'''+x+'''" && $pwd == "'''+y+'''") ]]; then
	echo -e "\e[1;;46mLogin successful!\e[0m"
	sleep 1
	loop=false
	elif [[ ($usr == "forgotten" && $pwd == "forgotten") ]]; then
	bash ~/../usr/etc/forgotten.sh
	loop=false
	else
	echo -e "\e[1;;45mWrong username or password!\e[0m"
	fi
	done
clear
figlet '''+x
    m=input("\n"+ask+"Your favourite food/person name in case you forgotten password > "+green)
    if m=="":
        print(error+"No information")
        time.sleep(2)
        setlock()
    forgotdata='''
loop=true
while $loop; do
echo -e "Enter your favourite person/food name:"
read forg
if [ "$forg"="'''+m+'''" ]; then
echo -e "Removing lock!"
removelock
sleep 2
loop=false
else
echo -e "You can't reset password.\nClear your termux data!"
fi
done
'''            
    if os.path.isfile("/data/data/com.termux/files/usr/etc/zshrc"):
        os.system("cp -r zshrc ~/../usr/etc")
        with open("/data/data/com.termux/files/usr/etc/zshrc", "a") as file2:
            file2.write(data)
    if os.path.isfile("/data/data/com.termux/files/usr/etc/bash.bashrc"):
        os.system("cp -r bash.bashrc ~/../usr/etc")
        with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "a") as file2:
            file2.write(data)
    if not os.path.isfile("/data/data/com.termux/files/usr/etc/forgotten.sh"):        
        os.system("touch /data/data/com.termux/files/usr/etc/forgotten.sh")
    with open("/data/data/com.termux/files/usr/etc/forgotten.sh", "w") as forgotten:
        forgotten.write(forgotdata)
    os.system("cp -r ~/muxlock/removelock ~/../usr/bin")
    print("\n"+success+"Lock setup successful. Enter \"removelock\" to remove lock")
    time.sleep(2)
def setwc():
    if os.system("command -v mpv > /dev/null 2>&1")!=0:
        print(info+"Installing mpv....")
        os.system("apt update && apt upgrade -y && apt install mpv -y")
    os.system("clear")
    print(logo)
    b=input("\n"+ask+"Enter your name to be displayed on home > "+green)
    if b=="":
        print(error+"No name")
        time.sleep(2)
        setwc()
    c=input("\n"+ask+"Enter some welcome text > "+green)
    if c=="":
        print(error+"No welcome text")
        time.sleep(2)
        setwc()
    wcdata="\nmpv ~/../usr/etc/wc.mp3\nclear\nfiglet "+b+"\necho "+c
    if os.path.isfile("/data/data/com.termux/files/usr/etc/zshrc"):  
        with open("/data/data/com.termux/files/usr/etc/zshrc", "r") as file:
            data= file.read()
            if not data.find("MuxLock")!=-1:
                os.remove("/data/data/com.termux/files/usr/etc/zshrc")
                os.system("cp -r zshrc ~/../usr/etc")
            with open("/data/data/com.termux/files/usr/etc/zshrc", "a") as file2:    
                file2.write(wcdata)
    if os.path.isfile("/data/data/com.termux/files/usr/etc/bash.bashrc"):
        with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "r") as file:
            data= file.read()
            if not data.find("MuxLock")!=-1:
                os.remove("/data/data/com.termux/files/usr/etc/bash.bashrc")
                os.system("cp -r bash.bashrc ~/../usr/etc")
            with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "a") as file2:    
                file2.write(wcdata)
    os.system("cp -r wc.mp3 ~/../usr/etc")
    print("\n"+success+"Welcome setup successful!")
    
os.system("chmod 777 *")
os.system("cp -r motd ~/../usr")
os.system("cp -r bash.bashrc ~/../usr")
os.system("cp -r zshrc ~/../usr")
os.system("rm -rf ~/../usr/etc/motd")
os.system("clear")
print(logo)
main()