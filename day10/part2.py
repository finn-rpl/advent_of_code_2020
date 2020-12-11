import utils


def day10(input_list):
    input_list.sort()
    input_list = [0] + input_list + [input_list[-1] + 3]

    joltlist = []
    listcount = -1

    for i in range(len(input_list) - 1):
        if input_list[i + 1]-input_list[i] == 1:
            listcount += 1
        if input_list[i + 1]-input_list[i] == 3:
            if listcount > 0:
                joltlist.append(listcount)
            listcount = -1

    paths = 1
    pdict = {1: 2, 2: 4, 3: 7}
    for i in joltlist:
        paths = paths * pdict[i]

    return paths


def main():
    d10 = utils.read_list('day10.csv', data_type=int)
    print(day10(d10))


if __name__ == '__main__':
    main()