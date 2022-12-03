priorities = {
	item: priority
	for priority, item in enumerate(
		".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	)
}

with open("./input.txt", "r") as f:

	result = sum(
		[
			priorities.get(item)
			for item in [
				[letter for letter in comp1 if letter in comp2][0]
				for comp1, comp2 in [
					(line[: len(line.strip()) // 2], line[len(line.strip()) // 2 :])
					for line in f.readlines()
				]
			]
		]
	)


print(result)
