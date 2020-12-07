import utils

'''
Advent of code 2020
Day 2
'''


def part1(input_data):
    valid_passwords = 0
    for line in input_data:
        bounds = line[0].split('-')
        char = line[1][0]
        pw = line[2]
        if int(bounds[0]) <= pw.count(char) <= int(bounds[1]):
            valid_passwords += 1
    return valid_passwords


def part2(input_data):
    valid_passwords = 0
    for line in input_data:
        bounds = line[0].split('-')
        char = line[1][0]
        pw = line[2]
        if (pw[int(bounds[0])-1] == char) != (pw[int(bounds[1])-1] == char):
            valid_passwords += 1
    return valid_passwords


def main():
    print(part1(utils.read_xsv('day2.csv')))
    print(part2(utils.read_xsv('day2.csv')))


if __name__ == '__main__':
    main()
