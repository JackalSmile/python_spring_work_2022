#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.


mass = [1,2,17,16,30,51,2,70,3,2]

for i in mass:
    if mass.count(i) > 1:
        x = i
y = []
z = []

if x in mass:
    counter = 0
    start = 0
    if mass.count(x) == 1:
        print("В списке одно значение, под индексом :", x)
    else:
        while counter < mass.count(x):
            start = mass.index(x, start, len(mass)) +1
            counter += 1
            y.append(start - 1)

for x in range(0, len(y)-1):
    z.append(y[x + 1] - y[x])

for x in range(0, len(y) - 1):
    if y[x + 1] - y[x] == min(z):
        print("Для числа", i, "индексы двух ближайших чисел:", y[x], "и", y[i])