def fib(n):
    if n < 0:
        return (-1)**(n % 2 + 1) * fib_iter(1, 0, 0, 1, abs(n))
    return fib_iter(1, 0, 0, 1, n)

def fib_iter(a, b, p, q, count):
    if count == 0:
        return b
    if count % 2 == 0:
        return fib_iter(a, b, p*p + q*q, q*q + 2*p*q, count/2)
    else:
        return fib_iter(b*q + a*q + a*p, b*p + a*q, p, q, count-1)