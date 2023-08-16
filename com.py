def fibonacci_sequence(n, a=0, b=1):
    if n == 0:
        return []
    elif n == 1:
        return [a]
    else:
        return [a] + fibonacci_sequence(n-1, b, a+b)

n = int(input("Введите натуральное число n: "))
sequence = fibonacci_sequence(n)
print(*sequence)
