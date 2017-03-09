# Разложение на множители

def perfectSquare(x):
    return (int(x**0.5))**2 == x

def factorizeFerma(n):
    x = int(n ** 0.5) + 1
    while not perfectSquare(x * x - n):
        x += 1
    y = int((x * x - n) ** 0.5)
    a = x - y
    b = x + y
    return a, b

while True:
    n = int(input('Введите число: '))
    a, b = factorizeFerma(n)
    print('{} = {} * {}\n'.format(n, a, b))
