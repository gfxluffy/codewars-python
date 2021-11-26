import itertools
adj_digits = {'1': ['1', '2', '4'],
              '2': ['2', '1', '3', '5'],
              '3': ['3', '2', '6'],
              '4': ['4', '1', '5', '7'],
              '5': ['5', '2', '4', '6', '8'],
              '6': ['6', '3', '5', '9'],
              '7': ['7', '4', '8'],
              '8': ['8', '0', '5', '7', '9'],
              '9': ['9', '6', '8'],
              '0': ['0', '8']
             }

def get_pins(observed):
    adj_set = [adj_digits[digit] for digit in map(str, observed)]
    combination = [''.join(c) for c in itertools.product(*adj_set)]
    return combination


# import itertools
# from itertools import product

# a = [1,2,3]
# b = [4,5,6]


# observed = [a, b]
# print(list(product(*observed)))