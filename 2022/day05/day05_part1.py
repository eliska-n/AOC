import re

with open("./input.txt", "r") as f:
	input = f.read()
	schema = input.split("\n\n")[0]
	instructions = input.split("\n\n")[1]

schema = schema.split("\n")
stacks = [[line[i] for line in schema if line[i] != ' '] for i in range(len(schema[0])) if schema[-1][i] != ' ']
for stack in stacks:
	stack.reverse()
	stack.pop(0)


for instruction in instructions.split("\n"):
	res = re.match(r"move (.*) from (.*) to (.*)", instruction)
	count = int(res[1])
	from_stack = int(res[2])
	to_stack = int(res[3])
	while count > 0:
		crate = stacks[from_stack-1].pop(-1)
		stacks[to_stack-1].append(crate)
		count -= 1

result = "".join([stack[-1] for stack in stacks])
print(result)