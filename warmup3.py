#Diego Aspinwall
#9-15-17
#warmup3

num = int(input('Input an integer: '))

if num%3==0 and num%2==0:
    print(num, 'is divisible by 2 and 3')
elif num%3==0:
    print(num, 'is divisible by 3')
elif num%2==0:
    print(num, 'is divisible by 2')
else:
    print(num, 'is divisible by neither 3 or 2')
