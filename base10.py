#Diego Aspinwall
#9-18-17
#base10.py - base 10 number to hex

base10a = int(input('Enter a base 10 number (0-255): '))
base10b = int(input('Enter a base 10 number (0-255): '))
base10c = int(input('Enter a base 10 number (0-255): '))

dig1a = base10a%16
dig2a = (base10a//16)%16
dig1b = base10b%16
dig2b = (base10b//16)%16
dig1c = base10c%16
dig2c = (base10c//16)%16

