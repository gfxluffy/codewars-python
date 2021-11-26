def accum(s):
    return '-'.join(c+c.lower()*i for i, c in enumerate(s.upper()))

# print('-'.join(c+c.lower()*i for i, c in enumerate('ABCD')))