import utils
from part1 import run


def debug(debug_list):

    corrections = {'nop': 'jmp',
                   'jmp': 'nop'}

    for i in range(len(debug_list)):
        if debug_list[i][0] in corrections:
            debug_list[i][0] = corrections[debug_list[i][0]]
            ans, ext = run(debug_list, detect_exit=True)
            if ext:
                return ans
            debug_list[i][0] = corrections[debug_list[i][0]]


def main():
    d8 = utils.read_xsv('day8eg.csv')
    print(debug(d8))


if __name__ == '__main__':
    main()
