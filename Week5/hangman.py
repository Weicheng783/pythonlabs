word = 'yellow'
count = 0
win = False
guesses = ''
answer = '______'
while (count < 10 and win == False):
  count = count + 1
  guess = input("Enter guess " + str(count)+": ")
  guesses = guesses + guess
  tmp = ''
  i = 0
  while i < len(word):
    if (word[i] == guess):
       tmp = tmp + guess
    else:
       tmp = tmp + answer[i]
#end if
    i = i + 1
   #end while
  if (answer != tmp):
    print('good guess')
    count = count - 1
    answer = tmp
  else:
    print('not a good guess')
#end if
  if (answer == word):
     print('Well done you win!')
     win = True
    # end if
  print(str(10 - count) + '/10 guesses left.')
  print('your guesses: ' + guesses)
#end while

