class CPU():
	def __init__(self, crt):
		self.crt = crt
		self.cycle = 0
		self.x = 1
		self.result = 0

	def tick(self):
		self.cycle += 1
		self.crt.draw(self.cycle, self.x)

	def process(self, input):
		if input == "noop":
			self.tick()
		else:
			self.tick()
			self.tick()
			self.x += int(input[5:])


class CRT():
	def __init__(self):
		self.output = ""

	def draw(self, cycle, x):
		sprite_middle = x % 40
		position = (cycle -1) % 40
		sprite = [sprite_middle - 1, sprite_middle, sprite_middle + 1]
		if position in sprite:
			self.output += "#"
		else:
			self.output += "."

	def print_output(self):
		for i in range(0, 220, 40):
			print(self.output[i: i+40])



if __name__ == "__main__":
	crt = CRT()
	cpu = CPU(crt)
	with open("./input.txt", "r") as f:
		for line in f.readlines():
			cpu.process(line.strip())
	crt.print_output()
