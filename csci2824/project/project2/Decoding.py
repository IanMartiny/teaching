#! /usr/bin/env python
from fractions import gcd
from math import *
import random

import sys

def computePow (m,n,e): 
    """ The idea is to compute m^e mod n """
    p = m # p will hold m^{2^j}
    r = 1 # r is the result
    while ( e > 0):
        if (e %2 == 1):
            r = (r * p)%n
        p = (p*p) % n
        e = e / 2
    return r %n

def decodeMessageList (l, n, d):
    l = map( lambda j: computePow(j,n,d) % 256, l)
    l1 = map ( chr, l)
    s = ''.join(l1)
    return s

def computeGCD(u,v):
    """ The euclidean GCD algorithm """
    # if (u > v):
    #     u,v = v,u
    u1,u2,u3 = 1,0,u
    v1,v2,v3 = 0,1,v
    while (v3 > 0):
        q = u3/v3
        t1 = u1 - q * v1
        t2 = u2 - q * v2
        t3 = u3 - q * v3
        u1,u2,u3 = v1,v2,v3
        v1,v2,v3 = t1,t2,t3
    return u1,u2,u3


def computePrivateKey(k,e):
    (d,v,l) = computeGCD(e,k)
    assert (l == 1)
    assert( d * e + v * k == 1)
    # d * e + v * k = 1
    # k * e - e * k = 0
    # therefore (d + m* k)  * e + (v - m * e) k = 1
    if ( d < 0):
        m = int (-d/k) + 1 
        d = d + m * k
    return d

# if you are using a language other than Python, you can change the following
# line of code, each one of the 1's should be just ONE of the factors of the 
# public keys. i.e. p[1] should be one of the prime factors the first number in
# public-1.txt, the other prime factor will be found by the code provided here.
# The zero, is unused by the program, so you may as well leave that alone.

p = [0,1,1,1,1]

def main():
    for i in range(1,5):
        f = open("public-{:d}.txt".format(i),"r")
        nums = f.readlines()
        f.close()
        

        n = int(nums[0])
        e = int(nums[1])

        # Factor the number here!
        # your code will go here!
        # p[i] = factor(n)

        print(str(n) + " = " + str(p[i]) + " * " + str(n/p[i]))
        q = n/p[i]

        k = (p[i]-1)*(q-1)

        try:
            d = computePrivateKey(k,e)
        else:
            print("Could not compute private key, n factored incorrectly. Trying next file")
            continue
        
        f = open("message-{:d}.txt".format(i),"r")
        dlist = []
        for line in f:
            dlist.append(int(line))
        print("     >>Encoded message: " + str(dlist))
        f.close()

        s = decodeMessageList(dlist,n,d)
        print("     >> decoded message: " + s)

if __name__ == "__main__":
    main()
