import re


def process_input():
    with open("input.txt") as f:
        input = f.read()
    return input


def part_one():
    values = process_input()
    entries = values.split("\n\n")
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid_count = 0
    for entry in entries:
        data_pairs = re.split(r'[\n\s]', entry)
        keys = set()
        for kv in data_pairs:
            if not kv:
                continue
            k, v = kv.split(":")

            keys.add(k)
        if required_fields.issubset(keys):
            valid_count += 1
    print(f"Part one: There are {valid_count} valid passports.")


def part_two():
    values = process_input()
    entries = values.split("\n\n")
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid_ecl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    valid_count = 0
    for entry in entries:
        data_pairs = re.split(r'[\n\s]', entry)
        keys = set()
        valid = True
        for kv in data_pairs:
            if not kv:
                continue
            k, v = kv.split(":")
            if k == "byr" and len(v) and (int(v) < 1920 or int(v) > 2020):
                valid = False
            if k == "iyr" and len(v) and (int(v) < 2010 or int(v) > 2020):
                valid = False
            if k == "eyr" and len(v) and (int(v) < 2020 or int(v) > 2030):
                valid = False
            if k == "hgt":
                if "cm" not in v and "in" not in v:
                    valid = False
                else:
                    unit = v[-2:]
                    value = int(v[:-2])
                    if unit == "cm" and (value < 150 or value > 193):
                        valid = False
                    if unit == "in" and (value < 59 or value > 76):
                        valid = False
            if k == "hcl" and not re.match(r"^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", v):
                valid = False
            if k == "ecl" and v not in valid_ecl:
                valid = False
            if k == "pid" and (len(v) != 9 or not v.isdigit()):
                valid = False
            keys.add(k)
        if required_fields.issubset(keys) and valid:
            valid_count += 1
    print(f"Part two: There are {valid_count} valid passports.")


if __name__ == '__main__':
    part_one()

    part_two()