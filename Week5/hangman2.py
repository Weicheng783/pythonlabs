import random


file = open("englishWords.txt", "r")
for line in file: 
  line = line.rstrip()
  theWords = []
#  theWords = ["red", "magenta", "green", "blue", "pink", "brown"]
  theWords.append(line)
word = random.choice(theWords)
count = 0
win = False
guesses = ''
answer = ''
#numberOfChars = len(word)
#for i in range(numberOfChars): answer += "_"
for i in range(len(word)): answer += "_"
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

