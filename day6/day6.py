import utils

'''
Advent of code 2020
Day 6
'''


def day6(input_list):
    n1 = 0
    n2 = 0
    for g in input_list:
        dd = {}
        for p in g:
            for q in p:
                if q in dd:
                    dd[q] += 1
                else:
                    dd[q] = 1
        n1 += len(dd)

        # PART 2
        for i in dd:
            if dd[i] == len(g):
                n2 += 1

    return n1, n2


def main():
    d6 = utils.read_xsv('day6.csv', rowdelim='\n\n', coldelim='\n')
    print(day6(d6))


if __name__ == '__main__':
    main()
