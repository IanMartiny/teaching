#! /usr/bin/env python

fibs = [0, 1]

def fib(n):
    if (len(fibs) > n and fibs[n] != -1):
        return fibs[n]
    else:
        # here we build the list up to n
        for i in range(len(fibs), n+1):
            fibs.append(fibs[-1] + fibs[-2])

        return fibs[n]


def main():
    print("fib(5) = " + str(fib(5)))
    print("fib(10) = " + str(fib(10)))
    print("fib(50) = " + str(fib(50)))
    print("fib(100) = " + str(fib(100)))

if __name__ == "__main__":
    main()