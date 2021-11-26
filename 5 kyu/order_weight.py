def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key=lambda x:sum(map(int,x))))