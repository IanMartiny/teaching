#! /usr/bin/env python

from math import sqrt

t1 = (1 + sqrt(5))/2
b  = 1/sqrt(5)
t2 = (1 - sqrt(5))/2
d  = 1/sqrt(5)

def fib(n):
    return int(b*(t1**n) - d*(t2**n))


def main():
    print("fib(5) = " + str(fib(5)))
    print("fib(10) = " + str(fib(10)))
    print("fib(40) = " + str(fib(40)))
    print("fib(100) = " + str(fib(100)))

if __name__ == "__main__":
    main()