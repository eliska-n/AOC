with open("./input_star1.txt", "r") as f:
	result = sum(
		sorted([
			sum([
				int(calorie) for calorie in elf.split()
			]) for elf in f.read().split("\n\n")
		])[-3:]
	)

print(result)
