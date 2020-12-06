import utils


def find_two_sums(input_list, desired_total):
    for i in input_list:
        for k in input_list:
            if i+k == desired_total:
                return i*k


def find_three_sums(input_list, desired_total):
    for i in input_list:
        for j in input_list:
            for k in input_list:
                if i+j+k == desired_total:
                    return i*j*k


if __name__ == '__main__':
    print(find_two_sums(utils.read_list('day1.csv', int), 2020))
    print(find_three_sums(utils.read_list('day1.csv', int), 2020))

