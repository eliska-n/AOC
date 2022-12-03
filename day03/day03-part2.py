priorities = {
	item: priority
	for priority, item in enumerate(
		".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	)
}

with open("./input.txt", "r") as f:

	input = f.readlines()

	result = sum(
		[
			priorities.get(item)
			for item in [
				[letter for letter in elf1 if letter in elf2 and letter in elf3][0]
				for elf1, elf2, elf3 in [
					input[start:stop]
					for start, stop in [
						(i, i + 3) for i in range(len(input)) if i % 3 == 0
					]
				]
			]
		]
	)


print(result)
