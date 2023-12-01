with open("./input_example.txt", "r") as f:
	input = f.readlines()

nodes = [(10, 10) for i in range(10)]


vizualization = [["." for i in range(20)] for i in range(20)]

tails = set()

for line in input:
	print(line)
	f = line.strip().split(" ")
	direction = f[0]
	count = int(f[1])

	while count > 0:
		for n, node in enumerate(nodes):
			if n == 0:
				head = node
				if direction == "U":
					new_head = (head[0], head[1] - 1)
				elif direction == "D":
					new_head = (head[0], head[1] + 1)
				elif direction == "R":
					new_head = (head[0] + 1, head[1])
				if direction == "L":
					new_head = (head[0] -1, head[1])
				nodes[n] = new_head
			
			else:
				tail = node
				head = nodes[n-1]

				#print(tail, head)

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

				if n == 9:
					tails.add(new_tail)

				x = (tail[0] - head[0])
				y = (tail[1] - head[1])
				if x**2 > 4 or y**2 > 4:
					print(tail, head)
					print("!!!")
					print(x, y)
				

				nodes[n] = new_tail
				

		count -= 1
	for n, x in enumerate(nodes):
		vizualization[x[1]][x[0]] = str(n)
	print("\n".join("".join(line) for line in vizualization))
	print("---")
	vizualization = [["." for i in range(20)] for i in range(20)]
print(len(tails))

