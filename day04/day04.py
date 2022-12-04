with open("./input.txt", "r") as f:

    a = [
        [(int(elf.split("-")[0]), int(elf.split("-")[1])) for elf in group]
        for group in [line.strip().split(",") for line in f.readlines()]
    ]

    print("star1")
    print(
        sum(
            [
                1
                for group in a
                if (group[0][0] >= group[1][0] and group[0][1] <= group[1][1])
                or (group[1][0] >= group[0][0] and group[1][1] <= group[0][1])
            ]
        )
    )

    print("star2")
    print(
        sum(
            [
                1
                for group in a
                if not ((group[0][1] < group[1][0]) or (group[0][0] > group[1][1]))
            ]
        )
    )
