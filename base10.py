#Diego Aspinwall
#9-18-17
#base10.py - base 10 number to hex

base10 = int(input('Enter a base 10 number (0-255): '))

dig1 = base10%16
dig2 = (base10//16)%16
