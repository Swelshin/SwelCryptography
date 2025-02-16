import tms

keys = tms.Tms(7, 9)
keys.keygen(1024)
texto_c=keys.encrypt("Hola Buenos Días")
print("Texto Cifrado → " + texto_c)
print("Texto Descifrado → " + keys.decrypt(texto_c))
