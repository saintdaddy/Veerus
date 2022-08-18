import uuid
import base64
import hashlib

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

key = input("Type something : ")
webhook = input("Webhook : ")
print(f"Salt : {key}\n\nWebhook : {str(Getchiffrer(key, webhook))}\n\nMagic Number : {str(chiffrer(key, webhook))}")
