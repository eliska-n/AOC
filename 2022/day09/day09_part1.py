with open("./input.txt", "r") as f:
	input = f.readlines()

head = (0, 0)
tail = (0, 0)

tails = set()

for line in input:
	f = line.strip().split(" ")
	direction = f[0]
	count = int(f[1])
	print(direction, count)

	while count > 0:
		if direction == "U":
			new_head = (head[0], head[1] + 1)
		elif direction == "D":
			new_head = (head[0], head[1] - 1)
		elif direction == "R":
			new_head = (head[0] + 1, head[1])
		if direction == "L":
			new_head = (head[0] -1, head[1])

		head = new_head

		if ((tail[0] - head[0])**2)**0.5 <= 1 and ((tail[1] - head[1])**2)**0.5 <= 1:
			new_tail = tail

		# ......
		# T.H...
		# ......
		elif (tail[0] - head[0]) < -1 and (tail[1] - head[1]) == 0:
			new_tail = (tail[0] + 1, tail[1])

		# ......
		# ..H.T.
		# ......
		elif (tail[0] - head[0]) > 1 and (tail[1] - head[1]) == 0:
			new_tail = (tail[0] - 1, tail[1])

		# ..H...
		# ......
		# ..T...
		elif (tail[0] - head[0]) == 0 and (tail[1] - head[1]) < -1:
			new_tail = (tail[0], tail[1] + 1)

		# ..T...
		# ......
		# ..H...
		elif (tail[0] - head[0]) == 0 and (tail[1] - head[1]) > 1:
			new_tail = (tail[0], tail[1] - 1)

		# diagonal


		# .H....
		# ..H...
		# T.....
		elif ((tail[0] - head[0]) < -1 and (tail[1] - head[1]) == -1) or ((tail[0] - head[0]) == -1 and (tail[1] - head[1]) < -1):
			new_tail = (tail[0] + 1, tail[1] + 1)


		# ...H..
		# ..H...
		# ....T.
		elif ((tail[0] - head[0]) > 1 and (tail[1] - head[1]) == -1) or ((tail[0] - head[0]) == 1 and (tail[1] - head[1]) < -1):
			new_tail = (tail[0] - 1, tail[1] + 1)

		# ...T..
		# .H....
		# ..H...
		elif ((tail[0] - head[0]) > 1 and (tail[1] - head[1]) == 1) or ((tail[0] - head[0]) == 1 and (tail[1] - head[1]) > 1):
			new_tail = (tail[0] - 1, tail[1] - 1)

		elif ((tail[0] - head[0]) < -1 and (tail[1] - head[1]) == 1) or ((tail[0] - head[0]) == -1 and (tail[1] - head[1]) > 1):
			new_tail = (tail[0] + 1, tail[1] - 1)

		
		tails.add(new_tail)
		tail = new_tail
		print(new_head, new_tail)
		count -= 1

print(len(tails))

