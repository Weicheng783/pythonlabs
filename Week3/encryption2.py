# Encryption Program

plaintext=input('To Encrypt What ?')
cipherText=""
plaintextPosition=0
while plaintextPosition < len(plaintext):
      plaintextChar = plaintext[plaintextPosition]
      ASCIIValue = ord(plaintextChar)
      ASCIIValue -= 3
      cipherText = cipherText + chr(ASCIIValue)
      plaintextPosition += 1
print(cipherText)

#To Encrypt What ?LOVEPYTHON
#ILSBMVQELK
#To Encrypt What ?LOVEUOM
#ILSBRLJ
#To Encrypt What ?FULLOFLOVE
#CRIILCILSB
