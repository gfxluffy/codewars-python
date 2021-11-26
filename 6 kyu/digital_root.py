def digital_root(n):
    if n%10 == n:
        return n
    sum = n%10 + digital_root(n//10)
    return sum if sum < 10 else digital_root(sum)


'''
def digital_root(n):
	return n if n < 10 else digital_root(sum(map(int,str(n))))

print(digital_root(16))
'''