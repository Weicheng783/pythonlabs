num1 = input("Please enter a temperature in Celsius degrees: ")
print ("The temperature you entered display in Fahrenheit is " + str(float(num1)*float(1.8)+float(32)))

from math import pi

num2 = input("Then, please enter a number which is the radius of a circle or a sphere ")
print ("The area of the circle is " + str(float(num2)*float(num2)*pi))
print ("The circumference of the circle is " + str(float(2)*float(num2)*pi))
print ("The surface area of a sphere given this radius is " + str(float(4)*float(num2)*pi*float(num2)))

num3 = input("please enter a number which is the height of a cylinder ")
num4 = input("then, please enter a number which is the radius of a cylinder ")

print('The surface area of the cylinder is : '+ str((float(num4)*float(num4)*pi)*float(num3)))

name1=input('Can I ask for your first name ? ')
name2=input('Can I ask for your surname ? ')
print('Then your name is : '+name1+' '+name2+' .  Thanks.')


age1=input('Can I ask your age ? ')
print(int(age1)>int(17))




