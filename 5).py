a = 0
b = int(input('Введите количество строк:'))
while a < b:
    print('#', end=' ')
    c = 0
    while c != a:
        print(' ', end=' ')
        c = c+1
    print('#')
    a = a+1
