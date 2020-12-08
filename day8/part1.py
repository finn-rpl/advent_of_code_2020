import utils


def run(input_list, detect_exit=False):
    line = 0
    acc = 0
    instruction = input_list[line]
    history = []

    while line not in history:
        history.append(line)

        if instruction[0] == 'acc':
            acc += int(instruction[1])
        if instruction[0] == 'jmp':
            line += int(instruction[1])
        else:
            line += 1

        try:
            instruction = input_list[line]
        except IndexError:
            return acc, True if detect_exit else acc

    return (acc, False) if detect_exit else acc


def main():
    d8 = utils.read_xsv('day8.csv')
    print(run(d8))


if __name__ == '__main__':
    main()
