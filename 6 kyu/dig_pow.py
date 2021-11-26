def dig_pow(n, p):
    dig_sum = sum(d**(p+x) for x, d in enumerate(map(int, str(n))))
    return dig_sum / n if dig_sum % n == 0 else -1