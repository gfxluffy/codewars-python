def validate_battlefield(field):
	ship_count = [0, 0, 0, 0] # [s, d, c, b]

	# Pad zeros
	for i in range(10):
		field[i].insert(0, 0)
		field[i].append(0)

	field.insert(0, [0]*12)
	field.append([0]*12)


	# Horizontal pass
	for k in range(1,5):
		for i in range(1, 11):
			for j in range(1,11):
				if field[i][j:j+k] == [1]*k:
					if field[i-1][j-1:j+k+1] == [0]*(k+2) and \
						field[i+1][j-1:j+k+1] == [0]*(k+2) and \
						field[i][j-1] == 0 and \
						field[i][j+k] == 0:
						field[i][j:j+k] = [0]*k
						ship_count[k-1] += 1
						#print('hey', k, i, j)

	# Vertical pass
	field = list(map(list, zip(*field)))
	for k in range(1,5):
		for i in range(1, 11):
			for j in range(1,11):
				if field[i][j:j+k] == [1]*k:
					if field[i-1][j-1:j+k+1] == [0]*(k+2) and \
						field[i+1][j-1:j+k+1] == [0]*(k+2) and \
						field[i][j-1] == 0 and \
						field[i][j+k] == 0:
						field[i][j:j+k] = [0]*k
						ship_count[k-1] += 1
						#print('hey', k, i, j)

	# for row in field:
	# 	print(row)
	# print(ship_count)

	return ship_count == [4, 3, 2, 1] and all(v==0 for l in field for v in l)

battleField =  [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
				[1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
				[1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
				[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
				[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battleField))
