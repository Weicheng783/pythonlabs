settings = open("settings.txt")

# print(settings.read(9))
# print(settings.readline())
# print(settings.readline())

# for x in settings:
#     print(x)
#
# settings.close()

# settings = open("settings.txt","a")
# settings.write('\nAdding more settings')
# settings.close()
#
# settings = open("settings.txt",'r')
# print(settings.read())

# WARNING: w means overwrite!
# settings = open("settings.txt","w")
# settings.write('\nAdding more settings')
# settings.close()

# newFile = open('myFile.txt','x')

import os
os.remove("myFile.txt")
