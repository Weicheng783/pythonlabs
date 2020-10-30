# ---My Test Based Adventure Game---
import time, os

print('Loading. . . .')
time.sleep(2)

playerSettings = list()
with open('settings.txt') as file:
     playerSettings = file.readlines()

playerSettings = [line.rstrip('\n') for line in open('settings.txt')]
#Welcome to my game Gareth

print('Welcome to my game '+playerSettings[0]+'\nPlease choose a character: ')


#playerName = input('What is your name? ')
#print('\n\nHello'+ playerName)

#print('1.Knight')
#print('2.Warrior')
#print('3.Wizard')
characterList=['Knight','Warrior','Wizard']

# Added a while loop to print out characterList

#i=0
#while i < len(characterList):
#    print(str(i+1)+'.'+characterList[i])
#    i += 1

for idx,val in enumerate(characterList,start=1):
    print(' '+str(idx)+'. '+val)

# since the character list could grow with new characters,
# better not to use a literal string of characters in the output.
#print('\nChoose a character:',*characterList,sep='\n')

#character=input('Type in your character number: ')
#selectedCharacter=characterList[int(character)-1]

character=int(input('Type in your character number: '))
playerSettings[1]=characterList[character-1]

#selectedCharacter=characterList[character-1]

print('You chose:' + playerSettings[1])

#settingsMenu=['Player Name','Character Name','Character Age','View Current Settings']

while True:
     menu=int(input('Would you like to start the adventure (1), change the settings (2), view settings (3), or save game (4) ? '))
     if(menu==1):
         move=input(playerSettings[1]+', do you want to move? ')
         count=0
         while move in{'Yes','yes','YES','y','Y'}:
               print('You moved forwards 1 space! ')
               move=input('Keep moving? ')
               count += 1
         else:
              print('You moved '+str(count)+' spaces, Congrats!')
              playerSettings[3] = int(playerSettings[3]) + count
              with open ('settings.txt','w') as file:
                   for item in playerSettings:
                       file.write('%s\n' % item)
              break

     elif (menu == 2):
          settingChange = int(input('What do you want to change? '))
          newValue = input('What is the new setting?')
          playerSettings[settingChange - 1] = newValue

     elif (menu == 3):
          print('Name: %s \nCharacter Name: %s \nCharacter Age: %s \n' % (playerSettings[0],playerSettings[1],playerSettings[2]))


     elif (menu == 4):
           with open ('settings.txt','w') as file:
                for item in playerSettings:
                    file.write('%s\n' % item)
           time.sleep(2)
           print('Game Saved !\n')
 
     else:
          print('Not a valid input: Try again! ')


