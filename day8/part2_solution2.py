import utils
from part1_solution2 import run


def debug(debug_list):
    corrections = {'nop': 'jmp',
                   'jmp': 'nop'}
    ans = None
    for i in range(len(debug_list)):
        if debug_list[i][0] in corrections:
            debug_list[i][0] = corrections[debug_list[i][0]]
            try:
                ans = run(debug_list)
            except StopIteration:
                pass
            debug_list[i][0] = corrections[debug_list[i][0]]
    return ans


def main():
    d8 = utils.read_xsv('day8.csv')
    print(debug(d8))


if __name__ == '__main__':
    main()
