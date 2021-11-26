def sum_two_smallest_numbers(numbers):
    a = min(numbers)
    numbers.remove(a)
    b = min(numbers)
    return a + b

'''
hey = [5, 6, 7, 1, 2, 3, 4]

def sum_two_smallest_numbers(numbers):
	numbers.sort()
	return sum(numbers[:2])

print(sum_two_smallest_numbers(hey))
'''