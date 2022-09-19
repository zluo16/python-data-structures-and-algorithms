def fibonacci_recursive(idx):
    if idx < 2:
        return idx

    return fibonacci_recursive(idx - 2) + fibonacci_recursive(idx - 1)


def fibonacci_dynamic():
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            cache[n] = fib(n - 1) + fib(n - 2)
            return cache[n]

    return fib


fibonacci = fibonacci_dynamic()

print(fibonacci(20))
print(fibonacci(43))
