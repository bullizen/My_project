def factorial(n):
    # Basfall: faktoriell av 0 eller 1 är 1
    if n == 0 or n == 1:
        return 1
    # Rekursivt fall: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Testa funktionen
print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)
