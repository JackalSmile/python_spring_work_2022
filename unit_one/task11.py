# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

X = int(input("Введите год: "))
Y = int(X/100)+1
print ("Столетие:",Y)