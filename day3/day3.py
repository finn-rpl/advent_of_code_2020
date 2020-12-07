import utils

'''
Advent of code 2020
Day 3
'''


def tree_hit(input_data, xs, ys):
    x = xs
    y = ys
    out = 0
    while y <= len(input_data)-1:
        if x >= len(input_data[0]):
            x = x - len(input_data[0])
        if input_data[y][x] == '#':
            out += 1
        x += xs
        y += ys
    return out


def main():
    d3 = utils.read_list('day3.csv')
    print(tree_hit(d3, 3, 1))
    print(tree_hit(d3, 1, 1) * tree_hit(d3, 3, 1) * tree_hit(d3, 5, 1) * tree_hit(d3, 7, 1) * tree_hit(d3, 1, 2))


if __name__ == '__main__':
    main()