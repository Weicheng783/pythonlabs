# ---My Test Based Adventure Game--- #

playerName = input('What is your name? ')

print('Hello'+ playerName)

#print('1.Knight')
#print('2.Warrior')
#print('3.Wizard')

print('Choose a character:','1.Knight','2.Warrior','3.Wizard',sep='\n')

characterList=['Knight','Warrior','Wizard']

character=input('Type in your character number: ')

print('You chose:' + characterList[int(character)-1])

