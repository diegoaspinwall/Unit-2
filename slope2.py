#Diego Aspinwall
#9-15-17
#slope2.py - improving slope.py

x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
if x1==x2:
    print('The slope is undefined')
    print('The equation of the line is X =', x1)
else:
    slope = (y2-y1)/(x2-x1)
    print('The slope is', slope)
    print('The equation of the line is Y =', slope, 'X +', (y2 - slope * x2))
