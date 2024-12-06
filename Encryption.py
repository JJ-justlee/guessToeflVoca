from encDecModule import SimpleEnDecrypt

simpleEnDecrypt = SimpleEnDecrypt(b'NcUgge50agCYGXpJmpcxsE5_0do84kKNdI6DsG-iwm8=')
access = "" #put a thing that has to be encrypted
print("Encryption: ", simpleEnDecrypt.encrypt(access))