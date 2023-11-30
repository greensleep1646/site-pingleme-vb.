#!usr/bin/env python3

import os
import sys
import time

os.system("pkg install cowsay")
os.system("clear")
os.system("pkg install dnsutils -y")
os.system("pip install nslookup")
os.system("cowsay -f GREENSLEEP TOOL")
print("""
\033[92m
       Codded by/GREENSLEEP
   \033[94m☾★ Github:https://github.com/greensleep1646/
   \033[94m   
   \033[94m  instagram:xxqwxexx

\033[92m[1]\033[93mSite IP bulma

\033[92m[2]\033[93mSite Ping Atma

\033[92m[3]\033[93mÇıkış


""")
islemno=input("İşlem numarasını Seç: ")

if islemno=="1":
        islemno2=input("\033[94mHedef Site Gir ")
        os.system("nslookup" " "+islemno2)

if islemno=="2":
        islemno3=input("\033[94mHedef IP gir: ")
        os.system("ping -s 1000" " "+islemno3)
if islemno=="3":
        os.system("cowsay -s Güle Güle...") 
        quit()
