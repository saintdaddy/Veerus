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
	fille = open("../client.py", "r").read()
	chiffre = str(chiffrer("0xSxZ", fille))
	
	part2 = base64.b64encode(("""
def transcrireCle(cle):
	return "".join([str(ord(elt)) for elt in cle])
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
""").encode()).decode()


	fille = str("""
import base64
exec(base64.b64decode("aW1wb3J0IGhhc2hsaWIsIHN5cywgdGltZQ=="))
Made_By_0xSxZ = """ +'"'
+ part2 + '"'+"""\n\n"""+ """
def decryptMD5():
	print("Bahhahah you rly tought")
exec(base64.b64decode(Made_By_0xSxZ).decode())
""")
	open("../clientencoded.py", "x").write(fille.replace("b'", "").replace("'", ""))

print("[.] Created clientencoded.py .")