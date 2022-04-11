# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A
# и вывести новые значения переменных A, B, C

A = int(input("Enter integer A "))
B = int(input("Enter integer B "))
C = int(input("Enter integer C "))
A, B, C = B, C, A
print(A, B, C)