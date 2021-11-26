def high(x):
    score = [sum(ord(c)-96 for c in word) for word in x.split(' ')]
    return x.split(' ')[score.index(max(score))]


# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

#    # get the max of the list based on the comparison of the return values
