#Diego Aspinwall
#9-18-17
#base10.py - base 10 number to hex

base10a = int(input('Enter a base 10 number (0-255): '))

dig1 = base10a%16
dig2 = (base10a//16)%16

if dig1<10 and dig2<10:
    print(dig1, dig2)
if dig1==10 and dig2<10:
    print('A', dig2)
if dig1==11 and dig2<10:
    print('B', dig2)
if dig1==12 and dig2<10:
    print('C', dig2)
if dig1==13 and dig2<10:
    print('D', dig2)
if dig1==14 and dig2<10:
    print('E', dig2)
if dig1==15 and dig2<10:
    print('F', dig2)