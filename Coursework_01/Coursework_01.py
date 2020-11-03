import time, os, datetime, timeit
from difflib import SequenceMatcher
# score1 = SequenceMatcher(None, "apple", "appl44").ratio()
# score2 = SequenceMatcher(None, "apple", "mapplngo").ratio()
# print(score1)
# print(score2)

# EnglishWords = open("EnglishWords.txt")
count=len(open(r"EnglishWords.txt",'r').readlines())
# print(count)
wordnum=0
currentline=0

wordtrue=0
wordfalse=0
totalwords=0
wordsindic=0
wordschanged=0


while True:
 mainmanu=['1. Spell check a sentence','2. Spell check a file','0. Quit the program']
 print(os.getlogin()+', Welcome to Weichengs Spell Checker !'+'\nPlease choose a mode from the following to proceed:'+
'\n(Please enter a NUMBER for corresponding choice)')



 for idx, val in enumerate(mainmanu,start=1):
    print(' '+val)

 mainChoice=input('Type in your choice number: ')

 if mainChoice=='1':
   sentence=input('Enter your sentence to check : ')
   # print (sentence.split( ))
   start=timeit.default_timer()

   sentence=sentence.strip('')
   sentence=sentence.strip("!,.:;?~#!^*&'1234567890")
   sentence=sentence.lower()
   sentence=sentence.replace("'",'')
   sentence=sentence.replace(",",'')
   sentence=sentence.replace(";",'')
   sentence=sentence.replace(":",'')
   sentence=sentence.replace("!",'')
   sentence=sentence.replace("#",'')
   sentence=sentence.replace('.','')
   sentence=sentence.replace('0','')
   sentence=sentence.replace('1','')
   sentence=sentence.replace('2','')
   sentence=sentence.replace('3','')
   sentence=sentence.replace('4','')
   sentence=sentence.replace('5','')
   sentence=sentence.replace('6','')
   sentence=sentence.replace('7','')
   sentence=sentence.replace('8','')
   sentence=sentence.replace('9','')
   sentence=sentence.replace('*','')
   print(sentence)
   split=sentence.split()
   marka=''
   result=''

   totalwords=len(split)-1
   file=[line.rstrip('\n')for line in open('EnglishWords.txt')]
   # print(file[0])
   while wordnum <= len(split)-1:
       while currentline <= count:
           if split[wordnum] == file[currentline]:
              # print(split[wordnum]+' :spelt correctly!')
              wordtrue += 1
              result=result+' '+split[wordnum]
              currentline=0
              break
           elif split[wordnum] != file[currentline]:
              if currentline == count-1:

                  while True:
                      print('Ooops! '+split[wordnum]+' did not find in the dictionary, please enter your choice below.')
                      incorrectmanu=['1. ignore','2. mark','3. add to dictionary','4. suggest likely correct spelling']
                      for idx, val in enumerate(incorrectmanu,start=1):
                          print(' '+val)
                      incorrectchoice=input('Type in your choice number: ')
                      if incorrectchoice == '1':
                          wordfalse += 1
                          result=result+' '+split[wordnum]
                          print(split[wordnum]+" is ignored, counted as incorrectly spelt.")
                          break
                      elif incorrectchoice == '2':
                          wordfalse += 1
                          marka=marka+' ?'+split[wordnum]+'?'
                          result=result+' ?'+split[wordnum]+'?'
                          print(split[wordnum]+' is marked as ?'+split[wordnum]+'? .Counted as incorrectly spelt.')
                          break
                      elif incorrectchoice == '3':
                          wordsindic += 1

                          result=result+' '+split[wordnum]
                          print(split[wordnum]+" is added to the dictionary, counted as correctly spelt.")
                          break
                      elif incorrectchoice == '4':

                          print(split[wordnum]+" has the following suggestion, enter 1 to accept,or 2 to reject the word suggested.")
                          currentline=0
                          currentscore=0
                          word=''
                          while currentline <= count-1:
                              score = SequenceMatcher(None, split[wordnum], file[currentline]).ratio()
                              if currentscore <= score:
                                 word = file[currentline]
                                 currentscore = score
                              if currentline == count:
                                 currentline = 0
                                 break
                              else:
                                 currentline += 1
                          print('< '+word+' >'+'  (Match Rate:'+str(currentscore)+')')
                          while True:
                              changechoice=input('Please type in your choice: ')
                              if changechoice == '1':
                                  wordtrue += 1
                                  wordschanged += 1
                                  result=result+' '+word
                                  print(word+" is changed and added to the dictionary, counted as correctly spelt.")
                                  break
                              if changechoice == '2':
                                  wordfalse += 1
                                  marka=marka+' ?'+split[wordnum]+'?'
                                  result=result+' ?'+split[wordnum]+'?'
                                  print(word+" is rejected, "+split[wordnum]+" counted as incorrectly spelt.")
                                  break
                              else:
                                  print('Your entered an invalid choice, please try again.')
                          break
                      else:
                          print('Your entered an invalid choice, please try again.')
                  currentline=0
                  break
              else:
                  currentline += 1
              # print(currentline)

       # print(wordnum)
       wordnum += 1
   end = timeit.default_timer()

   print('Sentence Checking Complete!')
   print('  < Statistics Summary >')
   print('  the total number of words : '+str(totalwords+1)+' words')
   print('  the number of words spelt correctly : '+str(wordtrue)+' words')
   print('  the number of incorrectly spelt words : '+str(wordfalse)+' words')
   print('  the number of words added to the dictionary : '+str(wordsindic)+' words')
   print('  the number of words changed by the user accepting the suggested word : '+str(wordschanged)+' words')
   curr_time=datetime.datetime.now()
   time_str=curr_time.strftime('%Y-%m-%d %H:%M:%S')
   print('  the time and date the input was spellchecked : '+ time_str)
   print('  The amount of time elapsed to spellcheck the input : '+'%s Seconds'%(end-start))

   wordnum=0
   newfilename=input('Please enter a filename that stores the result: ')
   newfile=open(newfilename+'.txt','w')

   newfile.write('< Statistics Summary >\n'+'the total number of words : '+str(totalwords+1)+' words\n'+'the number of words spelt correctly : '+str(wordtrue)+' words\n'+'the number of incorrectly spelt words : '+str(wordfalse)+' words\n'+'the number of words added to the dictionary : '+str(wordsindic)+' words\n'+'the number of words changed by the user accepting the suggested word : '+str(wordschanged)+' words\n'+'the time and date the input was spellchecked : '+ time_str+'\n'+'The amount of time elapsed to spellcheck the input : '+'%s Seconds'%(end-start)+'\n'+'Original input: '+sentence+'\n'+'incorrectly spelt words: '+ marka +'\n'+'result: '+ result +'\n')
   newfile.close()
   marka=''
   result=''
   print('File Created and Saved successful!!! Return to the main in 3 secs.')
   time.sleep(3)
   # print(file.readline[3])
   # for idx, val in enumerate(split,start=1):

    # print(' '+val)
     # while True:

      # for line in file:

      #     currentline=0
      #     totalline=count
      #      # print(line+val, end=" ")
      #     if split[wordnum] == line:
      #         print(split[wordnum]+' :spelt correctly!')
      #         break
      #     elif wordnum == count+1:
      #

           # if val==line:

    # if split==line:
    #     print('spelt duila!'+val)
    # else:
    #     pass   # else:
           #     break
    #    if split[0]==line:
    #       print('This word '+val+' spelt correctly!')
    #
    #
    # # if input('Enter PIN: ')=='1':
    # #    print('')
    #
    #    else:
    #       break
 elif mainChoice=='2':

     while True:
      filename=input('Enter your filename to check (enter 0 back to the main manu): ')
      if os.path.isfile(filename+'.txt'):
          print (filename.split( ))
          break
      elif filename=='0':
          print('Exit to the main manu.')
          break
      else:
        print('\nOoops! The file '+filename+' does not exist! Please try again.')



 elif mainChoice=='0':
    exit()
    # kill()
 else:
    print('\nOoops! You entered '+mainChoice+', which is an invalid choice! Please enter again.')
    # print('Please choose a mode from the following to proceed:'+
    # '\n(Please enter a NUMBER for corresponding choice)')
    # for idx,val in enumerate(mainmanu,start=1):
    #     print(' '+val)

# print('2nd functions!Congrats!')
