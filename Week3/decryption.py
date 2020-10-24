# Encryption Program

#1: plaintext ← read(‘Plaintext:’) EBIIL
plaintext=input('To Decrypt What ?')
#2: cipherText ← “ ”
cipherText=""
#3: alphabet ← “XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC”
alphabet="XYZABCDEFGHIJKLMNOPQRSTUVW"
#alphabet='CBAZYXWVUTSRQPONMLKJIHGFEDCBAZYX'
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
            if alphabetPosition == 0:
               alphabetPosition = 25
            else: alphabetPosition -= 1
#9: alphabetPosition ← alphabetPosition + 1
#10: end while
      if alphabetPosition >= 23:
         shift=25-alphabetPosition
         if shift == 0:
            alphabetPosition = 2
         elif shift == 1:
            alphabetPosition = 1
         else:
            alphabetPosition = 0

      else: alphabetPosition += 3
#11: alphabetPosition ← alphabetPosition - 3
#12: cipherText ← cipherText + alphabet[alphabetPosition]
      cipherText = cipherText + alphabet[alphabetPosition]
#13: plaintextPosition ← plaintextPosition + 1
      plaintextPosition += 1
     
#14: end while

#15: display(cipherText)
print(cipherText)






