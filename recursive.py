"""
A series of problems that can be programmed recursively
"""

"""
1. Factorial of N
fac(n) = N! = N * (N-1) * ... * 1
"""
def fac(n):
    return 1 if n == 1 else fac(n - 1) * n

print(fac(5))


"""
2. Fibonacci sequence
Note: fib(n) only returns the nth Fibonacci number. If we need the whole sequence, we should be careful of collecting
each number to avoid high complexity
"""
def fib(n):
    return 1 if n == 1 or n == 2 else fib(n - 1) + fib(n - 2)

print(fib(6))


"""
Hanoi tower
"""
def hanoi():
    pass