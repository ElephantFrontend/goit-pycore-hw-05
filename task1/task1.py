def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n == 1:
            result = n
        if n <=0:
            result = 0
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))