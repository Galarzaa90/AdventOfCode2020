import re


def process_input():
    values = []
    pattern = re.compile(r'(\d+)-(\d+)\s(\w): (\w+)')
    with open("input.txt") as f:
        for line in f:
            m = pattern.search(line)
            number1 = int(m.group(1))
            number2 = int(m.group(2))
            letter = m.group(3)
            password = m.group(4)
            values.append((number1, number2, letter, password))
    return values


def part_one():
    valid_passwords = 0
    for minimum, maximum, letter, password in process_input():
        letter_count = password.count(letter)
        if maximum >= letter_count >= minimum:
            valid_passwords += 1
    print(f"Part one: There are {valid_passwords} valid passwords.")


def part_two():
    valid_passwords = 0
    for pos1, pos2, letter, password in process_input():
        if (password[pos1-1] == letter) ^ (password[pos2-1] == letter):
            valid_passwords += 1
    print(f"Part two: There are {valid_passwords} valid passwords.")


if __name__ == '__main__':
    part_one()
    part_two()
