# ---My Test Based Adventure Game---
import time, os

print('Loading. . . .')
time.sleep(2)

print('Welcome to my game'+os.getlogin()+'\nPlease choose a character: ')


#playerName = input('What is your name? ')
#print('\n\nHello'+ playerName)

#print('1.Knight')
#print('2.Warrior')
#print('3.Wizard')
characterList=['Knight','Warrior','Wizard']

# Added a while loop to print out characterList
i=0
while i < len(characterList):
    print(str(i+1)+'.'+characterList[i])
    i += 1


# since the character list could grow with new characters,
# better not to use a literal string of characters in the output.
#print('\nChoose a character:',*characterList,sep='\n')

#character=input('Type in your character number: ')
#selectedCharacter=characterList[int(character)-1]

character=int(input('Type in your character number: '))
selectedCharacter=characterList[character-1]



print('You chose:' + selectedCharacter)

