def fib(n):
    a = 1
    b = 1

    print(a, b, end=' ')

    for i in range(2, n):
        c = a+b
        a = b
        b = c
        print(c, end=' ')
num = int(input('How many fibonacci numbers you want: '))
fib(num)
