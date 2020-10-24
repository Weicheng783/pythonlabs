# Decryption Program

ciphertext=input('To Decrypt What ?')
plainText=""
ciphertextPosition=0
while ciphertextPosition < len(ciphertext):
      ciphertextChar = ciphertext[ciphertextPosition]
      ASCIIValue = ord(ciphertextChar)
      ASCIIValue += 3
      plainText = plainText + chr(ASCIIValue)
      ciphertextPosition += 1

print(plainText)
