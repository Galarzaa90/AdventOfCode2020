def process_input():
    values = []
    with open("input.txt") as f:
        for line in f:
            values.append(line.strip())
    return values

def part_one():
    lines = process_input()
    highest = 0
    for line in lines:
        rows = line[:8]
        columns = line[7:]
        _range = [0, 127]
        for char in rows:
            diff = (_range[1] - _range[0] + 1) / 2
            if _range[0] == _range[1]:
                break
            if char == 'F':
                _range[1] -= diff
            else:
                _range[0] += diff
        row = _range[0]
        _range = [0, 7]
        for char in columns:
            diff = (_range[1] - _range[0] + 1) / 2
            if _range[0] == _range[1]:
                break
            if char == 'L':
                _range[1] -= diff
            else:
                _range[0] += diff
        column = _range[0]
        seat_id = row * 8 + column
        highest = int(max(seat_id, highest))
    print(f"Part one: The highest seat id is {highest}")


if __name__ == '__main__':
    part_one()