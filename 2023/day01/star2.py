import re

with open("data.txt") as f:
    lines = f.readlines()

res = 0

lexicon = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in lines:
    line = line.rstrip("\n")
    first = next(iter(re.findall(r"1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine", line)))
    first = lexicon.get(first, first)
    last = next(iter(re.findall(r"1|2|3|4|5|6|7|8|9|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", line[::-1])))[::-1]
    last = lexicon.get(last, last)

    r = first + last
    r = int(r)
    res += r

print(res)