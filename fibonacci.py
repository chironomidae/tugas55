def fibonacci(n):
    fib_sequence = [1, 1]

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

n = 10
fib_numbers = fibonacci(n)

output = ', '.join(map(str, fib_numbers))
print(output)
