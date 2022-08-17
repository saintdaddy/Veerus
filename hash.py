import requests
import uuid
from Crypto.Cipher import AES



ip = requests.get('https://api.ipify.org').content.decode('utf8')

salt = input("[.] Encoding KEY (default : 0xSxZ^@@@!dazd0xSxZ) : ")
if(salt == "" or salt == None):
	salt = "0xSxZ^@@@!dazd0xSxZ"
salt2ask = input("[.] Add 2nd layer to encryption? (y/n) : ")
if salt2ask == "y":
	salt2 = input("[.] 2nd Encryption KEY (ex : sk1d) : ")
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
