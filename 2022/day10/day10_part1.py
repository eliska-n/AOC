class CPU():
	def __init__(self):
		self.cycle = 0
		self.x = 1
		self.result = 0

	def tick(self):
		self.cycle += 1
		if self.cycle == 20 or ((self.cycle-20) % 40 == 0 and self.cycle <=220):
			signal = self.cycle * self.x
			print("cycle", self.cycle)
			print("signal", signal)
			self.result += signal

	def iterate(self):
		with open("./input.txt", "r") as f:
			input = f.readlines()
		for line in input:
			line = line.strip()
			if line == "noop":
				self.tick()
			else:
				self.tick()
				self.tick()
				self.x += int(line.lstrip("addx "))


if __name__ == "__main__":
	cpu = CPU()
	cpu.iterate()
	print(cpu.result)


	
	
