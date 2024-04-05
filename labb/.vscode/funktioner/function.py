# För att skapa en funktion skriver man "def" innan

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
# end skapar ett mellanslag på samma rad, utan end blir det ingen ny rad
fib (4)