#Diego Aspinwall
#9-15-17
#quadratic.py

print('ax^2 + bx + c = 0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
print('x =', (-b+(b**2-4*a*c)**(1/2))/2*a, 'or')
print('x =', (-b-(b**2-4*a*c)**(1/2))/2*a)

if (b**2-4*a*c)<0:
    print('No real solutions, imaginary solutions above.')

"""
mr.Smedinghoff's answer looked different, but when I tested this it worked. Maybe has something to
do with i?
"""
