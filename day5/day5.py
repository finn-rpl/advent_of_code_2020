import utils

'''
Advent of code 2020
Day 5
'''


def day5(input_list):
    ind = {0: 64, 1: 32, 2: 16, 3: 8, 4: 4, 5: 2, 6: 1, 7: 4, 8: 2, 9: 1}
    highest = 0
    # PART 2 Variables
    seats = [[0 for i in range(8)] for i in range(128)]
    ids = []
    seatid = None

    for bp in input_list:
        row = 0
        col = 0
        for i in range(len(bp)):
            if bp[i] == 'B':
                row += ind[i]
            elif bp[i] == 'R':
                col += ind[i]
        id = (row * 8) + col
        if id > highest:
            highest = id
        # PART2 addition
        ids.append(id)
        seats[row][col] = 1

    # PART2 addition
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == 0 and (i*8)+j-1 in ids and (i*8)+j+1 in ids:
                seatid = (i*8)+j

    return highest, seatid


def main():
    d5 = utils.read_list('day5.csv')
    print(day5(d5))


if __name__ == '__main__':
    main()
