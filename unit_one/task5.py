# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму
# Примечание: все точки получаем через функцию input()
# При решении задачи обратите внимание какой тип вы получаете через функцию input()
A=float(input("enter А:"))
B=float(input("enter B:"))
C=float(input("enter C:"))
print("AC = " + str(C - A))
print("BC = " + str(C - B))
print("AC + BC = " + str((C - A) + (C - B)))