#Diego Aspinwall
#9-13-17
#gradeCalculator.py

grade = float(input('Input your grade: '))
if 100>grade>=90:
    print('You earned an A')
elif 90>grade>=80:
    print('You earned a B')
elif 80>grade>=70:
    print('You earned a C')
elif 70>grade>=60:
    print('You earned a D')
if grade<60:
    print('You earned an F')