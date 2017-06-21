#! /usr/bin/env python

def fib(n):
    if n == 1 or n == 2:
        return 1;
    else:
        return fib(n-1) + fib(n-2)


def main():
    print("fib(5) = " + str(fib(5)))
    print("fib(10) = " + str(fib(10)))
    print("fib(50) = " + str(fib(50)))

if __name__ == "__main__":
    main()