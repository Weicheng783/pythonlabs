def printState():
    print('Red Light on? '+str(redLight))
    print('Yellow Light on? '+str(yellowLight))
    print('Green Light on? '+str(greenLight))

redLight=True
yellowLight=False
greenLight=False

printState()

print (type(redLight))

x=10
y=20.0
z=1j

print(type(x))
print(type(y))
print(type(z))

x1=int(1)
y1=int(2.8)
z1=int('3')

print(type(x1))
print(type(y1))
print(type(z1))

day='Beautiful'
print(day[1])
print(day[0:5])

print(day[-3])    # f
print(day[-3:])   # ful
print(day[-5:3])  # /error/empty(N/A)
print(day[-5:-3]) # ti

day == "Beautiful"
print("Today is " + day)



