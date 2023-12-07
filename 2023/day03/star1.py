with open("data.txt") as f:
	lines = f.read().split("\n")
	
weird_characters_coordinates = {}  # y: x
numbers = []
for y, line in enumerate(lines):
	for x, char in enumerate(line):
		if char == ".":
			continue
		elif char.isdigit():
			if x!=0 and line[x-1].isdigit():
				# this one has been already taken in previous cycle
				continue
			number = char
			add = 1
			if x < len(line)-1:
				next_char = line[x+add]
				while next_char.isdigit():
					number += next_char
					add += 1
					if x+add >= len(line)-1:
						break
					next_char = line[x+add]
			number = int(number)
			adjacent_coordinates = {
				y-1: [i for i in range(x-1, x+add+1)],
				y: [x-1, x+add],
				y+1: [i for i in range(x-1, x+add+1)]
			}
			numbers.append((number, adjacent_coordinates))
		else:
			if y in weird_characters_coordinates:
				weird_characters_coordinates[y].append(x)
			else:
				weird_characters_coordinates[y] = [x]

# now compare
part_numbers_sum = 0
for number, adjacent_coordinates in numbers:

	for y, x_list in adjacent_coordinates.items():
		if y not in weird_characters_coordinates:
			continue
		if any(x for x in x_list if x in weird_characters_coordinates[y]):
			# number is a part number
			part_numbers_sum += number

#print(numbers)
#print(weird_characters_coordinates)

print(part_numbers_sum)

# 537939 is too low

