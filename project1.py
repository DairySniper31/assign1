# Project 1

# Question 5

def fib(a):
    if a <= 1:
        return a
    else:
        return fib(a - 1) + fib(a - 2)


# Question 7

def fibItHelper(n, a, b):
    if n <= 0:
        return a
    elif n == 1:
        return b
    else:
        return fibItHelper(n-1, b, a+b)


def fibIt(n):
    return fibItHelper(n, 0, 1)
