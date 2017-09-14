#Diego Aspinwall
#9-14-17
#unitConverter.py

print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')
print(' ')

num = int(input('Choose a number: '))

if num==4:
    cel = float(input('Enter Degrees in Celsius: '))
    print(cel, 'degrees Celsius is', cel*9/5 + 32, 'degrees in Fahrenheit')
elif num==3:
    lit = float(input('Enter Volume in Liters: '))
    print(lit, 'Liters is', lit*0.264172, 'Gallons')
elif num==2:
    mass = float(input('Enter Mass in Kilograms: '))
    print(mass, 'Kilograms is', mass*2.20462, 'Pounds')
elif num==1:
    kilo = float(input('Enter Distance in Kilometers: '))
    print(kilo, 'Kilometers is', kilo*0.621371, 'Miles')
