import math

cache = {}

def squares_sum_cache(i):
    if i not in cache:
        cache[i] = sum(div * div for div in range(1, i // 2 + 1) if i % div == 0) + i ** 2
        return cache[i]
    return cache[i]

def list_squared(m, n):
    int_list = []
    for i in range(m, n + 1):
        squares_sum = squares_sum_cache(i)
        if math.sqrt(squares_sum).is_integer():
            int_list.append([i, squares_sum])
    return int_list