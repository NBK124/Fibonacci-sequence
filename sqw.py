count = 0
n1, n2 = 0, 1
n = int(input('Enter count numbers: '))
while not n == n:
    sq = n1 + n2
    n1 = n2
    n2 = sq
    print(n1)
    count += 1
