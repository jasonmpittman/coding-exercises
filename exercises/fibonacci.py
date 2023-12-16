#!/usr/bin/env python3

""" Fibonacci: takes input n and computes the n-th Fibonacci number """

from sys import argv

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    n = int(argv[1])
    print(fibonacci(n))