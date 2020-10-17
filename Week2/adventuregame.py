# ---My Test Based Adventure Game--- #

playerName = input('What is your name? ')

print('\n\nHello'+ playerName)

#print('1.Knight')
#print('2.Warrior')
#print('3.Wizard')
characterList=['Knight','Warrior','Wizard']
# since the character list could grow with new characters,
# better not to use a literal string of characters in the output.
print('\nChoose a character:',*characterList,sep='\n')



character=input('Type in your character number: ')

print('You chose:' + characterList[int(character)-1])

