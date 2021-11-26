def sum_of_intervals(intervals):
    u = set()
    for l, r in intervals:
        for n in range(l,r):
            u.add(n)
    return len(u)

# def sum_of_intervals(intervals):
#     n_line = sorted(set([i for t in intervals for i in t]))
#     summ = 0
#     for a,b in zip(n_line,n_line[1:]):
#         for l, r in intervals:
#             if l <= (b+a)/2 <= r:
#                 summ += (b-a)
#                 break
#     return summ


# hey = [(1, 4),(3, 6), (3, 5), (6,7)]
# intervals = [(-127, 347), (-61, 238), (226, 332)]

