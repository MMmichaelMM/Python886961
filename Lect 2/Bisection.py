"""
This function uses the bisection method to find a root of the function f
in the interval [a,b] to within Nmax iterations.
It prints a table of the iteration number, the endpoints a and b, the midpoint c,
and the value f(c) at each iteration.
"""

def bisect(f, a, b, Nmax):
    n = 1
    while n <= Nmax:
        c = (a+b)/2.0
        print('{0:2d} {1:3.6f} {2:3.6f} {3:3.6f} {4:3.6f}'.\
              format(n, a, c, b, f(c)))
        if f(c) == 0 or n == Nmax:
            return c
        else:
            n = n+1
            if f(c)*f(a) < 0:
                b = c
            else:
                a = c


def func1(x):
    return x**3-x-2


alpha = bisect(func1, 1, 2, 15)
print('the root is: ', alpha)
