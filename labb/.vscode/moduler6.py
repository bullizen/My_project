# Fibonacci numbers module


def fib(n: int):  # write Fibonacci series up to n
    """Prints the fib sequence up until n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fib2(n: int):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
