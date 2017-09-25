#Diego Aspinwall
#9-18-17
#base10.py - base 10 number to hex

base10a = int(input('Enter a base 10 number (0-255): '))

dig1 = base10a%16
dig2 = (base10a//16)%16

if dig1==10:
    dig1a = 'A'
elif dig1==11:
    dig1a = 'B'
elif dig1==12:
    dig1a = 'C'
elif dig1==13:
    dig1a = 'D'
elif dig1==14:
    dig1a = 'E'
elif dig1==15:
    dig1a = 'F'
else:
    dig1a = dig1
    
if dig2==10:
    dig2a = 'A'
elif dig2==11:
    dig2a = 'B'
elif dig2==12:
    dig2a = 'C'
elif dig2==13:
    dig2a = 'D'
elif dig2==14:
    dig2a = 'E'
elif dig2==15:
    dig2a = 'F'
else:
    dig2a = dig2
    
print(dig2a, dig1a)