import random
ex=1
def sum(x, y):
    return list(map(lambda a, b: a + b, x, y))
def aminb(x, y):
    return list(map(lambda a, b: a - b, x, y))
def det(a):
    res = 1
    n = len(a)
    for i in range(n):
        # выбираем опорный элемент
        j = max(range(i,n), key=lambda k: abs(a[k][i]))
        if i != j:
            a[i],a[j] = a[j],a[i]
            res *= -1


        res *= a[i][i]
        # "обнуляем" элементы в текущем столбце
        for j in range(i+1,n):
            b = a[j][i] / a[i][i]
            a[j] = [a[j][k]-b*a[i][k] for k in range(n)]
    return res

while ex != 0:
	print("Складывать и вычитать можно матрицы имеющие одинаковую размерность")

	r1 =  int(input('Введите размерность матрицы A (целое число > 0) :'))
	r2 =  int(input('Введите размерность матрицы B (целое число > 0) :'))

	m1 = [[random.randint(-50, 100) for x in range(r1)] for x in range(r1)]
	m2 = [[random.randint(-50, 100) for x in range(r2)] for x in range(r2)]
	print("матрица A:")
	for x in m1:
		print(' '.join([str(elem) for elem in x]))
	print("матрица B:")
	for x in m2:
		print(' '.join([str(elem) for elem in x]))

	w = 0
	s = 0  # сумма
	t = []  # временная матрица
	m3 = []  # конечная матрица
	if len(m2) != len(m1[0]) or r1 != r2:
		w = 1

	else:
		for z in range(0, r1):
			for j in range(0, r2):
				for i in range(0, r1):
					s = s + m1[z][i] * m2[i][j]
				t.append(s)
				s = 0
			m3.append(t)
			t = []
	m4 = []
	m5 = []
	m7 = m2
	for x in m1:
		for y in m2:
			m4.append(sum(x, y))
			m5.append(aminb(x, y))
			m2 = m2[1:]
			break

	da = int(det(m1))
	db = int(det(m7))
	if r1 == r2 :
		print("матрица A + B :")
		for x in m4:
			print(' '.join([str(elem) for elem in x]))
		print("матрица A - B :")
		for x in m5:
			print(' '.join([str(elem) for elem in x]))
	else:
		print("Складывать и вычитать можно матрицы имеющие одинаковую размерность")
	if w ==1 :
  	 	print("Данные Матрицы не могут быть перемножены")
	else:
		print("матрица A * B:")
	for x in m3:
		print(' '.join([str(elem) for elem in x]))

	print("Оприделитель матрицы A:")
	print(da)
	print("Оприделитель матрицы B:")
	print(db)

	print("для ввода новых данных нажмите 1, для выхода 0")
	ex = int(input())