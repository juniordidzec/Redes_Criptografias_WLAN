import os

from Crypto.Cipher import AES
from Crypto import Random

from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

import time


dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+r"\plainText.txt", "r") as arquivo:
	plainText = arquivo.read()
	# print(os.path.getsize(dir_path+r"\plainText.txt") )
# print(plainText[:32])

keyBits = 32
print(f'Tamanho da chave: {keyBits*8}')

iv = Random.new().read(16)
key = Random.new().read(keyBits)
plainText = str.encode(plainText)
# ------------------------------------------------------ AES
start1_AES = time.time() 
cipher_AES = AES.new(key, AES.MODE_CFB, iv)
msg_AES = cipher_AES.encrypt(plainText)
end1_AES = time.time() 
print(msg_AES[:16])
print(f'Tempo de criptografar com AES: {end1_AES - start1_AES:.6f} ')

start2_AES = time.time() 
decipher_AES = AES.new(key, AES.MODE_CFB, iv)
decryptMsg_AES = decipher_AES.decrypt(msg_AES)
end2_AES = time.time()
print(decryptMsg_AES[:16])
print(f'Tempo de decriptografar com AES: {end2_AES - start2_AES:.6f} ')


# ------------------------------------------------------ RC4
start1_RC4 = time.time() 
tempkey = SHA.new(key+iv).digest()
cipher_RC4 = ARC4.new(tempkey)
msg_RC4 = cipher_RC4.encrypt(plainText)
end1_RC4 = time.time() 
print(msg_RC4[:16])
print(f'Tempo de criptografar com RC4: {end1_RC4 - start1_RC4:.6f} ')

start2_RC4 = time.time() 
decipher_RC4 = ARC4.new(tempkey)
decryptMsg_RC4 = decipher_RC4.decrypt(msg_RC4)
end2_RC4 = time.time() 
print(decryptMsg_RC4[:16])
print(f'Tempo de decriptografar com RC4: {end2_RC4 - start2_RC4:.6f} ')