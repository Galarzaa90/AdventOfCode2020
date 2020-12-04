def process_input():
    values = []
    with open("input.txt") as f:
        for line in f:
            values.append(line.strip())

    return values

def part_one():
    values = process_input()
    x_pos = 0
    trees = 0
    for line in values:
        size = len(line)
        point = line[x_pos - (int(x_pos / size) * size)]
        if point == '#':
            trees += 1
        x_pos += 3
    print(f"Part one: {trees} trees found.")


def part_two():
    values = process_input()
    sequence = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    result = 1
    for x_steps, y_steps in sequence:
        x_pos = 0
        y_pos = 0
        trees = 0
        while y_pos < len(values):
            line = values[y_pos]
            size = len(line)
            point = line[x_pos - (int(x_pos / size) * size)]
            if point == '#':
                trees += 1
            x_pos += x_steps
            y_pos += y_steps
        print(f"Trees: {trees}")
        result *= trees
    print(f"Part two: The multiplication of trees is {result}.")


if __name__ == '__main__':
    part_one()
    part_two()