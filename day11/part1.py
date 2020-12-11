import utils

_directions_ = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1)]


def rule(m, y, x):
    count = 0
    global _directions_

    for i in _directions_:
        try:
            if m[y+i[0]][x+i[1]] == '#' and 0 <= i[0]+y and 0 <= i[1]+x:
                count += 1
        except IndexError:
            pass
    return count


def step(matrix, max_neighbors):
    out = []

    for line in range(len(matrix)):
        ln = ''
        for i in range(len(matrix[line])):
            if matrix[line][i] == '.':
                ln += '.'
                continue
            if rule(matrix, line, i) > max_neighbors[matrix[line][i]]:
                ln += 'L'
            else:
                ln += '#'
        out.append(ln)
    return out


def day11(matrix, max_neighbors):
    history = ['test']

    while history[-1] != matrix:
        history.append(matrix.copy())
        matrix = step(matrix, max_neighbors)

    count = 0
    for line in matrix:
        for i in line:
            if i == '#':
                count += 1

    return count


def main():
    max_neighbors = {'L': 0, '#': 3}
    matrix = utils.read_list('day11.csv')

    print(day11(matrix, max_neighbors))


if __name__ == '__main__':
    main()
