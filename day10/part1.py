import utils


def day10(input_list):
    input_list.sort()
    input_list = [0] + input_list + [input_list[-1] + 3]
    jolt = 0
    jolts3 = 0

    for i in range(len(input_list)-1):
        if input_list[i+1]-input_list[i] == 1:
            jolt += 1
        if input_list[i+1]-input_list[i] == 3:
            jolts3 += 1
    return jolt*jolts3


def main():
    d10 = utils.read_list('day10.csv', data_type=int)
    print(day10(d10))


if __name__ == '__main__':
    main()