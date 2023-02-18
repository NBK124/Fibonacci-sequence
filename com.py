count, n = 0, int(input('Введите количество чисел: '))


def fib(an, ol, n):
	global count 
	count += 1
	ne = an + ol
	tne = ne
	ol, an = ne, ol
	print(tne, end=' ')
	if count <= n: fib(an, ol, n)


print(1, 1, end=' ')
fib(1, 1, n)
#1, 1 – предыдущие числа 
#n — сколько раз
print()