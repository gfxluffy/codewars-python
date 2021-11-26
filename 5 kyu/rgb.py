def rgb(r, g, b):   
    return '%.2X%.2X%.2X'% tuple(max(0, min(255, n)) for n in [r, g, b])


# def rgb(r, g, b):
# 	return '{:02X}{:02X}{:02X}'.format(*[max(0, min(255, n)) for n in [r, g, b]])

# print(rgb(1,2,3))

# a = 1
# b = 2
# c = 3
# #k = [max(0, min(255, n)) for n in [a, b, c]]

# def clamp(n, min_n, max_n):
# 	return min(max_n, max(min_n, n))

# print(clamp(35, 0, 255))

# print('%.2X%X'%(2, 255))
