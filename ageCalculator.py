#Diego Aspinwall
#9-15-17
#ageCalculator.py

from datetime import date

year = int(input('Enter the year you were born: '))
month = int(input('Enter the month you were born (1-12): '))
day = int(input('Enter the day you were born: '))

yearNow = date.today().year
monthNow = date.today().month
dayNow = date.today().day

if monthNow==month and dayNow==day:
    print ('Happy Birthday, you', yearNow-year, 'year old!')
elif monthNow==month and dayNow<day:
    print('You are', (yearNow-year)-1, 'years old')
elif month:
    print('You are', (yearNow-year), 'years old')
elif monthNow<month:
    print('You are', (yearNow-year)-1, 'years old')
