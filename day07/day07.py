with open("./input.txt", "r") as f:
	input = f.readlines()

breadcrumbs = []
directories = {}

for line in input:
	line = line.strip()
	if line.startswith("$ cd"):
		directory = line[5:]
		if directory == "..":
			breadcrumbs.pop(-1)
		else:
			if directory == "/":
				path = "."
			else:
				path = "/".join(breadcrumbs) + "/" + directory
			breadcrumbs.append(path)
	elif line.startswith("dir"):
		continue
	elif line.startswith("$ ls"):
		continue
	else:
		file_size = int(line.split(" ")[0])
		for directory in breadcrumbs:
			current_size = directories.get(directory)
			if current_size is None:
				directories[directory] = file_size
			else:
				directories[directory] = file_size + current_size

# part1
result = 0
for dir, size in directories.items():
	if size <= 100000:
		result += size

print(result)

# part2
outermost_directory = directories.get(".")
unused_space = 70000000 - outermost_directory
to_delete = 30000000 - unused_space

diffs = {k: v - unused_space for k,v in directories.items()}
dir = min([i for i in diffs.values() if i > 0])

print(dir)