#Diego Aspinwall
#9-15-17
#coloredSquare.py

from random import randint
from ggame import *

numcolor = randint(1,4)

if numcolor==1:
    red = Color(0xff0000, 1)
    line = LineStyle(3,red)
    rectangle = RectangleAsset(100,100,line,red)
elif numcolor==2:
    blue = Color(0x0000ff, 1)
    line = LineStyle(3,blue)
    rectangle = RectangleAsset(100,100,line,blue)
elif numcolor==3:
    yellow = Color(0xffff00, 1)
    line = LineStyle(3,yellow)
    rectangle = RectangleAsset(100,100,line,yellow)
elif numcolor==4:
    green = Color(0x00ff00, 1)
    line = LineStyle(3,green)
    rectangle = RectangleAsset(100,100,line,green)
Sprite(rectangle)
myApp = App()
myApp.run()