def divisors(integer):
    div_list = [div for div in range(2,integer) if integer%div == 0]
    if div_list:
        return div_list
    return '{} is prime'.format(integer)