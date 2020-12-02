def process_input():
    values = []
    with open("input.txt") as f:
        for line in f:
            values.append(int(line))
    return values


def part_one():
    numbers = process_input()
    for i, n1 in enumerate(numbers):
        for j, n2 in enumerate(numbers[i+1:]):
            if n1 + n2 == 2020:
                print(f"Part 1: The answer is: {n1*n2}")
                return


def part_two():
    numbers = process_input()
    for i, n1 in enumerate(numbers):
        for j, n2 in enumerate(numbers[i+1:]):
            for k, n3 in enumerate(numbers[i+2:]):
                if n1 + n2 + n3 == 2020:
                    print(f"Part 2: The answer is: {n1*n2*n3}")
                    return


if __name__ == "__main__":
    part_one()
    part_two()
