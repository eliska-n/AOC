winning_strategies = {
	"A Y": 6,
	"B Z": 6,
	"C X": 6,
	"A X": 3,
	"B Y": 3,
	"C Z": 3,
}

points = {
	"X": 1,
	"Y": 2,
	"Z": 3,
}

# first star
with open("./input.txt", "r") as f:
	result1 = sum(
		[winning_strategies.get(attempt.strip(), 0) + points.get(attempt.strip().split()[-1]) 
		for attempt in 
		f.readlines()]
	)
print(result1)


play_strategy = {
	"A X": "A Z",
	"A Y": "A X",
	"A Z": "A Y",
	"B X": "B X",
	"B Y": "B Y",
	"B Z": "B Z",
	"C X": "C Y",
	"C Y": "C Z",
	"C Z": "C X",
}

# second star
with open("./input.txt", "r") as f:
	result2 = sum(
		[winning_strategies.get(attempt, 0) + points.get(attempt.split()[-1]) 
		for attempt in 
		[play_strategy.get(line.strip()) for line in f.readlines()]]
	)
print(result2)