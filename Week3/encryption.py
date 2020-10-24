# Encryption Program

#1: plaintext ← read(‘Plaintext:’)
plaintext=input('To Encrypt What ?')
#2: cipherText ← “ ”
cipherText=""
#3: alphabet ← “XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC”
alphabet="XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
#4: plaintextPosition ← 0
plaintextPosition=0
#5: while (plaintextPosition < length(plaintext)) do
while plaintextPosition < len(plaintext):
#6: plaintextChar ← plaintext[plaintextPosition]
      plaintextChar = plaintext[plaintextPosition]
#7: alphabetPosition ← 3
      alphabetPosition = 3
#8: while plaintextChar = alphabet[alphabetPosition] do
      while plaintextChar != alphabet[alphabetPosition]:
            alphabetPosition += 1
#9: alphabetPosition ← alphabetPosition + 1
#10: end while
      alphabetPosition -= 3
#11: alphabetPosition ← alphabetPosition - 3
#12: cipherText ← cipherText + alphabet[alphabetPosition]
      cipherText = cipherText + alphabet[alphabetPosition]
#13: plaintextPosition ← plaintextPosition + 1
      plaintextPosition += 1

#14: end while

#15: display(cipherText)
print(cipherText)

#To Encrypt What ?LOVEPYTHON
#ILSBMVQELK
#To Encrypt What ?LOVEUOM
#ILSBRLJ
#To Encrypt What ?FULLOFLOVE
#CRIILCILSB




