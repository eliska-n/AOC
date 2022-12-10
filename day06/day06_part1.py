with open("./input.txt", "r") as f:
	input = f.read()


for i in range(len(input)):
	if len(set(input[i:i+4])) == 4:
		break

result = i+4
print(result)
