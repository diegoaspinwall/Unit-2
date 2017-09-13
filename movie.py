#Diego Aspinwall
#9-13-17
#movie.py

age = int(input('Enter your age: '))
if age<8:
    print('You can watch G movies')
elif 13>age>=8:
    print('You can watch PG movies')
elif 18>age>=13:
    print('You can watch PG-13 movies')
else:
    print('You can watch R movies')
