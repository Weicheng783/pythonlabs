
print('EXAMPLE 1')

import time, os

time.sleep(2)
print(os.getlogin())

print('EXAMPLE 2')

myList = list(range(1,11,2))
print(myList)

# {1,3,5,7,9}

print('EXAMPLE 3')
i=0
while i < 4:
    print('while' + str(i))
    i += 1

print('EXAMPLE 4')
for x in range(4):
    print('For: '+str(x))

print('EXAMPLE 5')
for x in range(1,11):
     print('For sequence: ' + str(x))
#
print('EXAMPLE 6')
for x in range(1,11,2):
     print('For sequence: ' + str(x))

print('EXAMPLE 7')
fruits = ['apple','banana','pear']

for x in fruits:
    print(x)

print('EXAMPLE 8')
for x in 'banana':
    print(x)

print('EXAMPLE 9')
adj = ['warm','fancy','big']
clothes = ['hat','gloves','shoes']

for x in adj:
    for y in clothes:
        print(x,y)

