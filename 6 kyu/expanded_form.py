def expanded_form(num):
    num_list = list(map(int, str(num)))
    return ' + '.join(str(d * (10 ** (len(num_list) - x - 1))) for x, d in enumerate(num_list) if d != 0)

# def expanded_form(num):
#     exp_num = [str(d * (10 ** x)) for x, d in enumerate(list(map(int, str(num)))[::-1]) if d != 0]
#     return ' + '.join(exp_num[::-1])