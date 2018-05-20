import math
print("Введите коэффиценты a,b и c")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
dis = b ** 2 - 4 * a * c
print (a,"*x^2+",b,"+",c)
d=b*b-4*a*c
if (d < 0):
    print("нет решений")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1=",x1)
    print("x2=",x2)
print("конец")