a = int(input('Стартове количество организмов:'))
b = int(input('Среднесуточное увеличение популяции(в процентах):'))
c = int(input('Количество дней для размножения '))
d = 1
print('День Популяция')
print(1, ' ', a)
while d != c:
    d += 1
    a *= (1+b/100)
    print(d, ' ', a)
