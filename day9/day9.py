import utils


def all_sums_unique(input_list):
    input_list = set(input_list)
    out = []
    for i in input_list:
        for j in input_list:
            out.append(i+j)
    return out


def day9(input_list):
    for i in range(len(input_list)-26):
        test = all_sums_unique(input_list[i:i+25])
        if input_list[i+25] not in test:
            return input_list[i+25]
    pass


def day9part2(input_list, target):

    for i in range(1000):
        count_range = []
        for j in range(i, 1000):
            count_range.append(input_list[j])
            s = sum(count_range)
            if s > target:
                break
            elif s == target:
                count_range.sort()
                return count_range[0] + count_range[-1]


def main():
    d9 = utils.read_list('day9.csv', data_type=int)
    t = day9(d9)
    s = day9part2(d9, t)
    print(t, s)

if __name__ == '__main__':
    main()