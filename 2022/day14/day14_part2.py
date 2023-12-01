with open("./input.txt", "r") as f:
	input = f.readlines()

start = (500, 0)
cave = [["." for x in range(1000)] for y in range(195)]

rocks = []
for line in input:
	line = line.strip("\n")
	points = line.split(" -> ")
	for n, point in enumerate(points[:-1]):
		left = point.split(",")
		right = points[n+1].split(",")
		x_left = int(left[0])
		x_right = int(right[0])
		y_left = int(left[1])
		y_right = int(right[1])
		for x in range(min(x_left, x_right), max(x_left, x_right)+1):
			for y in range(min(y_left, y_right), max(y_left, y_right)+1):
				rocks.append((x, y))

last_rock = 0
for rock in rocks:
	if rock[1] > last_rock:
		last_rock = rock[1]
	cave[rock[1]][rock[0]] = "#"

# add floor
y = last_rock + 2
cave[y] = ["#" for x in range(1000)]


units = 0
while True:
# for i in range(20000):
	sand = start

	while True:
		if cave[sand[1]+1][sand[0]] == ".":
			sand = (sand[0], sand[1]+1)
		else:
			if cave[sand[1]+1][sand[0]-1] == ".":  # index out of control? (-1)
				sand = (sand[0]-1, sand[1]+1)
			elif cave[sand[1]+1][sand[0]+1] == ".":
				sand = (sand[0]+1, sand[1]+1)
			else:
				cave[sand[1]][sand[0]] = "o"
				units += 1
				break

	if sand == start:
		break

print(units)
