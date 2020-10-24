# ---My Test Based Adventure Game---
import time, os

print('Loading. . . .')
time.sleep(2)

playerSettings={
    'name':os.getlogin(),
    'characterName':'',
    'characterAge':528
}

print('Welcome to my game '+playerSettings.get('name')+'\nPlease choose a character: ')


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
playerSettings['characterName']=characterList[character-1]

#selectedCharacter=characterList[character-1]

print('You chose:' + playerSettings.get('characterName'))

settingsMenu=['Player Name','Character Name','Character Age','View Current Settings']

while True:
     menu=int(input('Would you like to start the adventure or change the settings? '))
     if(menu==1):
         move=input(playerSettings['characterName']+', do you want to move? ')
         count=0
         while move in{'Yes','yes','YES','y','Y'}:
               print('You moved forwards 1 space! ')
               move=input('Keep moving? ')
               count += 1
         else:
              print('You moved '+str(count)+' spaces, Congrats!')
              break

     elif (menu == 2):
          for idx,val in enumerate(settingsMenu,start=1):
              print(' '+str(idx)+'. '+val)

          settingChange=int(input('what do you want to change? '))

          if (settingChange == 1):
              playerSettings['name']=input('Please enter a new name: ')
              print('Thanks '+playerSettings['name']+', Enjoy the Game!')
          elif (settingChange == 2):
              print('')
          elif (settingChange == 3):
              print('')
          elif (settingChange == 4):
              print('Name: '+playerSettings['name']+'\nCharacter Name: '+playerSettings['characterName']+'\nCharacter Age: '+str(playerSettings['characterAge']))
      else:
          print('Not a valid input: Try again! ')


