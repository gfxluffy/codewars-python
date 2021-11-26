def last_digit(lst):
    print(lst)
    if not lst:
        return 1
    e = lst[-1]
    for b in lst[-2::-1]:
        if e % 100 == 0:
            e = int(str(e).strip('0') + '00')
        e = b ** (e % 1000)
    return int(str(e)[-1])